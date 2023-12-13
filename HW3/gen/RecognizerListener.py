# Generated from D:/antlr/recognizer/Recognizer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RecognizerParser import RecognizerParser
else:
    from RecognizerParser import RecognizerParser

# This class defines a complete listener for a parse tree produced by RecognizerParser.
class RecognizerListener(ParseTreeListener):

    # Enter a parse tree produced by RecognizerParser#nationalID.
    def enterNationalID(self, ctx:RecognizerParser.NationalIDContext):
        pass

    # Exit a parse tree produced by RecognizerParser#nationalID.
    def exitNationalID(self, ctx:RecognizerParser.NationalIDContext):
        pass


    # Enter a parse tree produced by RecognizerParser#startRule.
    def enterStartRule(self, ctx:RecognizerParser.StartRuleContext):
        pass

    # Exit a parse tree produced by RecognizerParser#startRule.
    def exitStartRule(self, ctx:RecognizerParser.StartRuleContext):
        pass



del RecognizerParser