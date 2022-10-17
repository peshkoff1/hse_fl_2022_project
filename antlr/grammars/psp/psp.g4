grammar psp;

file_ : expression* EOF;

expression      : S;

S       : '('S')'S1
        | ;

S1      : '['S']'S 
        | ;

WS       : [ \r\n\t] + -> skip ;