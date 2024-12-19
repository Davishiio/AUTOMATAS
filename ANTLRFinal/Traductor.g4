grammar Traductor;

// REGLA PRINCIPAL
programa : (instruccion | funcionDefinicion)* EOF ;

// INSTRUCCIONES
instruccion
    : asignacion ';'
    | condicional
    | bucle
    | mostrar ';'
    | entrada ';'
    | llamadaFuncion ';'
    ;

// DECLARACIÓN DE FUNCIONES
funcionDefinicion
    : 'función' ID '(' parametros? ')' bloque
    ;

parametros
    : ID (',' ID)*
    ;

// BLOQUES
bloque
    : '{' (instruccion | retorno)* '}'
    ;

retorno
    : 'retornar' expresion ';'
    ;

// ASIGNACIONES
asignacion
    : ID '=' expresion
    ;


// CONDICIONALES
condicional
    : 'si' expresion 'entonces' bloque ('sino' bloque)?
    ;

// BUCLES
bucle
    : 'mientras' expresion 'hacer' bloque
    | 'repetir' expresion 'veces' bloque
    ;

// ENTRADA Y SALIDA
mostrar
    : 'mostrar' expresion
    ;

entrada
    : ID '=' 'pregunta'
    ;

// LLAMADA A FUNCIONES
llamadaFuncion
    : ID '(' argumentos? ')'
    ;

argumentos
    : expresion (',' expresion)*
    ;

// EXPRESIONES
expresion
    : expresion operador=('*' | '/' | '+' | '-') expresion   
    | expresion operador=('==' | '!=' | '<' | '>' | '<=' | '>=') expresion  
    | expresion operador=('y' | 'o') expresion              
    | '(' expresion ')'
    | '-' expresion
    | 'no' expresion
    | ID
    | NUMERO
    | CADENA
    | 'verdadero' | 'falso'
    | llamadaFuncion // Aquí se permite que la llamada de función sea una expresión
    ;

// TIPOS DE DATOS
NUMERO : [0-9]+ ('.' [0-9]+)? ;
CADENA : '"' .*? '"' ;
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;

// OPERADORES
WS     : [ \t\r\n]+ -> skip ;
COMENTARIO : '//' ~[\r\n]* -> skip ;
