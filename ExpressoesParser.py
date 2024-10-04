# Generated from Expressoes.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,60,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,44,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,55,8,2,10,2,12,
        2,58,9,2,1,2,0,1,4,3,0,2,4,0,0,65,0,6,1,0,0,0,2,34,1,0,0,0,4,43,
        1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,5,1,0,0,10,11,3,
        4,2,0,11,12,5,4,0,0,12,35,1,0,0,0,13,14,5,5,0,0,14,15,5,7,0,0,15,
        16,3,4,2,0,16,17,5,4,0,0,17,35,1,0,0,0,18,22,5,13,0,0,19,21,3,2,
        1,0,20,19,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,25,
        1,0,0,0,24,22,1,0,0,0,25,35,5,14,0,0,26,27,5,2,0,0,27,28,5,11,0,
        0,28,29,3,4,2,0,29,30,5,12,0,0,30,31,3,2,1,0,31,32,5,3,0,0,32,33,
        3,2,1,0,33,35,1,0,0,0,34,9,1,0,0,0,34,13,1,0,0,0,34,18,1,0,0,0,34,
        26,1,0,0,0,35,3,1,0,0,0,36,37,6,2,-1,0,37,44,5,6,0,0,38,44,5,5,0,
        0,39,40,5,11,0,0,40,41,3,4,2,0,41,42,5,12,0,0,42,44,1,0,0,0,43,36,
        1,0,0,0,43,38,1,0,0,0,43,39,1,0,0,0,44,56,1,0,0,0,45,46,10,6,0,0,
        46,47,5,10,0,0,47,55,3,4,2,7,48,49,10,5,0,0,49,50,5,9,0,0,50,55,
        3,4,2,6,51,52,10,4,0,0,52,53,5,8,0,0,53,55,3,4,2,5,54,45,1,0,0,0,
        54,48,1,0,0,0,54,51,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,
        0,0,0,57,5,1,0,0,0,58,56,1,0,0,0,5,22,34,43,54,56
    ]

class ExpressoesParser ( Parser ):

    grammarFileName = "Expressoes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'if'", "'else'", "';'", "<INVALID>", 
                     "<INVALID>", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "IF", "ELSE", "PV", "VAR", "NUM", 
                      "EQ", "OP1", "OP2", "OP3", "APAR", "FPAR", "ACHAVE", 
                      "FCHAVE", "BRANCO" ]

    RULE_prog = 0
    RULE_com = 1
    RULE_exp = 2

    ruleNames =  [ "prog", "com", "exp" ]

    EOF = Token.EOF
    PRINT=1
    IF=2
    ELSE=3
    PV=4
    VAR=5
    NUM=6
    EQ=7
    OP1=8
    OP2=9
    OP3=10
    APAR=11
    FPAR=12
    ACHAVE=13
    FCHAVE=14
    BRANCO=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def com(self):
            return self.getTypedRuleContext(ExpressoesParser.ComContext,0)


        def EOF(self):
            return self.getToken(ExpressoesParser.EOF, 0)

        def getRuleIndex(self):
            return ExpressoesParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExpressoesParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.com()
            self.state = 7
            self.match(ExpressoesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ExpressoesParser.PRINT, 0)

        def exp(self):
            return self.getTypedRuleContext(ExpressoesParser.ExpContext,0)


        def PV(self):
            return self.getToken(ExpressoesParser.PV, 0)

        def VAR(self):
            return self.getToken(ExpressoesParser.VAR, 0)

        def EQ(self):
            return self.getToken(ExpressoesParser.EQ, 0)

        def ACHAVE(self):
            return self.getToken(ExpressoesParser.ACHAVE, 0)

        def FCHAVE(self):
            return self.getToken(ExpressoesParser.FCHAVE, 0)

        def com(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressoesParser.ComContext)
            else:
                return self.getTypedRuleContext(ExpressoesParser.ComContext,i)


        def IF(self):
            return self.getToken(ExpressoesParser.IF, 0)

        def APAR(self):
            return self.getToken(ExpressoesParser.APAR, 0)

        def FPAR(self):
            return self.getToken(ExpressoesParser.FPAR, 0)

        def ELSE(self):
            return self.getToken(ExpressoesParser.ELSE, 0)

        def getRuleIndex(self):
            return ExpressoesParser.RULE_com

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCom" ):
                listener.enterCom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCom" ):
                listener.exitCom(self)




    def com(self):

        localctx = ExpressoesParser.ComContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_com)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 9
                self.match(ExpressoesParser.PRINT)
                self.state = 10
                self.exp(0)
                self.state = 11
                self.match(ExpressoesParser.PV)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(ExpressoesParser.VAR)
                self.state = 14
                self.match(ExpressoesParser.EQ)
                self.state = 15
                self.exp(0)
                self.state = 16
                self.match(ExpressoesParser.PV)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(ExpressoesParser.ACHAVE)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8230) != 0):
                    self.state = 19
                    self.com()
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 25
                self.match(ExpressoesParser.FCHAVE)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(ExpressoesParser.IF)
                self.state = 27
                self.match(ExpressoesParser.APAR)
                self.state = 28
                self.exp(0)
                self.state = 29
                self.match(ExpressoesParser.FPAR)
                self.state = 30
                self.com()
                self.state = 31
                self.match(ExpressoesParser.ELSE)
                self.state = 32
                self.com()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def NUM(self):
            return self.getToken(ExpressoesParser.NUM, 0)

        def VAR(self):
            return self.getToken(ExpressoesParser.VAR, 0)

        def APAR(self):
            return self.getToken(ExpressoesParser.APAR, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressoesParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpressoesParser.ExpContext,i)


        def FPAR(self):
            return self.getToken(ExpressoesParser.FPAR, 0)

        def OP3(self):
            return self.getToken(ExpressoesParser.OP3, 0)

        def OP2(self):
            return self.getToken(ExpressoesParser.OP2, 0)

        def OP1(self):
            return self.getToken(ExpressoesParser.OP1, 0)

        def getRuleIndex(self):
            return ExpressoesParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpressoesParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 37
                self.match(ExpressoesParser.NUM)
                pass
            elif token in [5]:
                self.state = 38
                self.match(ExpressoesParser.VAR)
                pass
            elif token in [11]:
                self.state = 39
                self.match(ExpressoesParser.APAR)
                self.state = 40
                self.exp(0)
                self.state = 41
                self.match(ExpressoesParser.FPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 45
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 46
                        localctx.op = self.match(ExpressoesParser.OP3)
                        self.state = 47
                        self.exp(7)
                        pass

                    elif la_ == 2:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 48
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 49
                        localctx.op = self.match(ExpressoesParser.OP2)
                        self.state = 50
                        self.exp(6)
                        pass

                    elif la_ == 3:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 51
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 52
                        localctx.op = self.match(ExpressoesParser.OP1)
                        self.state = 53
                        self.exp(5)
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




