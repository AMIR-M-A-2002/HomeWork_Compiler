# Generated from HelloWorld.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HelloWorldParser import HelloWorldParser
else:
    from HelloWorldParser import HelloWorldParser

# This class defines a complete listener for a parse tree produced by HelloWorldParser.
class HelloWorldListener(ParseTreeListener):

    # Enter a parse tree produced by HelloWorldParser#r.
    def enterR(self, ctx:HelloWorldParser.RContext):
        pass

    # Exit a parse tree produced by HelloWorldParser#r.
    def exitR(self, ctx:HelloWorldParser.RContext):
        pass



del HelloWorldParser