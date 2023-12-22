// Calculator.g4
grammar Calculator;

// Parser Rules
expression : additiveExpression;

additiveExpression
    : multiplicativeExpression (('+' | '-') multiplicativeExpression)*
    ;

multiplicativeExpression
    : powerExpression (('*' | '/') powerExpression)*
    ;

powerExpression
    : primaryExpression ('^' primaryExpression)?
    ;

primaryExpression
    : '(' expression ')'
    | NUMBER
    ;

// Lexer Rules
NUMBER : DIGIT+ ('.' DIGIT+)?;

fragment DIGIT : '0'..'9';

WS : [ \t\r\n]+ -> skip;
