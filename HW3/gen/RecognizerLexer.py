# Generated from D:/antlr/recognizer/Recognizer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,96,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,4,0,17,8,0,11,0,12,0,18,1,0,4,0,22,8,0,11,0,12,0,23,1,
        0,4,0,27,8,0,11,0,12,0,28,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,39,
        8,1,1,2,4,2,42,8,2,11,2,12,2,43,1,2,1,2,4,2,48,8,2,11,2,12,2,49,
        3,2,52,8,2,1,3,4,3,55,8,3,11,3,12,3,56,1,3,1,3,4,3,61,8,3,11,3,12,
        3,62,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,74,8,4,11,4,12,4,75,
        1,4,1,4,4,4,80,8,4,11,4,12,4,81,4,4,84,8,4,11,4,12,4,85,1,5,1,5,
        1,6,4,6,91,8,6,11,6,12,6,92,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,1,0,7,7,0,37,37,43,43,45,46,48,57,65,90,95,95,97,122,1,0,
        64,64,4,0,45,46,48,57,65,90,97,122,4,0,43,43,65,91,93,93,97,122,
        1,0,48,57,2,0,65,90,97,122,3,0,9,10,13,13,32,32,108,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,1,16,1,0,0,0,3,33,1,0,0,0,5,41,1,0,0,0,7,54,1,0,0,0,9,64,
        1,0,0,0,11,87,1,0,0,0,13,90,1,0,0,0,15,17,7,0,0,0,16,15,1,0,0,0,
        17,18,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,0,20,22,7,
        1,0,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,
        26,1,0,0,0,25,27,7,2,0,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,
        0,28,29,1,0,0,0,29,30,1,0,0,0,30,31,7,3,0,0,31,32,6,0,0,0,32,2,1,
        0,0,0,33,34,7,4,0,0,34,38,6,1,1,0,35,36,5,45,0,0,36,37,7,4,0,0,37,
        39,6,1,2,0,38,35,1,0,0,0,38,39,1,0,0,0,39,4,1,0,0,0,40,42,3,11,5,
        0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,51,
        1,0,0,0,45,47,5,46,0,0,46,48,3,11,5,0,47,46,1,0,0,0,48,49,1,0,0,
        0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,45,1,0,0,0,51,52,
        1,0,0,0,52,6,1,0,0,0,53,55,3,11,5,0,54,53,1,0,0,0,55,56,1,0,0,0,
        56,54,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,60,5,46,0,0,59,61,3,
        11,5,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,
        8,1,0,0,0,64,65,5,104,0,0,65,66,5,116,0,0,66,67,5,116,0,0,67,68,
        5,112,0,0,68,69,5,58,0,0,69,70,5,47,0,0,70,71,5,47,0,0,71,73,1,0,
        0,0,72,74,7,2,0,0,73,72,1,0,0,0,74,75,1,0,0,0,75,73,1,0,0,0,75,76,
        1,0,0,0,76,83,1,0,0,0,77,79,5,46,0,0,78,80,7,5,0,0,79,78,1,0,0,0,
        80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,77,1,
        0,0,0,84,85,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,10,1,0,0,0,87,
        88,7,4,0,0,88,12,1,0,0,0,89,91,7,6,0,0,90,89,1,0,0,0,91,92,1,0,0,
        0,92,90,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,6,6,3,0,95,14,
        1,0,0,0,14,0,18,23,28,38,43,49,51,56,62,75,81,85,92,4,1,0,0,1,1,
        1,1,1,2,6,0,0
    ]

class RecognizerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EMAIL = 1
    POSTAL_CODE = 2
    VERSION = 3
    DECIMAL = 4
    URL = 5
    DIGIT = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "EMAIL", "POSTAL_CODE", "VERSION", "DECIMAL", "URL", "DIGIT", 
            "WS" ]

    ruleNames = [ "EMAIL", "POSTAL_CODE", "VERSION", "DECIMAL", "URL", "DIGIT", 
                  "WS" ]

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
            actions[0] = self.EMAIL_action 
            actions[1] = self.POSTAL_CODE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def EMAIL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            2,
     

    def POSTAL_CODE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            5
     

        if actionIndex == 2:
            4
     


