# gramatica.py
"""
Gramática para expresiones y asignaciones en Python simplificado
---------------------------------------------------------------

program     -> stmt_list

stmt_list   -> stmt (NEWLINE stmt)*

stmt        -> ID "=" expr
             | expr

expr        -> term ((PLUS | MINUS) term)*

term        -> factor ((TIMES | DIV) factor)*

factor      -> NUMBER
             | ID
             | "(" expr ")"

Tokens:
NUMBER   = dígitos (con o sin decimal)
ID       = letra o "_" seguido de letras, dígitos o "_"
PLUS     = "+"
MINUS    = "-"
TIMES    = "*"
DIV      = "/"
EQ       = "="
LPAREN   = "("
RPAREN   = ")"
NEWLINE  = "\n"
"""

GRAMATICA = __doc__
