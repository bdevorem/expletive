# xpl3t!v3 Formalisms

## Grammar
S -> ALPH | HALT | RULE | INPUT | TITLE | COMMENT | NEWLINE  
  
ALPH -> @|?h A  
A -> symbolA | epsilon  
  
HALT -> h@|+ H  
H -> symbol | epsilon  
  
RULE -> r#|3 R A  
R -> symbol   
  
INPUT -> n?#+ A  
  
TITLE -> +|+13 A  
  
COMMENT -> *A  
  
NEWLINE -> epsilon  
  

## Notes
Symbols can be represented by single or multiple characters.  
Example: `r#|3 a abc` maps `a` to the single symbol `abc`. 
Whereas, `r#|3 a a b c` maps `a` to the sequence of symbols
`a`, `b`, and `c`.  
Inline comments are not currently supported.  



