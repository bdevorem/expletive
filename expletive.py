#!/usr/bin/python2

# xpl3t!v3 interpreter
# Author: Breanna Devore-McDonald
# Usage: 
#		chmod +x expletive.py
#		./expletive.py [program.xpl]

# Program needs to define input alphabet.
# Can also provide halting symbol, if no
# symbol is given, program will halt when
# tape queue reaches length <= 1, or no
# rule is found for the symbol at the head

# @|?h {a b c d}      * alph =
# h@|+ {H}            * halt =
# r#|3 {a} {ccbaH}    * rule =
# r#|3 {b} {cca}      * rule =
# r#|3 {c} {cc}       * rule =

import sys
import Queue

tape = Queue.Queue() # 2-tag queue, turing-tape
prog = sys.argv[1] # user's program
# print prog
