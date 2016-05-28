# xpl3t!v3 Grammar


S -> ALPH | HALT | RULE | INPUT | TITLE | COMMENT | NEWLINE

ALPH -> @|?h {A}
A -> *symbol*A | *epsilon*

HALT -> h@|+ {H}
H -> *symbol* | *epsilon*

RULE -> r#|3 {R} {A}
R -> *symbol* 

INPUT -> n?#+ {A}

TITLE -> +|+13 {A}

COMMENT -> *A

NEWLINE -> *epsilon*

