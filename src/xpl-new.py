#!/usr/bin/env python2
# xpl
# Breanna Devore-McDonald

from token import Token
from lexer import Lexer
from interpreter import Interpreter
import sys
import Queue
import getopt

EOF =  'EOF'
SYMBOL, L_BRACKET, R_BRACKET = 'SYMBOL', 'L_BRACKET', 'R_BRACKET'
ALPH, HALT, RULE = 'ALPH', 'HALT', 'RULE'
INPUT, TITLE, COMMENT = 'INPUT', 'TITLE', 'COMMENT'

if __name__ == '__main__':
	"""
	Run a shell-like interpreter if no arguments are passed
	"""

	try:
		############## Argument Passing Interpreter ###############

		prog = sys.argv[1]		
		verbose = False
		init = False
		init_config = ""
		options, remainder = getopt.getopt(sys.argv[2:], \
							'i:v', ['initial=', 'verbose',])
		for opt, arg in options:
			#print opt + " " + arg
			if opt in ('-i', '--initial'):
				init = True
				init_config = arg
			elif opt in ('-v', '--verbose'):
				verbose = True


		lines = []
		try:
			with open(prog) as input_file:
				for i, line in enumerate(input_file):
					lines.append(line)
		except IOError as e:
			print str(e)


		lexer = Lexer(line)
		interpreter = Interpreter(lexer, verbose)
	
		for line in lines:
			lexer = update(line)
			interpreter = update(lexer)
			result = interpreter.expr()
			print(result)

	except IndexError:
		################# Interactive Interpreter ##################

		lexer = Lexer()
		interpreter = Interpreter(lexer)
	
		while True:
			try:
				line = raw_input('xpl> ')
			except EOFError:
				break

			if not line:
				continue

			lexer.update(line)
			interpreter.update(lexer)
			result = interpreter.expr()
			print(result)

	
