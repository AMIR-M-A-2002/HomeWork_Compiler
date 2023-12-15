# Generated from D:/REPO/HW4/Password.g4 by ANTLR 4.13.1
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
        4,1,7,6,2,0,7,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,4,0,2,1,0,0,0,2,3,5,
        6,0,0,3,4,5,7,0,0,4,1,1,0,0,0,0
    ]

class PasswordParser ( Parser ):

    grammarFileName = "Password.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "SPACES", "UPPER", "LOWER", "DIGIT", 
                      "SYMBOL", "MIN_LENGTH", "CHARS" ]

    RULE_password = 0

    ruleNames =  [ "password" ]

    EOF = Token.EOF
    SPACES=1
    UPPER=2
    LOWER=3
    DIGIT=4
    SYMBOL=5
    MIN_LENGTH=6
    CHARS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PasswordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIN_LENGTH(self):
            return self.getToken(PasswordParser.MIN_LENGTH, 0)

        def CHARS(self):
            return self.getToken(PasswordParser.CHARS, 0)

        def getRuleIndex(self):
            return PasswordParser.RULE_password

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassword" ):
                listener.enterPassword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassword" ):
                listener.exitPassword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassword" ):
                return visitor.visitPassword(self)
            else:
                return visitor.visitChildren(self)




    def password(self):

        localctx = PasswordParser.PasswordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_password)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(PasswordParser.MIN_LENGTH)
            self.state = 3
            self.match(PasswordParser.CHARS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





