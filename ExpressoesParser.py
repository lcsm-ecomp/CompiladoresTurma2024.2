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
        4,1,5,24,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,3,1,11,8,1,1,1,
        1,1,1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,0,1,2,2,0,2,
        0,0,24,0,4,1,0,0,0,2,10,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,
        0,0,7,8,6,1,-1,0,8,11,5,2,0,0,9,11,5,1,0,0,10,7,1,0,0,0,10,9,1,0,
        0,0,11,20,1,0,0,0,12,13,10,4,0,0,13,14,5,4,0,0,14,19,3,2,1,5,15,
        16,10,3,0,0,16,17,5,3,0,0,17,19,3,2,1,4,18,12,1,0,0,0,18,15,1,0,
        0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,3,1,0,0,0,22,20,
        1,0,0,0,3,10,18,20
    ]

class ExpressoesParser ( Parser ):

    grammarFileName = "Expressoes.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "VAR", "NUM", "OP1", "OP2", "BRANCO" ]

    RULE_prog = 0
    RULE_exp = 1

    ruleNames =  [ "prog", "exp" ]

    EOF = Token.EOF
    VAR=1
    NUM=2
    OP1=3
    OP2=4
    BRANCO=5

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

        def exp(self):
            return self.getTypedRuleContext(ExpressoesParser.ExpContext,0)


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
            self.state = 4
            self.exp(0)
            self.state = 5
            self.match(ExpressoesParser.EOF)
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressoesParser.ExpContext)
            else:
                return self.getTypedRuleContext(ExpressoesParser.ExpContext,i)


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
            self.state = 10
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 8
                self.match(ExpressoesParser.NUM)
                pass
            elif token in [1]:
                self.state = 9
                self.match(ExpressoesParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 18
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 12
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 13
                        localctx.op = self.match(ExpressoesParser.OP2)
                        self.state = 14
                        self.exp(5)
                        pass

                    elif la_ == 2:
                        localctx = ExpressoesParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 15
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 16
                        localctx.op = self.match(ExpressoesParser.OP1)
                        self.state = 17
                        self.exp(4)
                        pass

             
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self._predicates[1] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




