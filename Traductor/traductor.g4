grammar traductor;

// Lexer rules
DEF       : 'def' ;
RETURN    : 'return' ;
PRINT     : 'print' ;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER    : [0-9]+ ;
PLUS      : '+' ;
MINUS     : '-' ;
MULTIPLY  : '*' ;
DIVIDE    : '/' ;
LPAREN    : '(' ;
RPAREN    : ')' ;
COMMA     : ',' ;
COLON     : ':' ;
NEWLINE   : '\r'? '\n' ; // Manejo de salto de línea
WS        : [ \t]+ -> skip ; // Ignora espacios y tabulaciones fuera de los tokens importantes

// Parser reglas
program        : functionDef printStatement ;
functionDef    : DEF IDENTIFIER LPAREN parameters RPAREN COLON NEWLINE statement+ ;
parameters     : IDENTIFIER (COMMA IDENTIFIER)* | ;
statement      : expressionStatement | returnStatement ;
expressionStatement : INDENT? IDENTIFIER '=' expression NEWLINE ;
returnStatement : INDENT? RETURN expression NEWLINE ;
printStatement : PRINT LPAREN IDENTIFIER LPAREN arguments RPAREN RPAREN NEWLINE ;
expression     : term ((PLUS | MINUS) term)* ;
term           : factor ((MULTIPLY | DIVIDE) factor)* ;
factor         : NUMBER | IDENTIFIER | LPAREN expression RPAREN ;
arguments      : expression (COMMA expression)* | ; 