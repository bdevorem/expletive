xpl3t!v3 
===========

An especially esoteric programming language for the Turing-complete 
2-tag system.  
Read: expletive  
Python 2.x.x required  
Currently: **stable**

##Grammar
xpl3t!v3 programs are based on Emil Leon Post's tag system from
1943. Tag systems are Turing-complete deterministic computational 
models using a single queue as the Turing Machine 'tape'. In 
xpl3t!v3, 2-tag systems are used: when one symbol is read, two get
popped off from the beginning of the queue, and a specific amount 
of symbols get pushed onto the back (predetermined by user-specified
rules).  

##Usage
A program written in xpl3t!v3 needs to have three key things: 
an input alphabet, rules for each alphabet symbol, and an initial
configuration. Optionally, a halting symbol can be defined. If one
is not defined, the program will halt when the length of the queue
is less than 2 symbols. For more information, check out xpl3t!v3's 
docs [here](https://expletive.herokuapp.com).

##Example
A valid xpl3t!v3 program:  
```
@|?h {a b c d}  
h@|+ {H}  
r#|3 {a} {ccbaH}   
r#|3 {b} {cca} 	
r#|3 {c} {cc}  
```

##To Do
- [x] start  
- [x] determine functionality of language  
- [x] write interpreter

##Future Work
- [x] add site?

##Contributors
[Breanna Devore-McDonald](http://breanna-devore-mcdonald.herokuapp.com)  
[Nicholas Jones](http://www.nicholascjones.com)  

##Sources
https://en.wikipedia.org/wiki/Tag_system  
http://beza1e1.tuxen.de/articles/accidentally_turing_complete.html
