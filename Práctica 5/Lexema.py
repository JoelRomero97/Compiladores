class Lexema:

	def __init__ (self, cadena):
		self.cadena = cadena
		self.token = -1
		self.pila = []
		self.indice_inicio_lexema = 0
		self.lexema = ''
		self.caracter_actual = 0

	def getToken(self):
		if self.caracter_actual == len(self.cadena):
			self.lexema=""
			return 0
		if self.cadena[self.caracter_actual] == '+':
			self.indice_inicio_lexema=self.caracter_actual
			self.token=10
			self.lexema=self.cadena[self.caracter_actual]
			self.caracter_actual=self.caracter_actual+1

		elif self.cadena[self.caracter_actual] == '-':
			self.indice_inicio_lexema=self.caracter_actual
			self.token=20
			self.lexema=self.cadena[self.caracter_actual]
			self.caracter_actual=self.caracter_actual+1

		elif self.cadena[self.caracter_actual] == '*':
			self.indice_inicio_lexema=self.caracter_actual
			self.token=30
			self.lexema=self.cadena[self.caracter_actual]
			self.caracter_actual=self.caracter_actual+1

		elif self.cadena[self.caracter_actual] == '/':
			self.indice_inicio_lexema=self.caracter_actual
			self.token=40
			self.lexema=self.cadena[self.caracter_actual]
			self.caracter_actual=self.caracter_actual+1

		elif self.cadena[self.caracter_actual] == '(':
			self.indice_inicio_lexema=self.caracter_actual
			self.token=50
			self.lexema=self.cadena[self.caracter_actual]
			self.caracter_actual=self.caracter_actual+1

		elif self.cadena[self.caracter_actual] == ')':
			self.indice_inicio_lexema=self.caracter_actual
			self.token=60
			self.lexema=self.cadena[self.caracter_actual]
			self.caracter_actual=self.caracter_actual+1
		elif re.match("\d",self.cadena[self.caracter_actual]):
			self.indice_inicio_lexema=self.caracter_actual
			while re.match("[\d|\.]",self.cadena[self.caracter_actual]):
				self.caracter_actual=self.caracter_actual+1
				if self.caracter_actual >= len(self.cadena):
					break;
			aux=self.cadena[self.indice_inicio_lexema:self.caracter_actual]
			if re.match("[\d+(\.d+)?]",aux):
				self.token=70
				self.lexema=aux
		else:
			return -1
		self.pila.append(self.indice_inicio_lexema)
		return self.token


	def RegresarToken(self):
		self.caracter_actual = self.pila.pop()