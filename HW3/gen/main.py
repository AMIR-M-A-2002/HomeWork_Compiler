from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from RecognizerLexer import RecognizerLexer
from RecognizerParser import RecognizerParser
from RecognizerListener import RecognizerListener


class MyListener(RecognizerListener):
    def enterStartRule(self, ctx):
        print(f"Matched: {ctx.getText()}")

def main():
    input_text = "123456789 test@gmail.com 123456789 82943756 3.14 http://www.test.ut.ac.ir"

    # Create an input stream from the input text
    input_stream = InputStream(input_text)

    # Create a lexer
    lexer = RecognizerLexer(input_stream)

    # Create a token stream from the lexer
    token_stream = CommonTokenStream(lexer)

    # Create a parser
    parser = RecognizerParser(token_stream)

    # Add a custom listener to the parser
    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, parser.startRule())

if __name__ == "__main__":
    main()
