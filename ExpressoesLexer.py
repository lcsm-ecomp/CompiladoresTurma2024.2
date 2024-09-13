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
        4,0,12,65,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,27,8,0,
        11,0,12,0,28,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,4,3,42,
        8,3,11,3,12,3,43,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,
        1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,
        5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,1,0,4,1,0,48,57,1,0,97,122,
        2,0,43,43,45,45,2,0,42,42,47,47,66,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,26,1,0,
        0,0,3,30,1,0,0,0,5,36,1,0,0,0,7,41,1,0,0,0,9,45,1,0,0,0,11,47,1,
        0,0,0,13,49,1,0,0,0,15,51,1,0,0,0,17,53,1,0,0,0,19,55,1,0,0,0,21,
        57,1,0,0,0,23,61,1,0,0,0,25,27,7,0,0,0,26,25,1,0,0,0,27,28,1,0,0,
        0,28,26,1,0,0,0,28,29,1,0,0,0,29,2,1,0,0,0,30,31,5,112,0,0,31,32,
        5,114,0,0,32,33,5,105,0,0,33,34,5,110,0,0,34,35,5,116,0,0,35,4,1,
        0,0,0,36,37,5,105,0,0,37,38,5,110,0,0,38,39,5,116,0,0,39,6,1,0,0,
        0,40,42,7,1,0,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,
        1,0,0,0,44,8,1,0,0,0,45,46,7,2,0,0,46,10,1,0,0,0,47,48,7,3,0,0,48,
        12,1,0,0,0,49,50,5,61,0,0,50,14,1,0,0,0,51,52,5,40,0,0,52,16,1,0,
        0,0,53,54,5,41,0,0,54,18,1,0,0,0,55,56,5,59,0,0,56,20,1,0,0,0,57,
        58,5,10,0,0,58,59,1,0,0,0,59,60,6,10,0,0,60,22,1,0,0,0,61,62,5,32,
        0,0,62,63,1,0,0,0,63,64,6,11,0,0,64,24,1,0,0,0,3,0,28,43,1,6,0,0
    ]

class ExpressoesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    PRINT = 2
    INT = 3
    VAR = 4
    OP1 = 5
    OP2 = 6
    EQUAL = 7
    APAR = 8
    FPAR = 9
    PV = 10
    ENTER = 11
    BRANCO = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "'int'", "'='", "'('", "')'", "';'", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "PRINT", "INT", "VAR", "OP1", "OP2", "EQUAL", "APAR", 
            "FPAR", "PV", "ENTER", "BRANCO" ]

    ruleNames = [ "NUM", "PRINT", "INT", "VAR", "OP1", "OP2", "EQUAL", "APAR", 
                  "FPAR", "PV", "ENTER", "BRANCO" ]

    grammarFileName = "Expressoes.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


