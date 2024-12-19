#Auto: David Josue Chab Angulo
class MaquinaAFD:
    """
    Clase que define una Máquina de Estado Finito Determinista (AFD).
    """
    def __init__(self, estado_inicial, estados_finales, alfabeto, conjunto_estados, funciones_transicion):
        self.ESTADO_INICIAL_AUTOMATA = estado_inicial
        self.ESTADO_ACEPTACION_AUTOMATA = estados_finales
        self.ALFABETO_AUTOMATA = alfabeto
        self.CONJUNTO_ESTADOS_AUTOMATA = conjunto_estados
        self.FUNCIONES_TRANSICION_AUTOMATA = funciones_transicion
        self.ESTADO_ACTUAL_AUTOMATA = None

    def verificar_cadena(self, cadena):
        """
        Verifica si una cadena es aceptada por el autómata.

        Parameters:
        cadena (str): Cadena de entrada.

        Returns:
        bool: True si es aceptada, False si es rechazada.
        """
        self.ESTADO_ACTUAL_AUTOMATA = self.ESTADO_INICIAL_AUTOMATA
        for simbolo in cadena:
            if simbolo in self.FUNCIONES_TRANSICION_AUTOMATA[self.ESTADO_ACTUAL_AUTOMATA]:
                self.ESTADO_ACTUAL_AUTOMATA = self.FUNCIONES_TRANSICION_AUTOMATA[self.ESTADO_ACTUAL_AUTOMATA][simbolo]
            else:
                print(f"Símbolo '{simbolo}' no está en el alfabeto.")
                return False
        return self.ESTADO_ACTUAL_AUTOMATA in self.ESTADO_ACEPTACION_AUTOMATA


def leerArchivo():
    """
    Lee las quíntuplas de un autómata desde un archivo 'automata.csv' y procesa la información.

    Returns:
    MaquinaAFD: Instancia del AFD.
    """
    archivo = open("automata.csv")
    lista_sin_formato = archivo.readlines()
    archivo.close()

    estado_inicial = ""
    estados_finales = set()
    funciones_transicion = {}

    # Procesar líneas del archivo
    lista = []
    for linea in lista_sin_formato:
        if "+" in linea and "*" not in linea[1]:
            estado_inicial = linea[1:linea.find(",")]
        elif "+*" in linea or "*+" in linea:
            estado_inicial = linea[2:linea.find(",")]
            estados_finales.add(linea[2:linea.find(",")])
        elif "*" in linea and "+" not in linea[1]:
            estados_finales.add(linea[1:linea.find(",")])
        lista.append(linea.strip().replace("+", "").replace("*", "").split(","))

    alfabeto = lista[0]

    conjunto_de_estados = set()
    for cadena in lista[1:]:
        for caracter in cadena:
            conjunto_de_estados.add(caracter)

    conjunto_de_estados = list(conjunto_de_estados)
    conjunto_de_estados.sort()

    for cadena in lista[1:]:
        llave = cadena[0]
        funciones_transicion[llave] = {}
        for letra, estado in zip(alfabeto, cadena[1:]):
            funciones_transicion[llave][letra] = estado

    # Crear instancia de la máquina AFD
    return MaquinaAFD(estado_inicial, list(estados_finales), alfabeto, conjunto_de_estados, funciones_transicion)


if __name__ == "__main__":
    automata = leerArchivo()  # Leer el autómata desde el archivo
    print("Autómata cargado exitosamente.")
    print("Ingresa cadenas para validarlas o escribe 'salir' para terminar.\n")

    while True:
        cadena = input("Ingresa la cadena: ")
        if cadena.lower() == 'salir':
            print("Saliendo del programa.")
            break
        elif automata.verificar_cadena(cadena):
            print("Cadena aceptada.")
        else:
            print("Cadena rechazada.")
