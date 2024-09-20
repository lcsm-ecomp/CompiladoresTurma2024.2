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
    'x' : 3,
    'y' : 4
}
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
        else:
            return v1/v2
    elif exp.VAR():
        nome = exp.VAR().getText()
        if nome in vars.keys():
           return vars[nome]
        else:
           raise Exception('variavel ' + nome + ' não declarada')


def imprime(no, indent):
    print(indent + no.getText())
    for pos in range(no.getChildCount()):
        imprime(no.getChild(pos), indent + "+-- ")

input_stream = FileStream(sys.argv[1])
lexer = ExpressoesLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExpressoesParser(stream)
tree = parser.prog()
if parser.getNumberOfSyntaxErrors()==0:
    print("ok")
    print(tree.toStringTree(recog=parser))
    exp=tree.exp()
else:
    print("erro sintático")
