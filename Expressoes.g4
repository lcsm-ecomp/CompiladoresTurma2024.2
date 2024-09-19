grammar Expressoes;

// Analise Lexica

NUM : [0-9]+ ;
OP1 : '+' | '-' ; 
OP2 : '*' |  '/' ;
BRANCO : ( ' '  ) -> skip ;

// Analise Sintatica
prog : exp EOF ; 
exp : exp OP2 exp
    | exp OP1 exp
    | NUM
    ;
