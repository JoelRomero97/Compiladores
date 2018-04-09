class Lexema:

	def __init__ (self, expresion):
		self.expresion = expresion
		self.token = -1
		self.pila = []
		self.indice_inicio_lexema = 0
		self.lexema = ''
		self.caracter_actual = 0

	def get_token (self):
		if self.caracter_actual == len (self.expresion):
			self.lexema = ''
			self.pila.append (self.caracter_actual)
			return 0
		#PIPE (OR)
		if self.expresion [self.caracter_actual] == '|':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 10
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#AMPERSAND (CONCATENACIÓN)
		elif self.expresion [self.caracter_actual] == '&':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 20
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#MAS (CERRADURA POSITIVA)
		elif self.expresion [self.caracter_actual] == '+':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 30
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#ASTERISCO (CERRADURA DE KLEENE)
		elif self.expresion [self.caracter_actual] == '*':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 40
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#INTERROGACIÓN (CERRADURA OPCIONAL)
		elif self.expresion [self.caracter_actual] == '?':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 50
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#PARÉNTESIS IZQUIERDO
		elif self.expresion [self.caracter_actual] == '(':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 60
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#PARÉNTESIS DERECHO
		elif self.expresion [self.caracter_actual] == ')':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 70
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#CORCHETE IZQUIERDO
		elif self.expresion [self.caracter_actual] == '[':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 80
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#GUIÓN
		elif self.expresion [self.caracter_actual] == '-':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 90
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#CORCHETE DERECHO
		elif self.expresion [self.caracter_actual] == ']':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 100
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#DIAGONAL INVERTIDA
		elif self.expresion [self.caracter_actual] == '\\':
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 110
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		#CUALQUIER OTRO SÍMBOLO
		else:
			self.indice_inicio_lexema = self.caracter_actual
			self.token = 120
			self.lexema = self.expresion [self.caracter_actual]
			self.caracter_actual = self.caracter_actual + 1
		self.pila.append (self.indice_inicio_lexema)
		return self.token

	def return_token (self):
		self.caracter_actual = self.pila.pop ()