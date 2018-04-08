class AFD:
	def __init__ (self):
		#El conjunto del alfabeto se inicializa como un conjunto vacío
		self.Alfabeto = set ()
		#La tabla de transiciones se crea como una lista vacía
		self.Tabla = []

	def get_tabla (self):
		for fila in (self.Tabla):
			matrix = ''
			for columna in fila:
				matrix += str ((self.Tabla) [(self.Tabla).index (fila)][fila.index (columna)]) + '\t'
			print (matrix)

	def get_estados (self):
		a = set ()
		for e in self.Estados:
			a.add (e.id_estado)
		return a

	def get_estado_inicial (self):
		a = set ()
		a.add ((self.Estado_Inicial).id_estado)
		return a

	def get_edos_aceptacion (self):
		a = set ()
		for e in self.Estados_Aceptacion:
			a.add (e.id_estado)
		return a