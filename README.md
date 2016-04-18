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
Define an alphabet:&nbsp;&nbsp;&nbsp;@|?h {}  
\* Define halting symbols:&nbsp;h@|+ {}  
Define rules:&nbsp;&nbsp;&nbsp;r#|3 {}  
  
\* unnecessary  

##Examples
```
@|?h {a b c d}				* alph = a, b, c, d
h@|+ {H} 					* halt = H
r#|3 {a} {ccbaH} 		* rule = a --> ccbaH
r#|3 {b} {cca} 				* rule = b --> cca
r#|3 {c} {cc} 				* rule = c --> cc
```

##To Do
- [x] start  
- [x] determine functionality of language  
- [x] write interpreter

##Future Work
- [ ] add site?

##Contributors
[Breanna Devore-McDonald](http://breanna-devore-mcdonald.herokuapp.com)  
[Nicholas Jones](http://www.nicholascjones.com)  

##Sources
https://en.wikipedia.org/wiki/Tag_system  
http://beza1e1.tuxen.de/articles/accidentally_turing_complete.html
