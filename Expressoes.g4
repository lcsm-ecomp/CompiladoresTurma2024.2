grammar Expressoes;

// Analise Lexica

VAR : [a-z] ;
NUM : [0-9]+ ;
OP1 : '+' | '-' ; 
OP2 : '*' |  '/' ;
BRANCO : ( ' '  ) -> skip ;

// Analise Sintatica
prog : exp EOF ; 
exp : exp op=OP2 exp
    | exp op=OP1 exp
    | NUM | VAR
    ;
