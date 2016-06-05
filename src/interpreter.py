#!/usr/bin/env python2
# xpl interpreter
# Breanna Devore-McDonald
# Interpreter idea: https://ruslanspivak.com/lsbasi-part1/

from token import Token
from lexer import Lexer

EOF =  'EOF'
SYMBOL, L_BRACKET, R_BRACKET = 'SYMBOL', 'L_BRACKET', 'R_BRACKET'
ALPH, HALT, RULE = 'ALPH', 'HALT', 'RULE'
INPUT, TITLE, COMMENT = 'INPUT', 'TITLE', 'COMMENT'

class Interpreter(object):
	def __init__(self, lexer):
		self.lexer = lexer
		self.current_token = self.lexer.get_next_token()

		self.alphabet = set()
		self.halt = ''
		self.rules = {}
		self.title = ''

	def eat(self, token_type):
		"""
		Compares current token type with parameter token type
		If they're equal, eat
		Else, raise exception
		"""
		#print "current:" + self.current_token.type
		#print "parameter:" + token_type
		if self.current_token.type == token_type:
			self.current_token = self.lexer.get_next_token()
		else:
			raise Exception("Parsing error")
	
	#TODO: add support for {} construct
	#TODO: add complete grammar rules
	#TODO: if halting sym in alph, default to len<2
	#TODO: implement queue
	def expr(self):
		"""
		expr -> ALPH | HALT | RULE | INPUT | TITLE | COMMENT
		ALPH -> @|?h SYMBOLS
		HALT -> h@|+ SYMBOL
		RULE -> r#|3 SYMBOL SYMBOLS
		INPUT -> n?#+ SYMBOLS
		TITLE -> +|+13 SYMBOLS		
		COMMENT -> *SYMBOLS
	
		SYMBOL -> SYMBOL | epsilon
		SYMBOLS -> SYMBOL SYMBOL | epsilon

		policy: ALPH | HALT | RULE | INPUT | TITLE | COMMENT | NEWLINE
		mapping: corresponding grammar rules
        """
		
		# get policy
		# can be ALPH, HALT, RULE
		policy = self.current_token
		if policy.type == ALPH:
			self.eat(ALPH)
		elif policy.type == HALT:
			self.eat(HALT)
		elif policy.type == RULE:
			self.eat(RULE)
		elif policy.type == TITLE:
			self.eat(TITLE)

		# get mappings
		if policy.type == RULE:
			read = self.current_token
			self.eat(SYMBOL)
			
			self.rules[read] = []

		while True:
			mapping = self.current_token
			if mapping.value == None:
				self.eat(EOF)
				break
			else:
				self.eat(SYMBOL)

				#TODO: allow range construct
				if policy.type == ALPH:
					self.alphabet.add(mapping)
				elif policy.type == HALT:
					# as declared in lang spec, if more than
					# one halt sym is declared, go w latest change
					self.halt = mapping
				elif policy.type == RULE:
					self.rules[read].append(mapping)

		for key, val in self.rules.iteritems():
			print 'key: ' + str(key) + ', val: ' + str(val)

		return self.halt

if __name__ == '__main__':

	while True:
		try:
			text = raw_input('xpl> ')
		except EOFError:
			break

		if not text:
			continue

		lexer = Lexer(text)
		intr = Interpreter(lexer)
		result = intr.expr()
		print(result)

