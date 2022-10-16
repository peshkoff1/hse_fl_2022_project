# Generated from arithmetic.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,3,0,25,8,0,1,0,4,0,28,
        8,0,11,0,12,0,29,1,1,1,1,3,1,34,8,1,1,2,1,2,3,2,38,8,2,1,3,1,3,1,
        4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,55,8,10,
        11,10,12,10,56,1,10,1,10,0,0,11,1,1,3,2,5,3,7,4,9,5,11,0,13,0,15,
        0,17,0,19,6,21,7,1,0,1,3,0,9,10,13,13,32,32,60,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,1,24,1,0,0,0,3,33,1,0,0,0,5,37,1,0,0,0,7,39,1,0,0,0,9,41,1,0,
        0,0,11,43,1,0,0,0,13,45,1,0,0,0,15,47,1,0,0,0,17,49,1,0,0,0,19,51,
        1,0,0,0,21,54,1,0,0,0,23,25,5,45,0,0,24,23,1,0,0,0,24,25,1,0,0,0,
        25,27,1,0,0,0,26,28,2,48,57,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,
        1,0,0,0,29,30,1,0,0,0,30,2,1,0,0,0,31,34,3,11,5,0,32,34,3,13,6,0,
        33,31,1,0,0,0,33,32,1,0,0,0,34,4,1,0,0,0,35,38,3,15,7,0,36,38,3,
        17,8,0,37,35,1,0,0,0,37,36,1,0,0,0,38,6,1,0,0,0,39,40,5,40,0,0,40,
        8,1,0,0,0,41,42,5,41,0,0,42,10,1,0,0,0,43,44,5,43,0,0,44,12,1,0,
        0,0,45,46,5,45,0,0,46,14,1,0,0,0,47,48,5,42,0,0,48,16,1,0,0,0,49,
        50,5,47,0,0,50,18,1,0,0,0,51,52,5,94,0,0,52,20,1,0,0,0,53,55,7,0,
        0,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,58,
        1,0,0,0,58,59,6,10,0,0,59,22,1,0,0,0,6,0,24,29,33,37,56,1,6,0,0
    ]

class arithmeticLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    SUM_SIGN = 2
    MULT_SIGN = 3
    LPAREN = 4
    RPAREN = 5
    POW = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "SUM_SIGN", "MULT_SIGN", "LPAREN", "RPAREN", "POW", 
            "WS" ]

    ruleNames = [ "NUMBER", "SUM_SIGN", "MULT_SIGN", "LPAREN", "RPAREN", 
                  "PLUS", "MINUS", "TIMES", "DIV", "POW", "WS" ]

    grammarFileName = "arithmetic.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

