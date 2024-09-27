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
        4,0,13,67,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,39,8,3,11,3,12,3,40,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,50,8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,0,0,13,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,1,0,6,1,0,97,
        122,1,0,48,57,2,0,60,60,62,62,2,0,43,43,45,45,2,0,42,42,47,47,2,
        0,10,10,32,32,69,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,
        0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,
        3,33,1,0,0,0,5,35,1,0,0,0,7,38,1,0,0,0,9,42,1,0,0,0,11,49,1,0,0,
        0,13,51,1,0,0,0,15,53,1,0,0,0,17,55,1,0,0,0,19,57,1,0,0,0,21,59,
        1,0,0,0,23,61,1,0,0,0,25,63,1,0,0,0,27,28,5,112,0,0,28,29,5,114,
        0,0,29,30,5,105,0,0,30,31,5,110,0,0,31,32,5,116,0,0,32,2,1,0,0,0,
        33,34,5,59,0,0,34,4,1,0,0,0,35,36,7,0,0,0,36,6,1,0,0,0,37,39,7,1,
        0,0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,8,
        1,0,0,0,42,43,5,61,0,0,43,10,1,0,0,0,44,45,5,61,0,0,45,50,5,61,0,
        0,46,47,5,33,0,0,47,50,5,61,0,0,48,50,7,2,0,0,49,44,1,0,0,0,49,46,
        1,0,0,0,49,48,1,0,0,0,50,12,1,0,0,0,51,52,7,3,0,0,52,14,1,0,0,0,
        53,54,7,4,0,0,54,16,1,0,0,0,55,56,5,40,0,0,56,18,1,0,0,0,57,58,5,
        41,0,0,58,20,1,0,0,0,59,60,5,123,0,0,60,22,1,0,0,0,61,62,5,125,0,
        0,62,24,1,0,0,0,63,64,7,5,0,0,64,65,1,0,0,0,65,66,6,12,0,0,66,26,
        1,0,0,0,3,0,40,49,1,6,0,0
    ]

class ExpressoesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINT = 1
    PV = 2
    VAR = 3
    NUM = 4
    EQ = 5
    OP1 = 6
    OP2 = 7
    OP3 = 8
    APAR = 9
    FPAR = 10
    ACHAVE = 11
    FCHAVE = 12
    BRANCO = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "';'", "'='", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "PV", "VAR", "NUM", "EQ", "OP1", "OP2", "OP3", "APAR", 
            "FPAR", "ACHAVE", "FCHAVE", "BRANCO" ]

    ruleNames = [ "PRINT", "PV", "VAR", "NUM", "EQ", "OP1", "OP2", "OP3", 
                  "APAR", "FPAR", "ACHAVE", "FCHAVE", "BRANCO" ]

    grammarFileName = "Expressoes.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


