grammar Expressoes;

// Analise Lexica

NUM : [0-9]+ ;
PRINT : 'print'; 
INT : 'int' ;
VAR : [a-z]+ ;
OP1 : '+' | '-' ; 
OP2 : '*' |  '/' ;
EQUAL : '=' ;
APAR : '(' ;
FPAR : ')' ;
PV : ';' ;
ENTER : '\n' -> skip ;
BRANCO : ( ' '  ) -> skip ;

// Analise Sintatica
prog : (com PV)+; 
exp : exp OP2 exp
    | exp OP1 exp
    | NUM | VAR
    | APAR exp FPAR
    ;
    
com : INT VAR
    | PRINT exp 
    | VAR EQUAL exp ;
