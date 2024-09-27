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
        4,1,13,52,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,0,1,4,3,0,2,4,0,0,
        56,0,6,1,0,0,0,2,26,1,0,0,0,4,35,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,
        8,1,1,0,0,0,9,10,5,1,0,0,10,11,3,4,2,0,11,12,5,2,0,0,12,27,1,0,0,
        0,13,14,5,3,0,0,14,15,5,5,0,0,15,16,3,4,2,0,16,17,5,2,0,0,17,27,
        1,0,0,0,18,22,5,11,0,0,19,21,3,2,1,0,20,19,1,0,0,0,21,24,1,0,0,0,
        22,20,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,22,1,0,0,0,25,27,5,
        12,0,0,26,9,1,0,0,0,26,13,1,0,0,0,26,18,1,0,0,0,27,3,1,0,0,0,28,
        29,6,2,-1,0,29,36,5,4,0,0,30,36,5,3,0,0,31,32,5,9,0,0,32,33,3,4,
        2,0,33,34,5,10,0,0,34,36,1,0,0,0,35,28,1,0,0,0,35,30,1,0,0,0,35,
        31,1,0,0,0,36,48,1,0,0,0,37,38,10,6,0,0,38,39,5,8,0,0,39,47,3,4,
        2,7,40,41,10,5,0,0,41,42,5,7,0,0,42,47,3,4,2,6,43,44,10,4,0,0,44,
        45,5,6,0,0,45,47,3,4,2,5,46,37,1,0,0,0,46,40,1,0,0,0,46,43,1,0,0,
        0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,5,1,0,0,0,50,48,1,
        0,0,0,5,22,26,35,46,48
    ]

class ExpressoesParser ( Parser ):

    grammarFileName = "Expressoes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "';'", "<INVALID>", "<INVALID>", 
                     "'='", "<INVALID>", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "PV", "VAR", "NUM", "EQ", "OP1", 
                      "OP2", "OP3", "APAR", "FPAR", "ACHAVE", "FCHAVE", 
                      "BRANCO" ]

    RULE_prog = 0
    RULE_com = 1
    RULE_exp = 2

    ruleNames =  [ "prog", "com", "exp" ]

    EOF = Token.EOF
    PRINT=1
    PV=2
    VAR=3
    NUM=4
    EQ=5
    OP1=6
    OP2=7
    OP3=8
    APAR=9
    FPAR=10
    ACHAVE=11
    FCHAVE=12
    BRANCO=13

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
            self.state = 26
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
            elif token in [3]:
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
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(ExpressoesParser.ACHAVE)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2058) != 0):
                    self.state = 19
                    self.com()
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 25
                self.match(ExpressoesParser.FCHAVE)
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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 29
                self.match(ExpressoesParser.NUM)
                pass
            elif token in [3]:
                self.state = 30
                self.match(ExpressoesParser.VAR)
                pass
            elif token in [9]:
                self.state = 31
                self.match(ExpressoesParser.APAR)
                self.state = 32
                self.exp(0)
                self.state = 33
                self.match(ExpressoesParser.FPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 46
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 37
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 38
                        localctx.op = self.match(ExpressoesParser.OP3)
                        self.state = 39
                        self.exp(7)
                        pass

                    elif la_ == 2:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 40
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 41
                        localctx.op = self.match(ExpressoesParser.OP2)
                        self.state = 42
                        self.exp(6)
                        pass

                    elif la_ == 3:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 43
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 44
                        localctx.op = self.match(ExpressoesParser.OP1)
                        self.state = 45
                        self.exp(5)
                        pass

             
                self.state = 50
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
         




