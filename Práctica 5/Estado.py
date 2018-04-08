from Transicion import *

class Estado:
	#Id para cada uno de los estados creados
	id_global = 0
	
	def __init__ (self):
		#Se le asigna un id único a cada estado creado
		self.id_estado = Estado.id_global
		#El id incrementa después de ser asignado al estado
		Estado.id_global = Estado.id_global + 1
		#Siempre que se crea un estado, no es de aceptación (si si lo es, hay que cambiar la bandera a True)
		self.Estado_Aceptacion = False
		#El conjunto de transiciones se inicializa como un conjunto vacío
		self.Transiciones = set ()
		#Token para los estados de aceptación
		self.Token = -1

	def AddTransition (self, estado_siguiente, simbolo_min, simbolo_max = ''):
		#Si solo se ingresa un simbolo
		if (len (simbolo_max) == 0):
			(self.Transiciones).add (Transicion (estado_siguiente, simbolo_min))
		#Si se ingresa un rango
		else:
			(self.Transiciones).add (Transicion (estado_siguiente, simbolo_min, simbolo_max))