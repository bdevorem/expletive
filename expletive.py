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
# n?#+ {baa}          * input = 

import sys
import Queue

tape = Queue.Queue() # 2-tag queue, turing-tape
prog = sys.argv[1] # user's program
# print prog
lines = []

### Open file and read in data
try:
	with open(prog) as input_file:
    	for i, line in enumerate(input_file):
			lines.append(line)
        	
except IOError as e:
	print str(e)


### Parse through program
alph = []
halt = []
rules = {}

for line in lines:
	line = line.replace("}", "").split("{")
	
	if line[0].strip() == '@|?h':
		for sym in line[1].replace(" ", ""):
			alph.append(sym)

	elif line[0].strip() == 'h@|+':
		for sym in line[1].replace(" ", ""):
			halt.append(sym)

	elif line[0].strip() == 'r#|3':
		rules[line[1].strip()] = line[2].strip()

	elif line[0].strip() == 'n?#+':
		for sym in line[1].strip():
			tape.put(sym)

### Operate on queue



	
	







