grammar HelloWorld;     // The name of the grammar is Hello
r  : 'hello' ID ;         // The rule/production r match keyword `hello` followed by the rule `ID`
ID : [a-z]+ ;             // The rule/production `ID` match all lower-case characters
WS : [ \t\r\n]+ -> skip ; // This WS rule (WhiteSpace) skip spaces, tabs, newlines