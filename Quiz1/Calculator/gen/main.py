import antlr4
from antlr4 import ParseTreeVisitor
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from CalculatorVisitor import CalculatorVisitor
class EvalVisitor(ParseTreeVisitor):
    def visitAdditiveExpression(self, ctx):
        left = self.visit(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            if ctx.getChild(2*i-1).getText() == '+':
                left += self.visit(ctx.multiplicativeExpression(i))
            else:
                left -= self.visit(ctx.multiplicativeExpression(i))
        return left

    def visitMultiplicativeExpression(self, ctx):
        left = self.visit(ctx.powerExpression(0))
        for i in range(1, len(ctx.powerExpression())):
            if ctx.getChild(2*i-1).getText() == '*':
                left *= self.visit(ctx.powerExpression(i))
            else:
                left /= self.visit(ctx.powerExpression(i))
        return left

    def visitPowerExpression(self, ctx):
        left = self.visit(ctx.primaryExpression(0))
        for i in range(1, len(ctx.primaryExpression())):
            left **= self.visit(ctx.primaryExpression(i))
        return left

    def visitPrimaryExpression(self, ctx):
        if ctx.expression():
            return self.visit(ctx.expression())
        else:
            return float(ctx.NUMBER().getText())

def evaluate(expression):
    input_stream = antlr4.InputStream(expression)
    lexer = CalculatorLexer(input_stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = CalculatorParser(token_stream)
    tree = parser.expression()
    visitor = EvalVisitor()
    return visitor.visit(tree)

print(evaluate("3*2+6-(7/9)+7^3*9-10"))
