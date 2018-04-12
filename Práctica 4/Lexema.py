import re

class Lexema:

	def __init__ (self, cadena):
		self.cadena = cadena
		self.token = -1
		self.pila = []
		self.indIniLex=0
		self.lexema = ""
		self.carAct = 0

	def getToken (self):
		if (self.carAct == len (self.cadena)):
			self.lexema = ""
			return 0
		if (self.cadena [self.carAct] == '+'):
			self.indIniLex = self.carAct
			self.token = 10
			self.lexema = self.cadena [self.carAct]
			self.carAct = self.carAct + 1

		elif (self.cadena [self.carAct] == '-'):
			self.indIniLex = self.carAct
			self.token = 20
			self.lexema = self.cadena [self.carAct]
			self.carAct = self.carAct + 1

		elif (self.cadena [self.carAct] == '*'):
			self.indIniLex = self.carAct
			self.token = 30
			self.lexema = self.cadena [self.carAct]
			self.carAct = self.carAct + 1

		elif (self.cadena [self.carAct] == '/'):
			self.indIniLex = self.carAct
			self.token = 40
			self.lexema = self.cadena [self.carAct]
			self.carAct = self.carAct + 1

		elif (self.cadena [self.carAct] == '('):
			self.indIniLex = self.carAct
			self.token = 50
			self.lexema = self.cadena [self.carAct]
			self.carAct = self.carAct + 1

		elif (self.cadena [self.carAct] == ')'):
			self.indIniLex = self.carAct
			self.token = 60
			self.lexema = self.cadena [self.carAct]
			self.carAct = self.carAct + 1
		elif (re.match ("\d", self.cadena [self.carAct])):
			self.indIniLex = self.carAct
			while (re.match("[\d|\.]", self.cadena [self.carAct])):
				self.carAct = self.carAct + 1
				if (self.carAct >= len (self.cadena)):
					break;
			aux=self.cadena [self.indIniLex:self.carAct]
			if (re.match ("[\d+(\.d+)?]", aux)):
				self.token = 70
				self.lexema = aux
		else:
			return -1
		self.pila.append (self.indIniLex)
		return self.token


	def RegresarToken(self):
		self.carAct = self.pila.pop()