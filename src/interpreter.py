#!/usr/bin/env python2
# xpl interpreter
# Breanna Devore-McDonald
# Interpreter idea: https://ruslanspivak.com/lsbasi-part1/

from token import Token

EOF =  'EOF'
SYMBOL, L_BRACKET, R_BRACKET = 'SYMBOL', 'L_BRACKET', 'R_BRACKET'
ALPH, HALT, RULE = 'ALPH', 'HALT', 'RULE'

class Interpreter(object):
	def __init__(self, text):
		self.text = text
		self.pos = 0
		self.current_token = None
		self.current_char = self.text[self.pos]
		self.symbol = ''
		
		self.alphabet = set()
		self.halt = ''
		self.rules = {}

	def advance(self):
		"""
		Advance the position pointer and set new current_char
		"""

		self.pos += 1
		if self.pos > len(self.text) - 1:
			self.current_char = None
		else:
			self.current_char = self.text[self.pos]

	def _alph(self):
		"""
		Called when current_symbol == '@'
		Cycles through chars until a space is found, if
			resulting string == "@|?h", return True
			Else, the string is of type SYMBOL, return False
		"""
		self.symbol = self._sym()

		if self.symbol == '@|?h':
			return True
		else:
			return False

	def _halt(self):
		self.symbol = self._sym()

		if self.symbol == 'h@|+':
			return True
		else:
			return False

	def _rule(self):
		self.symbol = self._sym()

		if self.symbol == 'r#|3':
			return True
		else:
			return False

	def _sym(self):
		"""
		Called when current symbol is not space, or "@"
		Cycles through all non-space, non-EOF chars and
			returns that string		
		"""

		self.symbol = ''
		while self.current_char is not None \
				and self.current_char.isspace() is False:
			self.symbol += self.current_char
			self.advance()

		return self.symbol

	def get_next_token(self):
		"""
		"""	
		while self.current_char is not None:
			if self.current_char.isspace():
				while self.current_char is not None \
						and self.current_char.isspace():
					self.advance()
				continue

			if self.current_char == '@':
				if self._alph():
					return Token(ALPH, "@|?h")
				else:
					return Token(SYMBOL, self.symbol)	

			if self.current_char == 'h':
				if self._halt():
					return Token(HALT, "h@|+")
				else:
					return Token(SYMBOL, self.symbol)

			if self.current_char == 'r':
				if self._rule():
					return Token(RULE, "r#|3")
				else:
					return Token(SYMBOL, self.symbol)

			if self.current_char is not None:
				return Token(SYMBOL, self._sym())

		return Token(EOF, None)

	def eat(self, token_type):
		"""
		Compares current token type with parameter token type
		If they're equal, eat
		Else, raise exception
		"""
		#print "current:" + self.current_token.type
		#print "parameter:" + token_type
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			raise Exception("Parsing error")
	
	#TODO: add support for {} construct
	#TODO: add complete grammar rules
	#TODO: if halting sym in alph, default to len<2
	#TODO: implement queue
	def expr(self):
		"""
		expr -> ALPH SYMBOL
		SYMBOL -> SYMBOL | epsilon

		policy: ALPH | HALT | RULE | INPUT | TITLE | COMMENT | NEWLINE
		mapping: corresponding grammar rules
        """
		self.current_token = self.get_next_token()

		# get policy
		# can be ALPH, HALT, RULE
		policy = self.current_token
		if policy.type == ALPH:
			self.eat(ALPH)
		elif policy.type == HALT:
			self.eat(HALT)
		elif policy.type == RULE:
			self.eat(RULE)

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

        intr = Interpreter(text)
        result = intr.expr()
        print(result)

