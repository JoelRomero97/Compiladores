class Lexic:
	def __init__ (self, AFD, cadena):
		#Se inicializa la cadena
		self.cadena = cadena
		#Se obtiene la tabla del AFD
		self.Tabla = AFD.Tabla
		#Se obtiene el alfabeto
		self.Alfabeto = AFD.Alfabeto

	def get_token (self):
		#Si se lee el final de la cadena
		if (len (self.cadena) == 0):
			return 0, self.cadena
		else:
			#Se obtiene el estado actual y la posicion de caracter
			token, posicion = self.validar_cadena (self.cadena)
			if (token < 0):
				posicion = posicion + 1
			#El lexema será toda la cadena hasta la posicion obtenida
			lexema = self.cadena [:posicion]
			#Se actualiza la cadena desde la posicion obtenida hasta el final
			self.cadena = self.cadena [posicion:]
			return token, lexema

	def validar_cadena (self, cadena):
		estado_actual = 0
		posicion = 0
		token = 0

		#Se recorre la cadena
		for caracter in cadena:
			#Si se lee un caracter que no sea reconocido por el AFD
			if (caracter not in self.Alfabeto):
				return -1, posicion
			else:
				num_simbolo = (list (self.Alfabeto)).index (caracter)
				#Obtenemos toda la fila del respectivo estado actual
				fila = self.Tabla [estado_actual + 1]
				#Obtenemos la transicion con ese simbolo a partir de la tabla
				estado_actual = fila [num_simbolo]
				#Obtenemos el token de ese estado
				token = fila [len (fila) - 1]
				if (estado_actual == -1):
					return token, posicion
			posicion = posicion + 1
		#Obtenemos toda la fila del respectivo estado actual
		fila = self.Tabla [estado_actual + 1]
		#Obtenemos el token de ese estado
		token = fila [len (fila) - 1]
		return token, posicion