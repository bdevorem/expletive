from token import Token

EOF =  'EOF'
SYMBOL, L_BRACKET, R_BRACKET = 'SYMBOL', 'L_BRACKET', 'R_BRACKET'
ALPH, HALT, RULE = 'ALPH', 'HALT', 'RULE'
INPUT, TITLE, COMMENT = 'INPUT', 'TITLE', 'COMMENT'

class Lexer(object):
	def __init__(self, text):
		self.text = text
		self.pos = 0
		self.current_token = None
		self.current_char = self.text[self.pos]
		self.symbol = ''
   
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

	def _title(self):
		self.symbol = self._sym()

		if self.symbol == '+|+13':
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

			#TODO: refactor to reduce total if statement count
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

			if self.current_char == '+':
				if self._title():
					return Token(TITLE, "+|+13")
				else:
					return Token(SYMBOL, self.symbol)

			if self.current_char is not None:
				return Token(SYMBOL, self._sym())

		return Token(EOF, None)

