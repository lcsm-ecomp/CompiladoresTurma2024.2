import sys
from antlr4 import *
from ExpressoesLexer import ExpressoesLexer
from ExpressoesParser import ExpressoesParser

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
