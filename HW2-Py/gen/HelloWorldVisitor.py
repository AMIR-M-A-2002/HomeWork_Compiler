# Generated from D:/antlr/Newf/HelloWorld.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HelloWorldParser import HelloWorldParser
else:
    from HelloWorldParser import HelloWorldParser

# This class defines a complete generic visitor for a parse tree produced by HelloWorldParser.

class HelloWorldVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HelloWorldParser#r.
    def visitR(self, ctx:HelloWorldParser.RContext):
        return self.visitChildren(ctx)



del HelloWorldParser