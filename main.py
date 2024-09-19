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

def avalieExp(exp):
    if exp.NUM():
        return int(exp.getText())
    elif exp.OP1():
        v1 = avalieExp(exp.exp(0))
        v2 = avalieExp(exp.exp(1))
        op = exp.OP1().getText()
        if op=='+':
            return v1+v2
        else:
            return v1-v2
    elif exp.OP2():
        v1 = avalieExp(exp.exp(0))
        v2 = avalieExp(exp.exp(1))
        op = exp.OP2().getText()
        if op=='*':
            return v1*v2
        else:
            return v1/v2


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
else:
    print("erro sintático")
