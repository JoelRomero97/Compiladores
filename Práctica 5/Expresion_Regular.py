from AFN import *
from Tokens import *

class Expresion_Regular:

	def __init__ (self, Lexic):
		self.Lexic = Lexic

	def E (self, f):
		if (self.T (f)):
			if (self.Ep (f)):
				return True
		return False

	def Ep (self, f):
		f1 = AFN ()
		token = self.Lexic.get_token ()
		if (token == Tokens.OR):
			if (self.T (f1)):
				f.Unir_AFN (f1)
				if (self.Ep (f)):
					return True
			return False
		self.Lexic.return_token ()
		return True

	def T (self, f):
		if (self.C (f)):
			if (self.Tp (f)):
				return True
		return False

	def Tp (self, f):
		f1 = AFN ()
		token = self.Lexic.get_token ()
		if (token == Tokens.CONC):
			if (self.C (f1)):
				f.Concatenar_AFN (f1)
				if (self.Tp (f)):
					return True
			return False
		self.Lexic.return_token ()
		return True

	def C (self, f):
		if (self.F (f)):
			if (self.Cp (f)):
				return True
		return False

	def Cp (self, f):
		token = self.Lexic.get_token ()
		if (token == Tokens.MAS):
			f.Cerradura_Positiva ()
		elif (token == Tokens.PROD):
			f.Cerradura_Kleene ()
		elif (token == Tokens.OPC):
			f.Cerradura_Opcional ()
		else:
			self.Lexic.return_token ()
			return True
		if (self.Cp (f)):
			return True
		return False

	def F (self, f):
		token = self.Lexic.get_token ()
		if (token == Tokens.PARI):
			if (self.E (f)):
				token = self.Lexic.get_token ()
				if (token == Tokens.PARD):
					return True
			return False
		elif (token == Tokens.SIMB):
			f = AFN (self.Lexic.lexema [0])
			return True
		elif (token == Tokens.CORI):
			token = self.Lexic.get_token ()
			if (token == Tokens.SIMB):
				simb1 = self.Lexic.lexema [0]
				token = self.Lexic.get_token ()
				if (token == Tokens.GUION):
					token = self.Lexic.get_token ()
					if (token == Tokens.SIMB):
						simb2 = self.Lexic.lexema [0]
						token = self.Lexic.get_token ()
						if (token == Tokens.CORD):
							if (simb2 > simb1):
								f = AFN (simb1 + '-' + simb2)
		elif (token == Tokens.DIAG):
			token = self.Lexic.get_token ()
			simbolos = {10:'|', 20:'&', 30:'+', 40:'*', 50:'?', 60:'(', 70:')', 80:'[', 90:'-', 100:']', 110:'\\'}
			for i in range (10, 120, 10):
				if (token == i):
					f = AFN (simbolos [i])
		return False