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
        4,1,12,43,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,1,1,1,1,1,1,1,1,1,
        1,1,5,1,29,8,1,10,1,12,1,32,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        41,8,2,1,2,0,1,2,3,0,2,4,0,0,46,0,9,1,0,0,0,2,20,1,0,0,0,4,40,1,
        0,0,0,6,7,3,4,2,0,7,8,5,10,0,0,8,10,1,0,0,0,9,6,1,0,0,0,10,11,1,
        0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,14,6,1,-1,0,14,
        21,5,1,0,0,15,21,5,4,0,0,16,17,5,8,0,0,17,18,3,2,1,0,18,19,5,9,0,
        0,19,21,1,0,0,0,20,13,1,0,0,0,20,15,1,0,0,0,20,16,1,0,0,0,21,30,
        1,0,0,0,22,23,10,5,0,0,23,24,5,6,0,0,24,29,3,2,1,6,25,26,10,4,0,
        0,26,27,5,5,0,0,27,29,3,2,1,5,28,22,1,0,0,0,28,25,1,0,0,0,29,32,
        1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,3,1,0,0,0,32,30,1,0,0,0,33,
        34,5,3,0,0,34,41,5,4,0,0,35,36,5,2,0,0,36,41,3,2,1,0,37,38,5,4,0,
        0,38,39,5,7,0,0,39,41,3,2,1,0,40,33,1,0,0,0,40,35,1,0,0,0,40,37,
        1,0,0,0,41,5,1,0,0,0,5,11,20,28,30,40
    ]

class ExpressoesParser ( Parser ):

    grammarFileName = "Expressoes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'print'", "'int'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "'('", "')'", "';'", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "NUM", "PRINT", "INT", "VAR", "OP1", 
                      "OP2", "EQUAL", "APAR", "FPAR", "PV", "ENTER", "BRANCO" ]

    RULE_prog = 0
    RULE_exp = 1
    RULE_com = 2

    ruleNames =  [ "prog", "exp", "com" ]

    EOF = Token.EOF
    NUM=1
    PRINT=2
    INT=3
    VAR=4
    OP1=5
    OP2=6
    EQUAL=7
    APAR=8
    FPAR=9
    PV=10
    ENTER=11
    BRANCO=12

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

        def com(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressoesParser.ComContext)
            else:
                return self.getTypedRuleContext(ExpressoesParser.ComContext,i)


        def PV(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressoesParser.PV)
            else:
                return self.getToken(ExpressoesParser.PV, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.com()
                self.state = 7
                self.match(ExpressoesParser.PV)
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                    break

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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 14
                self.match(ExpressoesParser.NUM)
                pass
            elif token in [4]:
                self.state = 15
                self.match(ExpressoesParser.VAR)
                pass
            elif token in [8]:
                self.state = 16
                self.match(ExpressoesParser.APAR)
                self.state = 17
                self.exp(0)
                self.state = 18
                self.match(ExpressoesParser.FPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 28
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 22
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 23
                        self.match(ExpressoesParser.OP2)
                        self.state = 24
                        self.exp(6)
                        pass

                    elif la_ == 2:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 25
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 26
                        self.match(ExpressoesParser.OP1)
                        self.state = 27
                        self.exp(5)
                        pass

             
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExpressoesParser.INT, 0)

        def VAR(self):
            return self.getToken(ExpressoesParser.VAR, 0)

        def PRINT(self):
            return self.getToken(ExpressoesParser.PRINT, 0)

        def exp(self):
            return self.getTypedRuleContext(ExpressoesParser.ExpContext,0)


        def EQUAL(self):
            return self.getToken(ExpressoesParser.EQUAL, 0)

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
        self.enterRule(localctx, 4, self.RULE_com)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(ExpressoesParser.INT)
                self.state = 34
                self.match(ExpressoesParser.VAR)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(ExpressoesParser.PRINT)
                self.state = 36
                self.exp(0)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(ExpressoesParser.VAR)
                self.state = 38
                self.match(ExpressoesParser.EQUAL)
                self.state = 39
                self.exp(0)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




