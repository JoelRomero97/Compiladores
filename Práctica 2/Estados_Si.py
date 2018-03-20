class Estados_Si:
	#Id global para los conjuntos de estados
	id_global_si = 0

	def __init__ (self, Estados):
		#Se le asigna un id único a cada estado creado
		self.id_estado = Estados_Si.id_global_si
		#El id incrementa después de ser asignado al estado
		Estados_Si.id_global_si = Estados_Si.id_global_si + 1
		#El conjunto de estados se inicializa con el conjunto mandado como parametro
		self.Estados = Estados

	def get_estados (self):
		a = set ()
		for e in self.Estados:
			a.add (e.id_estado)
		return a