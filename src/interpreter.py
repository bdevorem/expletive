#!/usr/bin/env python2
# xpl interpreter
# Breanna Devore-McDonald
# Interpreter idea: https://ruslanspivak.com/lsbasi-part1/

from token import Token

EOF =  'EOF'
SYMBOL, L_BRACKET, R_BRACKET = 'SYMBOL', 'L_BRACKET', 'R_BRACKET'
ALPH = 'ALPH'

class Interpreter(object):
	def __init__(self, text):
		self.text = text
		self.pos = 0
		self.current_token = None
		self.current_char = self.text[self.pos]
		self.symbol = ''
		
		self.alphabet = []

	def advance(self):
		"""
		Advance the position pointer and set new current_char
		"""

		self.pos += 1
		if self.pos > len(self.text) - 1:
			self.current_char = None
		else:
			self.current_char = self.text[self.pos]

	def alph(self):
		"""
		Called when current_symbol == '@'
		Cycles through chars until a space is found, if
			resulting string == "@|?h", return True
			Else, the string is of type SYMBOL, return False
		"""
		self.symbol = ''
		while self.current_char is not None \
				and	self.current_char.isspace() is False:
			self.symbol += self.current_char
			self.advance()

		if self.symbol == '@|?h':
			return True
		else:
			return False	

	def sym(self):
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
				if self.alph():
					return Token(ALPH, "@|?h")
				else:
					return Token(SYMBOL, self.symbol)	

			if self.current_char is not None:
				return Token(SYMBOL, self.sym())

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
	def expr(self):
		"""
		expr -> ALPH SYMBOL
		SYMBOL -> SYMBOL | epsilon

		policy: ALPH | HALT | RULE | INPUT | TITLE | COMMENT | NEWLINE
		mapping: corresponding grammar rules
        """
		self.current_token = self.get_next_token()

		# start with ALPH
		policy = self.current_token
		self.eat(ALPH)

		while True:
			mapping = self.current_token
			if mapping.value == None:
				self.eat(EOF)
				break
			else:
				self.eat(SYMBOL)
				self.alphabet.append(mapping)

		return self.alphabet

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

