# Generated from D:/REPO/HW4/Password.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,67,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,4,0,17,8,0,11,0,12,0,18,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,3,6,66,8,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,
        13,7,1,0,1,3,0,9,10,13,13,32,32,70,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,16,1,0,
        0,0,3,22,1,0,0,0,5,24,1,0,0,0,7,26,1,0,0,0,9,28,1,0,0,0,11,58,1,
        0,0,0,13,65,1,0,0,0,15,17,7,0,0,0,16,15,1,0,0,0,17,18,1,0,0,0,18,
        16,1,0,0,0,18,19,1,0,0,0,19,20,1,0,0,0,20,21,6,0,0,0,21,2,1,0,0,
        0,22,23,2,65,90,0,23,4,1,0,0,0,24,25,2,97,122,0,25,6,1,0,0,0,26,
        27,2,48,57,0,27,8,1,0,0,0,28,29,5,33,0,0,29,30,5,34,0,0,30,31,5,
        36,0,0,31,32,5,37,0,0,32,33,5,94,0,0,33,34,5,42,0,0,34,35,5,40,0,
        0,35,36,5,41,0,0,36,37,5,95,0,0,37,38,5,43,0,0,38,39,5,61,0,0,39,
        40,5,45,0,0,40,41,5,123,0,0,41,42,5,124,0,0,42,43,5,125,0,0,43,44,
        5,91,0,0,44,45,5,93,0,0,45,46,5,59,0,0,46,47,5,58,0,0,47,48,1,0,
        0,0,48,49,5,64,0,0,49,50,5,35,0,0,50,51,5,60,0,0,51,52,5,62,0,0,
        52,53,5,44,0,0,53,54,5,126,0,0,54,55,5,96,0,0,55,56,5,63,0,0,56,
        57,5,46,0,0,57,10,1,0,0,0,58,59,9,0,0,0,59,60,6,5,1,0,60,12,1,0,
        0,0,61,66,3,3,1,0,62,66,3,5,2,0,63,66,3,7,3,0,64,66,3,9,4,0,65,61,
        1,0,0,0,65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,14,1,0,0,0,
        3,0,18,65,2,6,0,0,1,5,0
    ]

class PasswordLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SPACES = 1
    UPPER = 2
    LOWER = 3
    DIGIT = 4
    SYMBOL = 5
    MIN_LENGTH = 6
    CHARS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "SPACES", "UPPER", "LOWER", "DIGIT", "SYMBOL", "MIN_LENGTH", 
            "CHARS" ]

    ruleNames = [ "SPACES", "UPPER", "LOWER", "DIGIT", "SYMBOL", "MIN_LENGTH", 
                  "CHARS" ]

    grammarFileName = "Password.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.MIN_LENGTH_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def MIN_LENGTH_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            8
     


