grammar Password;

// Tokens

SPACES  : [ \t\r\n]+           -> skip;
UPPER   : 'A' .. 'Z';
LOWER   : 'a' .. 'z';
DIGIT   : '0' .. '9';
SYMBOL  : '!"$%^*()_+=-{|}[];:''@#<>,~`?.';

// Rule for a valid password

password : MIN_LENGTH CHARS;

// Minimum length rule

MIN_LENGTH : .{8};

// Character rule (excluding spaces)

CHARS   : UPPER | LOWER | DIGIT | SYMBOL;
