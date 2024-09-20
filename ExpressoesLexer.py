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
        4,0,5,26,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        1,4,1,15,8,1,11,1,12,1,16,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,0,0,5,
        1,1,3,2,5,3,7,4,9,5,1,0,4,1,0,97,122,1,0,48,57,2,0,43,43,45,45,2,
        0,42,42,47,47,26,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,1,11,1,0,0,0,3,14,1,0,0,0,5,18,1,0,0,0,7,20,1,0,0,0,
        9,22,1,0,0,0,11,12,7,0,0,0,12,2,1,0,0,0,13,15,7,1,0,0,14,13,1,0,
        0,0,15,16,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,4,1,0,0,0,18,19,
        7,2,0,0,19,6,1,0,0,0,20,21,7,3,0,0,21,8,1,0,0,0,22,23,5,32,0,0,23,
        24,1,0,0,0,24,25,6,4,0,0,25,10,1,0,0,0,2,0,16,1,6,0,0
    ]

class ExpressoesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAR = 1
    NUM = 2
    OP1 = 3
    OP2 = 4
    BRANCO = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "VAR", "NUM", "OP1", "OP2", "BRANCO" ]

    ruleNames = [ "VAR", "NUM", "OP1", "OP2", "BRANCO" ]

    grammarFileName = "Expressoes.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


