# Generated from Expressoes.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,22,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,11,8,0,11,
        0,12,0,12,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,0,0,4,1,1,3,2,5,3,7,4,
        1,0,3,1,0,48,57,2,0,43,43,45,45,2,0,42,42,47,47,22,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,1,10,1,0,0,0,3,14,1,0,0,0,5,16,
        1,0,0,0,7,18,1,0,0,0,9,11,7,0,0,0,10,9,1,0,0,0,11,12,1,0,0,0,12,
        10,1,0,0,0,12,13,1,0,0,0,13,2,1,0,0,0,14,15,7,1,0,0,15,4,1,0,0,0,
        16,17,7,2,0,0,17,6,1,0,0,0,18,19,5,32,0,0,19,20,1,0,0,0,20,21,6,
        3,0,0,21,8,1,0,0,0,2,0,12,1,6,0,0
    ]

class ExpressoesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    OP1 = 2
    OP2 = 3
    BRANCO = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NUM", "OP1", "OP2", "BRANCO" ]

    ruleNames = [ "NUM", "OP1", "OP2", "BRANCO" ]

    grammarFileName = "Expressoes.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


