class Transicion:
	def __init__ (self, estado_siguiente, simbolo_min, simbolo_max = ''):
		self.simbolo_min = simbolo_min
		if (len (simbolo_max) == 0):
			self.simbolo_max = simbolo_min
		else:
			self.simbolo_max = simbolo_max
		self.estado_siguiente = estado_siguiente

	def get_simbolo_min (self):
		return self.simbolo_min

	def get_simbolo_max (self):
		return self.simbolo_max