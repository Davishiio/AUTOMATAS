from antlr4 import *
from traductorLexer import traductorLexer
from traductorParser import traductorParser
from convertidor import convertidor

def ejecutar_traduccion():
    archivo_entrada = "operacion.txt"

    # Abre y lee el archivo de entrada
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
        contenido = entrada.read()

    # Inicializa el lexer con el contenido del archivo de entrada
    lexer = traductorLexer(InputStream(contenido))
    flujo_tokens = CommonTokenStream(lexer)

    # Configura el parser utilizando el flujo de tokens
    parser = traductorParser(flujo_tokens)

    # Genera el árbol sintáctico a partir de la regla principal
    arbol_sintactico = parser.program()

    # Convierte el código utilizando el listener
    traductor = convertidor()
    recorrido = ParseTreeWalker()
    recorrido.walk(traductor, arbol_sintactico)

    # Escribe el código convertido en un archivo Java
    codigo_java = traductor.get_java_code()
    with open("operacion.java", "w") as archivo_salida:
        archivo_salida.write("public class operacion {\n")
        archivo_salida.write(codigo_java)
        archivo_salida.write("\n}")

if __name__ == '__main__':
    ejecutar_traduccion()
