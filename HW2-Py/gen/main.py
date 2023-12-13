# Import the ANTLR runtime for Python
from antlr4 import *

# Import the generated lexer and parser
from HelloWorldLexer import HelloWorldLexer
from HelloWorldParser import HelloWorldParser

# Create an input stream from standard input
input_stream = InputStream("hello world")

# Create a lexer
lexer = HelloWorldLexer(input_stream)

# Create a token stream from the lexer
token_stream = CommonTokenStream(lexer)

# Create a parser
parser = HelloWorldParser(token_stream)

# Start parsing from the rule 'r'
tree = parser.r()

# Print the parse tree
print(tree.toStringTree(recog=parser))
