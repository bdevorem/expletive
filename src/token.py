# Breanna Devore-McDonald

EOF = 'EOF'
SYMBOL, L_BRACKET, R_BRACKET = 'SYMBOL', 'L_BRACKET', 'R_BRACKET'
ALPH, HALT = 'ALPH', 'HALT'

class Token(object):
    def __init__(self, type, value):
		# SYMBOL.value can be multiple chars
        self.type = type
        self.value = value

    def __str__(self):
        """
		String representation of the class instance.
        """

        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

