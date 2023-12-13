// Recognizer.g4
grammar Recognizer;

// Define lexer rules
EMAIL: [a-zA-Z0-9._%+-]+[@]+[a-zA-Z0-9.-]+[\]+[a-zA-Z]{2,};
POSTAL_CODE: [0-9]{5}('-'[0-9]{4})?;
VERSION: DIGIT+('.'DIGIT+)?;
DECIMAL: DIGIT+ '.' DIGIT+;
URL: 'http://' [a-zA-Z0-9.-]+('.'[a-zA-Z]+)+;

// National ID: A simplified version considering it's a numeric value
nationalID: DIGIT{10};

// Define parser rules
startRule: (nationalID | EMAIL | POSTAL_CODE | DECIMAL | VERSION | URL)+;

// Common tokens
DIGIT: [0-9];
WS: [ \t\r\n]+ -> skip;
