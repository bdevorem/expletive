# Breanna Devore-McDonald

import hashlib

EOF = 'EOF'
SYMBOL, L_BRACKET, R_BRACKET = 'SYMBOL', 'L_BRACKET', 'R_BRACKET'
ALPH, HALT, RULE = 'ALPH', 'HALT', 'RULE'
INPUT, TITLE = 'INPUT', 'TITLE'

class Token(object):
	def __init__(self, _type, _value):
		# SYMBOL.value can be multiple chars\
		self._type = _type
		self._value = _value

	def __eq__(self, other):
		if type(other) is type(self):
			return self._value == other._value
		else:
			return False

	def __str__(self):
		return 'Token({typ}, {value})'.format(
			typ=self._type,
			value=self._value)

	def __hash__(self):
		return int(hashlib.sha1(str(self._value)).hexdigest(), base=16)
#		return hash(str(self._value))

#	def __getattr__(self, name):  
#		return getattr(self._value, name)
