#!/usr/bin/env python
# xpl interpreter
# Breanna Devore-McDonald
# Interpreter idea: https://ruslanspivak.com/lsbasi-part1/

from token import Token
from lexer import Lexer
import Queue

EOF =  'EOF'
SYMBOL, L_BRACKET, R_BRACKET = 'SYMBOL', 'L_BRACKET', 'R_BRACKET'
ALPH, HALT, RULE = 'ALPH', 'HALT', 'RULE'
INPUT, TITLE, COMMENT = 'INPUT', 'TITLE', 'COMMENT'


class Interpreter(object):
	def __init__(self, lexer, verbose=False, config=None):
		self.lexer = lexer
		self.current_token = self.lexer.get_next_token()

		self.alphabet = set()
		self.halt = ''
		self.rules = {}
		self.title = ''
		self.tape = Queue.Queue()
		self.verbose = verbose
		
		if config is not None:
			self.config_tape(config)

	def config_tape(self, config):
		pass

	def update(self, lexer):
		self.lexer = lexer
		self.current_token = self.lexer.get_next_token()

	def _verbose(self):
		for elem in list(self.tape.queue):
			print elem._value,
		print "\n----------------\n"

	#TODO: maybe make this callable from the interactive
	#		interpreter? To allow for user debugging?
	def test(self):
		print "Test"
		print "----------------"
		
		print "Title = "
		print self.title
		print "----------------"

		print "Alph = "
		for sym in self.alphabet:
			print sym,
		print "----------------"

		print "Halt = "
		print str(self.halt)
		print "----------------"

		print "Rules = "
		for key, val in self.rules.iteritems():
			try:
				print str(key._value) + " --> " + str(val._value),
			except:
				print str(key) + " --> " + str(val)
		print "----------------"

		print "Input = "
		for elem in list(self.tape.queue):
			print elem

	def operate(self):
		"""
		For now, as soon as initial tape is set, start 
		performing the operations as declared by user
		with the r#|3 construct
		"""
		while not self.tape.empty():
			#if self.verbose:
			self._verbose()

			sym = self.tape.get()

			if sym == self.halt:
				break
			if self.tape.qsize() < 2:
				break
		
			if sym in self.rules:
				for elem in self.rules[sym]:
					if elem is not " ":
						self.tape.put(elem)
			sym = self.tape.get()

		for elem in list(self.tape.queue):
			print elem,

	def eat(self, token_type):
		"""
		Compares current token type with parameter token type
		If they're equal, eat
		Else, raise exception
		"""
		#print "current:" + self.current_token.type
		#print "parameter:" + token_type
		if self.current_token._type == token_type:
			self.current_token = self.lexer.get_next_token()
		else:
			raise Exception("Parsing error")
	
	#TODO: add support for {} construct
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
		#TODO: refactor to lower if statement count
		policy = self.current_token
		if policy._type == ALPH:
			self.eat(ALPH)
		elif policy._type == HALT:
			self.eat(HALT)
		elif policy._type == RULE:
			self.eat(RULE)
		elif policy._type == TITLE:
			self.eat(TITLE)
		elif policy._type == COMMENT:
			self.eat(COMMENT)
			return
		elif policy._type == INPUT:
			self.eat(INPUT)

		# get mappings
		if policy._type == RULE:
			read = self.current_token
			self.eat(SYMBOL)
			
			self.rules[read] = []

		while True:
			mapping = self.current_token
			if mapping._value == None:
				self.eat(EOF)
				break
			else:
				self.eat(SYMBOL)

				#TODO: allow range construct
				if policy._type == ALPH:
					self.alphabet.add(mapping)
				elif policy._type == HALT:
					# as declared in lang spec, if more than
					# one halt sym is declared, go w latest change
					self.halt = mapping
				elif policy._type == RULE:
					self.rules[read].append(mapping)
				elif policy._type == TITLE:
					self.title = self.title + mapping._value + ' '
				elif policy._type == INPUT:
					self.tape.put(mapping)

		#TODO: add a command to start operating?
		#		For now, start operating as soon as initial tape
		#		is set
		if policy._type == INPUT:
			self.operate()	
	
		#self.test()
