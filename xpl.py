#!/usr/bin/python2

# xpl3t!v3 interpreter
# Author: Breanna Devore-McDonald
# Usage: 
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
import getopt

def _verbose():
	for elem in list(tape.queue):
		print elem,
		#pass
	print "\n-------------\n"


def test():
	print "Test\n------------"
	print "Alph = "
	for sym in alph:
		print sym,
	print "\n\nHalt = "
	for sym in halt:
		print sym,
	print "\n\nRules = "
	for key, val in rules.iteritems():
		print key + " --> " + val,
	print "\nInput = "
	for elem in list(tape.queue):
		print elem,

tape = Queue.Queue() # 2-tag queue, turing-tape
prog = sys.argv[1] # user's program

verbose = False
init = False
init_config = ""

#print 'ARGV:', sys.argv[1:]

options, remainder = getopt.getopt(sys.argv[2:], 'i:v', ['initial=', 
                                                         'verbose',
                                                         ])
#print 'OPTIONS:', options
for opt, arg in options:
	#print opt + " " + arg
	if opt in ('-i', '--initial'):
		init = True
		init_config = arg
	elif opt in ('-v', '--verbose'):
		verbose = True

#print 'VERBOSE:', verbose
#print 'INITIAL:', init_config
#print 'REMAINING :', remainder

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
		comment = False
		for sym in line[1].replace(" ", ""):
			if sym == "*":
				comment = True
			if comment is False:
				alph.append(sym)

	elif line[0].strip() == 'h@|+':
		comment = False
		for sym in line[1].replace(" ", ""):
			if sym == "*":
				comment = True
			if comment is False:
				halt.append(sym)

	elif line[0].strip() == 'r#|3':
		r = ""
		for sym in line[2].strip().rstrip():
			if sym == "*":
				break
			r = r + sym
		rules[line[1].strip()] = r 

	elif line[0].strip() == 'n?#+':
		if init is False:
			for sym in line[1].strip():
				if sym == "*":		
					break
				if sym is not " ":
					tape.put(sym)
		else:
			for elem in init_config:
				tape.put(elem)

	elif line[0].strip() == '+|+13':
		print line[1].strip()
		print '-------------'

""" * considering a counting tape to solve counting problems *
	elif line[0].strip() == 'c0#n+':
		print len(line[1].strip())
"""

#test()

### Operate on queue
#print "\n"
while not tape.empty():
	if verbose:
		_verbose()

	sym = tape.get()

	if sym in halt:
		break
	if tape.qsize() < 2:
		break

	if sym in rules:
		for elem in rules[sym]:
			if elem is not " ":
				tape.put(elem)
	sym = tape.get()

### Display resulting queue
#print "Resulting tape:"
for elem in list(tape.queue):
	print elem,
	
	







