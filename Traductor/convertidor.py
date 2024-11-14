
from traductorParser import traductorParser
from traductorListener import traductorListener


class convertidor(traductorListener):
    def __init__(self):
        super().__init__()
        self.java_code = []
        self.function_name = ""
        self.arguments = ""

    def enterFunctionDef(self, ctx: traductorParser.FunctionDefContext):
        self.function_name = ctx.IDENTIFIER().getText()
        # Convertir parámetros a int en Java
        parameters = ctx.parameters().getText()
        java_parameters = ', '.join([f"int {param.strip()}" for param in parameters.split(',')])
        self.java_code.append(f"public static int {self.function_name}({java_parameters}) " + "{")

    def exitFunctionDef(self, ctx: traductorParser.FunctionDefContext):
        self.java_code.append("}")

    def enterExpressionStatement(self, ctx: traductorParser.ExpressionStatementContext):
        variable_name = ctx.IDENTIFIER().getText()
        expression = ctx.expression().getText()
        self.java_code.append(f"    int {variable_name} = {expression};")

    def enterReturnStatement(self, ctx: traductorParser.ReturnStatementContext):
        expression = ctx.expression().getText()
        self.java_code.append(f"    return {expression};")

    def enterPrintStatement(self, ctx: traductorParser.PrintStatementContext):
        # Convierte la llamada a print en Python a System.out.println en Java
        self.arguments = ctx.arguments().getText()

    def get_java_code(self):
        # Añade el método main para ejecutar la función
        main_code = [
            "public static void main(String[] args) {",
            f"    System.out.println({self.function_name}({self.arguments}));",
            "}"
        ]
        return "\n".join(self.java_code + main_code)


