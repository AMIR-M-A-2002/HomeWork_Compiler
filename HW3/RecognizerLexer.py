# Generated from Recognizer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,82,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,4,2,28,
        8,2,11,2,12,2,29,1,2,1,2,4,2,34,8,2,11,2,12,2,35,3,2,38,8,2,1,3,
        4,3,41,8,3,11,3,12,3,42,1,3,1,3,4,3,47,8,3,11,3,12,3,48,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,60,8,4,11,4,12,4,61,1,4,1,4,4,4,
        66,8,4,11,4,12,4,67,1,5,1,5,5,5,72,8,5,10,5,12,5,75,9,5,1,5,1,5,
        1,6,1,6,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,0,1,0,2,1,
        0,48,57,1,0,34,34,89,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,17,1,0,0,0,3,19,1,0,
        0,0,5,27,1,0,0,0,7,40,1,0,0,0,9,50,1,0,0,0,11,69,1,0,0,0,13,78,1,
        0,0,0,15,80,1,0,0,0,17,18,3,11,5,0,18,2,1,0,0,0,19,20,7,0,0,0,20,
        24,6,1,0,0,21,22,5,45,0,0,22,23,7,0,0,0,23,25,6,1,1,0,24,21,1,0,
        0,0,24,25,1,0,0,0,25,4,1,0,0,0,26,28,3,13,6,0,27,26,1,0,0,0,28,29,
        1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,37,1,0,0,0,31,33,5,46,0,0,
        32,34,3,13,6,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,
        0,0,0,36,38,1,0,0,0,37,31,1,0,0,0,37,38,1,0,0,0,38,6,1,0,0,0,39,
        41,3,13,6,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,
        0,0,43,44,1,0,0,0,44,46,5,46,0,0,45,47,3,13,6,0,46,45,1,0,0,0,47,
        48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,8,1,0,0,0,50,51,5,104,
        0,0,51,52,5,116,0,0,52,53,5,116,0,0,53,54,5,112,0,0,54,55,5,58,0,
        0,55,56,5,47,0,0,56,57,5,47,0,0,57,59,1,0,0,0,58,60,3,15,7,0,59,
        58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,
        0,63,65,5,46,0,0,64,66,3,15,7,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,
        1,0,0,0,67,68,1,0,0,0,68,10,1,0,0,0,69,73,5,34,0,0,70,72,8,1,0,0,
        71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,
        0,0,0,75,73,1,0,0,0,76,77,5,34,0,0,77,12,1,0,0,0,78,79,7,0,0,0,79,
        14,1,0,0,0,80,81,9,0,0,0,81,16,1,0,0,0,10,0,24,29,35,37,42,48,61,
        67,73,2,1,1,0,1,1,1
    ]

class recognizerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EMAIL = 1
    POSTAL_CODE = 2
    VERSION = 3
    DECIMAL = 4
    URL = 5
    QUOTED_STRING = 6
    DIGIT = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "EMAIL", "POSTAL_CODE", "VERSION", "DECIMAL", "URL", "QUOTED_STRING", 
            "DIGIT" ]

    ruleNames = [ "EMAIL", "POSTAL_CODE", "VERSION", "DECIMAL", "URL", "QUOTED_STRING", 
                  "DIGIT", "ANY_CHAR" ]

    grammarFileName = "Recognizer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.POSTAL_CODE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def POSTAL_CODE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            5
     

        if actionIndex == 1:
            4
     


