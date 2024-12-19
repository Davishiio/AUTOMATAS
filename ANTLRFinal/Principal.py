from antlr4 import *
from TraductorLexer import TraductorLexer
from TraductorParser import TraductorParser
from InTraductorTostr import InTraductorTostr

def main():
    # Archivo de entrada y salida definidos
    archivo_entrada = "TXT.txt"
    archivo_salida = "Salida.py"

    try:
        # Leer el archivo de entrada
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            codigo_fuente = f.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no existe.")
        return

    # Crear el input stream
    input_stream = InputStream(codigo_fuente)

    # Instanciar lexer, parser y listener
    lexer = TraductorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TraductorParser(token_stream)
    tree = parser.programa()

    # Crear el listener personalizado
    listener = InTraductorTostr()

    # Recorrer el árbol sintáctico con el listener
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Guardar el código traducido en un archivo .py
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write("\n".join(listener.codigo))

    print(f"Código traducido guardado en '{archivo_salida}'.")

if __name__ == "__main__":
    main()
