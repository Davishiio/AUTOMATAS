"""Máquina de Estado Finito Determinista (AFD)"""

class MaquinaAFD:
    """
    Clase que define una Máquina de Estado Finito Determinista (AFD).

    Atributos:
    ----------
    CONJUNTO_ESTADOS_AUTOMATA : list
        Lista que contiene los estados del autómata.
    ALFABETO_AUTOMATA : list
        Lista que contiene el alfabeto de entrada del autómata.
    FUNCIONES_TRANSICION_AUTOMATA : dict
        Diccionario que define la función de transición (estado actual × símbolo → estado siguiente).
    ESTADO_INICIAL_AUTOMATA : str
        Estado inicial del autómata.
    ESTADO_ACEPTACION_AUTOMATA : list
        Lista de estados de aceptación del autómata.
    ESTADO_ACTUAL_AUTOMATA : str
        Estado actual durante la ejecución del autómata.
    """

    def __init__(self):
        """Inicialización de la máquina AFD. Se definen los estados, el alfabeto, la función de transición,
        el estado inicial, los estados de aceptación y el estado actual."""
        self.CONJUNTO_ESTADOS_AUTOMATA = self.definir_estados()  # Definir los estados del autómata
        self.ALFABETO_AUTOMATA = self.definir_alfabeto()  # Definir el alfabeto del autómata
        self.FUNCIONES_TRANSICION_AUTOMATA = self.definir_funcion_Transicion()  # Definir la función de transición
        self.ESTADO_INICIAL_AUTOMATA, self.ESTADO_ACEPTACION_AUTOMATA = self.set_start_accept()  # Establecer estado inicial y de aceptación
        self.ESTADO_ACTUAL_AUTOMATA = None  # Inicializar el estado actual como vacío

    def set_start_accept(self):
        """
        Pide al usuario el estado inicial y los estados de aceptación, validando que estos pertenezcan al conjunto de estados.

        Returns:
        --------
        estado_inicial_ingresado : str
            Estado inicial validado.
        estado_aceptacion_ingresado : list
            Lista de estados de aceptación validados.
        """
        while True:
            estado_inicial_ingresado = input("Ingresa el Estado Inicial: ")
            estado_aceptacion_ingresado = input("Ingresa el Estado de Aceptación: ").split()
            # Verificar que el estado inicial y de aceptación estén dentro del conjunto de estados
            if (estado_inicial_ingresado in self.CONJUNTO_ESTADOS_AUTOMATA) and (set(estado_aceptacion_ingresado).issubset(set(self.CONJUNTO_ESTADOS_AUTOMATA))):
                return estado_inicial_ingresado, estado_aceptacion_ingresado
            else:
                print(
                    "Por favor, ingresa el ESTADO_INICIAL y los ESTADOS_DE_ACEPTACIÓN que están en el Conjunto de estados: {}.".format(
                        self.CONJUNTO_ESTADOS_AUTOMATA))

    def definir_estados(self):
        """
        Pide al usuario que ingrese el conjunto de estados del autómata.

        Returns:
        --------
        conjunto_estados_ingresados : list
            Lista de estados ingresados.
        """
        conjunto_estados_ingresados = input("Ingresa el conjunto de estados separado por espacios: ").split()
        print("Conjunto de estados : {}".format(conjunto_estados_ingresados))
        return conjunto_estados_ingresados

    def definir_alfabeto(self):
        """
        Pide al usuario que ingrese el alfabeto del autómata.

        Returns:
        --------
        alfabeto_ingresado : list
            Lista del alfabeto ingresado.
        """
        alfabeto_ingresado = input("Ingresa el alfabeto separado por espacios: ").split()
        print("Alfabeto : {}".format(alfabeto_ingresado))
        return alfabeto_ingresado

    def definir_funcion_Transicion(self):
        """
        Crea la función de transición del autómata basándose en los estados y símbolos del alfabeto.
        El usuario ingresa las transiciones manualmente.

        Returns:
        --------
        funciones_transicion : dict
            Diccionario que contiene la función de transición del autómata.
        """
        funciones_transicion = {}

        # Crear un diccionario de transiciones vacío para cada estado
        for estado in self.CONJUNTO_ESTADOS_AUTOMATA:
            diccionario_simbolos = {}
            for simbolo in self.ALFABETO_AUTOMATA:
                diccionario_simbolos[simbolo] = "NM"  # Asignar transiciones no definidas por defecto (NM)
            funciones_transicion[estado] = diccionario_simbolos

        # Solicitar al usuario definir las transiciones para cada estado y símbolo
        for key, dic_val in funciones_transicion.items():
            print("Ingresa los estados de transicion para el estado {}. Si no está definido, usa 'NM'.".format(key))
            for simbolo in dic_val:
                funciones_transicion[key][simbolo] = input("Estado actual: {}\tSimbolo de entrada:{}\tEstado siguiente:".format(key, simbolo))

        # Mostrar las transiciones definidas
        print("Función de transición EstadoActual × SimboloEntrada → EstadoSiguiente")
        print("ESTADO ACTUAL \tALFABETO DE ENTRADA\tESTADO SIGUIENTE")
        for key, dic_val in funciones_transicion.items():
            for simbolo, movimiento in dic_val.items():
                print("\t{}\t\t:{}\t{}".format(key, simbolo, movimiento))

        return funciones_transicion

    def val_state_alphabet(self, simbolo):
        """
        Transición del estado actual basado en el símbolo de entrada.

        Parameters:
        -----------
        simbolo : str
            Símbolo de entrada.

        Returns:
        --------
        None
        """
        self.ESTADO_ACTUAL_AUTOMATA = self.FUNCIONES_TRANSICION_AUTOMATA[self.ESTADO_ACTUAL_AUTOMATA][simbolo]

    def val_final_state(self):
        """
        Verifica si el estado actual es uno de los estados de aceptación.

        Returns:
        --------
        bool
            True si el estado actual es un estado de aceptación, False de lo contrario.
        """
        return self.ESTADO_ACTUAL_AUTOMATA in self.ESTADO_ACEPTACION_AUTOMATA

    def run_automata(self, cadena):
        """
        Valida una cadena de entrada contra el autómata.

        Parameters:
        -----------
        cadena : list
            Lista de símbolos que representan la cadena de entrada.

        Returns:
        --------
        bool
            True si la cadena es aceptada por el autómata, False de lo contrario.
        """
        self.ESTADO_ACTUAL_AUTOMATA = self.ESTADO_INICIAL_AUTOMATA
        for simbolo in cadena:
            self.val_state_alphabet(simbolo)
            if self.ESTADO_ACTUAL_AUTOMATA == 'NM':  # Si no hay transición definida, la cadena es rechazada
                return False
        return self.val_final_state()


if __name__ == "__main__":
    def leerArchivo():
        """
        Lee las quíntuplas de un autómata desde un archivo 'automata.csv' y procesa la información.
        """
        archivo = open("automata.csv")
        lista_sin_formato = archivo.readlines()
        archivo.close()

        estado_inicial = ""
        estado_final = ""
        funciones_transicion = {}

        # Procesar líneas del archivo
        lista = []
        for linea in lista_sin_formato:
            if "+" in linea and "*" not in linea[1]:
                estado_inicial = linea[1:linea.find(",")]
            elif "+*" in linea or "*+" in linea:
                estado_inicial = linea[2:linea.find(",")]
                estado_final = linea[2:linea.find(",")]
            elif "*" in linea and "+" not in linea[1]:
                estado_final = linea[1:linea.find(",")]
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

        # Mostrar el autómata procesado
        print("estado inicial =" + estado_inicial)
        print("estado final =" + estado_final)
        print(f"alfabeto ={alfabeto}")
        print(f"conjunto de estados = {conjunto_de_estados}")
        print(f"funciones de transicion{funciones_transicion}")

        def verificar_cadena(cadena):
            """
            Verifica si una cadena es aceptada por el autómata cargado desde el archivo.
            """
            estado_actual = estado_inicial
            for simbolo in cadena:
                if simbolo in funciones_transicion[estado_actual]:
                    estado_actual = funciones_transicion[estado_actual][simbolo]
                else:
                    print(f"Símbolo '{simbolo}' no está en el alfabeto.")
                    return False

            return estado_actual == estado_final

        cadena = input("ingresa la cadena: ")
        if verificar_cadena(cadena):
            print("Cadena aceptada")
        else:
            print("Cadena rechazada")


    # Menú principal
    while True:
        print("Menú Principal")
        print("1.- Definir Automata")
        print("2.- Leer Automata desde Archivo")
        print("3.- Probar Automata")
        print("4.- Salir")

        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            automata = MaquinaAFD()  # Crear una instancia del AFD y definirlo manualmente
        elif opcion == 2:
            leerArchivo()  # Leer el autómata desde un archivo
        elif opcion == 3:
            cadena = input("Ingresa una cadena de entrada: ").split()
            if automata.run_automata(cadena):  # Verificar si la cadena es aceptada por el autómata
                print("Cadena aceptada.")
            else:
                print("Cadena rechazada.")
        elif opcion == 4:
            break
        else:
            print("Opción no válida, intenta de nuevo.")
