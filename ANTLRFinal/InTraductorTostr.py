from TraductorParser import *
from TraductorListener import TraductorListener
import re
class InTraductorTostr(TraductorListener):
    def __init__(self):
        self.codigo = []  # Lista para almacenar las líneas de código traducidas.
        self.nivel_indentacion = 0  # Controla el nivel de indentación.

    def agregar_linea(self, linea):
        """Agrega una línea al código traducido respetando la indentación."""
        indentacion = "    " * self.nivel_indentacion
        self.codigo.append(indentacion + linea)

    def enterPrograma(self, ctx):
        pass

    def exitPrograma(self, ctx):
        # Al final, imprimimos o guardamos el código traducido.
        print("\n".join(self.codigo))

    def enterBloque(self, ctx):
        self.nivel_indentacion += 1  # Incrementamos la indentación al entrar a un bloque.

    def exitBloque(self, ctx):
        if self.nivel_indentacion > 0:
            self.nivel_indentacion -= 1


    def exitMostrar(self, ctx):
        mensaje = ctx.expresion().getText()
        print(f"Traduciendo 'mostrar': {mensaje}")  # Mensaje de depuración
        self.agregar_linea(f"print({mensaje})")


    def exitEntrada(self, ctx):
        variable = ctx.ID().getText()
        self.agregar_linea(f"{variable} = input()")

    def exitAsignacion(self, ctx):
        variable = ctx.ID().getText()
        valor = ctx.expresion().getText()
        self.agregar_linea(f"{variable} = {valor}")

    def exitFuncionDefinicion(self, ctx):
        nombre_funcion = ctx.ID().getText()
        parametros = ctx.parametros().getText() if ctx.parametros() else ""
        self.agregar_linea(f"def {nombre_funcion}({parametros}):")

    def enterCondicional(self, ctx: TraductorParser.CondicionalContext):
        condicion = ctx.expresion().getText()
        condicion = self.transformar_expresion(condicion)  # Transformar valores y operadores
        self.agregar_linea(f"if {condicion}:")  # Generamos el `if` con la condición.
        self.nivel_indentacion += 1
    def transformar_expresion(self, expresion):
            """Transforma expresiones para reemplazar valores y operadores específicos."""
            reemplazos = {
                r'\bverdadero\b': 'True',
                r'\bfalso\b': 'False',
            }
            # Aplicamos cada reemplazo usando expresiones regulares
            for patron, reemplazo in reemplazos.items():
                expresion = re.sub(patron, reemplazo, expresion)
            # Limpiamos espacios extra en caso de reemplazos adyacentes
            expresion = re.sub(r'\s+', ' ', expresion).strip()
            return expresion
    def exitCondicional(self, ctx: TraductorParser.CondicionalContext):
        self.nivel_indentacion -= 1
        if len(ctx.bloque()) > 1:
            self.agregar_linea("else:")
            self.nivel_indentacion += 1
            self.nivel_indentacion -= 1

    def enterBucle(self, ctx):
        if ctx.getText().startswith("mientras"):
            condicion = ctx.expresion().getText()
            self.agregar_linea(f"while {condicion}:")
            self.nivel_indentacion += 1  # Incrementa la indentación
        elif ctx.getText().startswith("repetir"):
            veces = ctx.expresion().getText()
            self.agregar_linea(f"for i in range({veces}):")
            self.nivel_indentacion += 1  # Incrementa la indentación

    def exitBucle(self, ctx):
        self.nivel_indentacion -= 1  # Reduce la indentación al salir del bucle


    def exitBucle(self, ctx):
        self.nivel_indentacion -= 1  # Reduce la indentación al salir del bucle.
        


    def enterFuncionDefinicion(self, ctx):
        nombre_funcion = ctx.ID().getText()
        parametros = ctx.parametros().getText() if ctx.parametros() else ""
        self.agregar_linea(f"def {nombre_funcion}({parametros}):")
        self.nivel_indentacion += 1  # Aumentamos el nivel de indentación para el cuerpo.


    def exitFuncionDefinicion(self, ctx):
        self.nivel_indentacion -= 1  # Reducimos la indentación al salir del bloque de la función.

    def exitRetorno(self, ctx):
        """Generar código para una instrucción de retorno."""
        valor = ctx.expresion().getText()
        self.agregar_linea(f"return {valor}")

    def exitLlamadaFuncion(self, ctx):
        """Generar código para una llamada a función."""
        # Extraer el nombre de la función
        nombre = ctx.ID().getText()

        # Verificar si hay argumentos
        argumentos = ""
        if ctx.argumentos():
            # Obtener los nodos de los argumentos y generar la lista
            argumentos = ", ".join([arg.getText() for arg in ctx.argumentos().expresion()])

        # Verificar si la llamada está dentro de una asignación
        if isinstance(ctx.parentCtx, TraductorParser.AsignacionContext):
            # Caso: La llamada está asignada a una variable
            variable = ctx.parentCtx.ID().getText()  # Nombre de la variable (ej., resultado)
            # Generar solo la asignación, no la llamada adicional
            self.agregar_linea(f"{variable} = {nombre}({argumentos})")
      