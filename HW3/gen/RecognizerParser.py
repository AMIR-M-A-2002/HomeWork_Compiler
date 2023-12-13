# Generated from D:/antlr/recognizer/Recognizer.g4 by ANTLR 4.13.1
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
        4,1,7,18,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,4,1,
        14,8,1,11,1,12,1,15,1,1,0,0,2,0,2,0,0,21,0,4,1,0,0,0,2,13,1,0,0,
        0,4,5,5,6,0,0,5,6,6,0,-1,0,6,1,1,0,0,0,7,14,3,0,0,0,8,14,5,1,0,0,
        9,14,5,2,0,0,10,14,5,4,0,0,11,14,5,3,0,0,12,14,5,5,0,0,13,7,1,0,
        0,0,13,8,1,0,0,0,13,9,1,0,0,0,13,10,1,0,0,0,13,11,1,0,0,0,13,12,
        1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,3,1,0,0,0,2,
        13,15
    ]

class RecognizerParser ( Parser ):

    grammarFileName = "Recognizer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "EMAIL", "POSTAL_CODE", "VERSION", "DECIMAL", 
                      "URL", "DIGIT", "WS" ]

    RULE_nationalID = 0
    RULE_startRule = 1

    ruleNames =  [ "nationalID", "startRule" ]

    EOF = Token.EOF
    EMAIL=1
    POSTAL_CODE=2
    VERSION=3
    DECIMAL=4
    URL=5
    DIGIT=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NationalIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(RecognizerParser.DIGIT, 0)

        def getRuleIndex(self):
            return RecognizerParser.RULE_nationalID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNationalID" ):
                listener.enterNationalID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNationalID" ):
                listener.exitNationalID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNationalID" ):
                return visitor.visitNationalID(self)
            else:
                return visitor.visitChildren(self)




    def nationalID(self):

        localctx = RecognizerParser.NationalIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_nationalID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(RecognizerParser.DIGIT)
            10
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nationalID(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RecognizerParser.NationalIDContext)
            else:
                return self.getTypedRuleContext(RecognizerParser.NationalIDContext,i)


        def EMAIL(self, i:int=None):
            if i is None:
                return self.getTokens(RecognizerParser.EMAIL)
            else:
                return self.getToken(RecognizerParser.EMAIL, i)

        def POSTAL_CODE(self, i:int=None):
            if i is None:
                return self.getTokens(RecognizerParser.POSTAL_CODE)
            else:
                return self.getToken(RecognizerParser.POSTAL_CODE, i)

        def DECIMAL(self, i:int=None):
            if i is None:
                return self.getTokens(RecognizerParser.DECIMAL)
            else:
                return self.getToken(RecognizerParser.DECIMAL, i)

        def VERSION(self, i:int=None):
            if i is None:
                return self.getTokens(RecognizerParser.VERSION)
            else:
                return self.getToken(RecognizerParser.VERSION, i)

        def URL(self, i:int=None):
            if i is None:
                return self.getTokens(RecognizerParser.URL)
            else:
                return self.getToken(RecognizerParser.URL, i)

        def getRuleIndex(self):
            return RecognizerParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartRule" ):
                return visitor.visitStartRule(self)
            else:
                return visitor.visitChildren(self)




    def startRule(self):

        localctx = RecognizerParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_startRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 7
                    self.nationalID()
                    pass
                elif token in [1]:
                    self.state = 8
                    self.match(RecognizerParser.EMAIL)
                    pass
                elif token in [2]:
                    self.state = 9
                    self.match(RecognizerParser.POSTAL_CODE)
                    pass
                elif token in [4]:
                    self.state = 10
                    self.match(RecognizerParser.DECIMAL)
                    pass
                elif token in [3]:
                    self.state = 11
                    self.match(RecognizerParser.VERSION)
                    pass
                elif token in [5]:
                    self.state = 12
                    self.match(RecognizerParser.URL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





