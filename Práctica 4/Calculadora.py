from Tokens import *

class Calculadora:

	def __init__(self, lexic):
		self.lexic = lexic

	def E (self, v):
		if (self.T (v)):
			if (self.Ep (v)):
				return True
		return False

	def Ep (self, v):
		v1 = [0, '', ''] 
		token = self.lexic.getToken()
		if (token == Tokens.mas or token == Tokens.menos):
			operador = (self.lexic).lexema
			if (self.T (v1)):
				v[0] = v [0] + (v1[0] if token == Tokens.mas else -v1[0])
				v [1] = operador +' ' + v [1]+ ' ' + v1 [1]
				v [2] = v [2] + ' ' + v1 [2] + ' ' + operador
				if (self.Ep (v)):
					return True
			return False
		self.lexic.RegresarToken ()
		return True

	def T (self, v):
		if (self.F (v)):
			if (self.Tp (v)):
				return True
		return False

	def Tp (self, v):
		v1 = [0, '', ''] 
		token = (self.lexic).getToken ()
		if (token == Tokens.prod or token == Tokens.div):
			operador = self.lexic.lexema
			if (self.F (v1)):
				v[0] = v [0] * (v1[0] if token == Tokens.prod else 1.0/v1[0])
				v[1] = operador + ' ' + v [1] + ' ' + v1 [1]
				v[2] = v [2] + ' ' + v1 [2] + ' ' + operador
				if (self.Tp (v)):
					return True
			return False
		(self.lexic).RegresarToken()
		return True

	def F (self, v):
		token = (self.lexic).getToken ()
		if (token == Tokens.parI):
			if (self.E (v)):
				token = (self.lexic).getToken ()
				if (token == Tokens.parD):
					return True
			return False
		elif (token == Tokens.num):
			v [0] = float (self.lexic.lexema)
			v [1] = v[2] = self.lexic.lexema
			return True
		return False