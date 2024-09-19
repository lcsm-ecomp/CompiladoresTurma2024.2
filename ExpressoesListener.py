# Generated from Expressoes.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpressoesParser import ExpressoesParser
else:
    from ExpressoesParser import ExpressoesParser

# This class defines a complete listener for a parse tree produced by ExpressoesParser.
class ExpressoesListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressoesParser#prog.
    def enterProg(self, ctx:ExpressoesParser.ProgContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#prog.
    def exitProg(self, ctx:ExpressoesParser.ProgContext):
        pass


    # Enter a parse tree produced by ExpressoesParser#exp.
    def enterExp(self, ctx:ExpressoesParser.ExpContext):
        pass

    # Exit a parse tree produced by ExpressoesParser#exp.
    def exitExp(self, ctx:ExpressoesParser.ExpContext):
        pass



del ExpressoesParser