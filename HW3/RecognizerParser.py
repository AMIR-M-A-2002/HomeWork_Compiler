# Generated from Recognizer.g4 by ANTLR 4.13.1
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
        4,1,7,26,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,4,0,11,8,0,11,0,
        12,0,12,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,2,0,
        2,0,0,29,0,10,1,0,0,0,2,14,1,0,0,0,4,11,3,2,1,0,5,11,5,1,0,0,6,11,
        5,2,0,0,7,11,5,4,0,0,8,11,5,3,0,0,9,11,5,5,0,0,10,4,1,0,0,0,10,5,
        1,0,0,0,10,6,1,0,0,0,10,7,1,0,0,0,10,8,1,0,0,0,10,9,1,0,0,0,11,12,
        1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,1,1,0,0,0,14,15,5,7,0,0,15,
        16,5,7,0,0,16,17,5,7,0,0,17,18,5,7,0,0,18,19,5,7,0,0,19,20,5,7,0,
        0,20,21,5,7,0,0,21,22,5,7,0,0,22,23,5,7,0,0,23,24,5,7,0,0,24,3,1,
        0,0,0,2,10,12
    ]

class recognizerParser ( Parser ):

    grammarFileName = "Recognizer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "EMAIL", "POSTAL_CODE", "VERSION", "DECIMAL", 
                      "URL", "QUOTED_STRING", "DIGIT" ]

    RULE_startRule = 0
    RULE_nationalID = 1

    ruleNames =  [ "startRule", "nationalID" ]

    EOF = Token.EOF
    EMAIL=1
    POSTAL_CODE=2
    VERSION=3
    DECIMAL=4
    URL=5
    QUOTED_STRING=6
    DIGIT=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nationalID(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(recognizerParser.NationalIDContext)
            else:
                return self.getTypedRuleContext(recognizerParser.NationalIDContext,i)


        def EMAIL(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.EMAIL)
            else:
                return self.getToken(recognizerParser.EMAIL, i)

        def POSTAL_CODE(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.POSTAL_CODE)
            else:
                return self.getToken(recognizerParser.POSTAL_CODE, i)

        def DECIMAL(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.DECIMAL)
            else:
                return self.getToken(recognizerParser.DECIMAL, i)

        def VERSION(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.VERSION)
            else:
                return self.getToken(recognizerParser.VERSION, i)

        def URL(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.URL)
            else:
                return self.getToken(recognizerParser.URL, i)

        def getRuleIndex(self):
            return recognizerParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)




    def startRule(self):

        localctx = recognizerParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 4
                    self.nationalID()
                    pass
                elif token in [1]:
                    self.state = 5
                    self.match(recognizerParser.EMAIL)
                    pass
                elif token in [2]:
                    self.state = 6
                    self.match(recognizerParser.POSTAL_CODE)
                    pass
                elif token in [4]:
                    self.state = 7
                    self.match(recognizerParser.DECIMAL)
                    pass
                elif token in [3]:
                    self.state = 8
                    self.match(recognizerParser.VERSION)
                    pass
                elif token in [5]:
                    self.state = 9
                    self.match(recognizerParser.URL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 190) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NationalIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(recognizerParser.DIGIT)
            else:
                return self.getToken(recognizerParser.DIGIT, i)

        def getRuleIndex(self):
            return recognizerParser.RULE_nationalID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNationalID" ):
                listener.enterNationalID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNationalID" ):
                listener.exitNationalID(self)




    def nationalID(self):

        localctx = recognizerParser.NationalIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nationalID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(recognizerParser.DIGIT)
            self.state = 15
            self.match(recognizerParser.DIGIT)
            self.state = 16
            self.match(recognizerParser.DIGIT)
            self.state = 17
            self.match(recognizerParser.DIGIT)
            self.state = 18
            self.match(recognizerParser.DIGIT)
            self.state = 19
            self.match(recognizerParser.DIGIT)
            self.state = 20
            self.match(recognizerParser.DIGIT)
            self.state = 21
            self.match(recognizerParser.DIGIT)
            self.state = 22
            self.match(recognizerParser.DIGIT)
            self.state = 23
            self.match(recognizerParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





