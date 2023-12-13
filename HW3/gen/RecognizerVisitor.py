# Generated from D:/antlr/recognizer/Recognizer.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RecognizerParser import RecognizerParser
else:
    from RecognizerParser import RecognizerParser

# This class defines a complete generic visitor for a parse tree produced by RecognizerParser.

class RecognizerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RecognizerParser#nationalID.
    def visitNationalID(self, ctx:RecognizerParser.NationalIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RecognizerParser#startRule.
    def visitStartRule(self, ctx:RecognizerParser.StartRuleContext):
        return self.visitChildren(ctx)



del RecognizerParser