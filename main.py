import sys
from antlr4 import *
from ExpressoesLexer import ExpressoesLexer
from ExpressoesParser import ExpressoesParser

def imprimeExp(exp, indent):
    if exp.NUM():
        print(indent+"Constante " + exp.getText())
    elif exp.OP1():
        print(indent + "OP1 " + exp.OP1().getText())
        imprimeExp(exp.exp(0),indent+"|  ")
        imprimeExp(exp.exp(1),indent+"|  ")
    elif  exp.OP2():
        print(indent + "OP2 " + exp.OP2().getText())
        imprimeExp(exp.exp(0),indent+"|  ")    
        imprimeExp(exp.exp(1),indent+"|  ") 

def geraCodigoInfix(exp):
    if exp.NUM():
        return exp.getText()
    elif exp.op:
        return "("+geraCodigoInfix(exp.exp(0))+exp.op.text+geraCodigoInfix(exp.exp(1))+")"

opName = {
    '+' : 'sum',
    '-' : 'diff',
    '*' : 'mult',
    '/' : 'div'
}
def geraCodigoprefix(exp):
    if exp.NUM():
        return exp.getText()
    elif exp.op:
        return opName[exp.op.text]+"("+geraCodigoprefix(exp.exp(0))+","+geraCodigoprefix(exp.exp(1))+")"
    elif exp.VAR():
        return exp.VAR().getText()

vars = {
    'x' : 2,
    'y' : 4
}
def executeCom(com):
    if com.PRINT():
        print(avalieExp(com.exp()))
    elif com.VAR():
        nomeVar = com.VAR().getText()
        valor = avalieExp(com.exp())
        vars[nomeVar] = valor
    elif com.ACHAVE():
        for c in com.com():
            executeCom(c)
    elif com.IF():
        valor = avalieExp(com.exp())
        if valor==True or valor!=0:
            executeCom(com.com(0))
        else:
            executeCom(com.com(1))
    else:
        raise Exception("Nao sei executar o comando" + com.toStringTree(recog=parser))

def avalieExp(exp):
    if exp.NUM():
        return int(exp.getText())
    elif exp.op:
        v1 = avalieExp(exp.exp(0))
        v2 = avalieExp(exp.exp(1))
        op = exp.getChild(1).getText()
        if op=='+':
            return v1+v2
        elif op=='-':
            return v1-v2
        elif op=='*':
            return v1*v2
        elif op=='/':
            return v1/v2
        elif op=='==':
            return v1==v2
        elif op=='!=':
            return v1!=v2
        elif op=='>':
            return v1>v2
        elif op=='<':
            return v1<v2
        else:
            return None
    elif exp.VAR():
        nome = exp.VAR().getText()
        if nome in vars.keys():
           return vars[nome]
        else:
           raise Exception('variavel ' + nome + ' não declarada')
    elif exp.APAR():
        return avalieExp(exp.exp(0))
    else:
        raise Exception("Nao sei avaliar expressao" + exp.toStringTree(recog=parser))
def imprime(no, indent):
    print(indent + no.getText())
    for pos in range(no.getChildCount()):
        imprime(no.getChild(pos), indent + "+-- ")

incrIndent = "    "
def embelezeCom(com,indent=" "):
    if com.PRINT():
        print(indent , "print exp ;")
    elif com.VAR():
        nomeVar = com.VAR().getText()
        print(indent,nomeVar, " = exp ;")
    elif com.ACHAVE():
        print(indent,"{")
        for c in com.com():
            embelezeCom(c,indent+incrIndent)
        print(indent,"}")
    elif com.IF():
        print(indent, "if (exp)")
        embelezeCom(com.com(0),indent+incrIndent)
        print(indent,"else")
        embelezeCom(com.com(1),indent+incrIndent)

    else:
        raise Exception("Nao sei executar o comando" + com.toStringTree(recog=parser))




#input_stream = FileStream(sys.argv[1])
input_stream = InputStream(
    """{x = 2 ; print(x);if (x > 1)print 1; else
       print 0; x = x * 5 ; print(x>0); print(x);} 
    """)
lexer = ExpressoesLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExpressoesParser(stream)
tree = parser.prog()
if parser.getNumberOfSyntaxErrors()>0:
    print("erro sintático")
    sys.exit(1)

print("ok")
com=tree.com()
#print(com.toStringTree(recog=parser))
#print('valor = ', executeCom(com))
embelezeCom(com)