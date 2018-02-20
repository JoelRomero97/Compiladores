import os
import sys

class AFN:
	def __init__ (self, simbolo):
		#Si no se recibe ningun simbolo, se inicializa todo a vacío
		if (len (simbolo) == 0):
			#Inicialización del estado inicial a 'null'
			self.Estado_Inicial = None
			#El conjunto del alfabeto se inicializa como un conjunto vacío
			self.Alfabeto = set ()
			#El conjunto de estados se inicializa como un conjunto vacío
			self.Estados = set ()
			#El conjunto de estados de aceptación se inicializa como un conjunto vacío
			self.Estados_Aceptacion = set ()
		#Si se recibe un simbolo, se crea un AFN básico
		else:
			#Se crea un estado inicial de tipo Estado como atributo del AFN
			self.Estado_Inicial = Estado ()
			#Se crea un estado final de tipo Estado
			Estado_Final = Estado ()
			#Se cambia el estado de la bandera a true para saber que es estado final
			Estado_Final.Estado_Aceptacion = True
			#El conjunto del alfabeto se inicializa como un conjunto vacío
			self.Alfabeto = set ()
			#Se agrega el símolo al alfabeto del AFN (si es un rango, se añaden todos los simbolos)
			if (len (simbolo) == 1):
				self.Alfabeto.add (simbolo)
			else:
				for i in range (ord (simbolo [0]), ord (simbolo [2]) + 1):
					self.Alfabeto.add (chr (i))
			#El conjunto de estados se inicializa como un conjunto vacío
			self.Estados = set ()
			#El conjunto de estados de aceptación se inicializa como un conjunto vacío
			self.Estados_Aceptacion = set ()
			#Se agrega una transición del estado inicial al estado final con el caracter 'simbolo'
			(self.Estado_Inicial).AddTransition (simbolo, Estado_Final)
	
	def Unir_AFN (self, AFN_2):
		Nuevo_Inicio = Estado ()
		Nuevo_Fin = Estado ()
		Nuevo_Inicio.AddTransition ('\0', self.Estado_Inicial)
		Nuevo_Inicio.AddTransition ('\0', AFN_2.Estado_Inicial)

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

	def AddTransition (self, simbolo, estado_siguiente):
		#Si solo se ingresa un simbolo
		if (len (simbolo) == 1):
			(self.Transiciones).add (Transicion (simbolo, simbolo, estado_siguiente))
		#Si se ingresa un rango
		else:
			(self.Transiciones).add (Transicion (simbolo [0], simbolo [2], estado_siguiente))

class Transicion:
	def __init__ (self, simbolo_min, simbolo_max, estado_siguiente):
		self.simbolo_min = simbolo_min
		self.simbolo_max = simbolo_max
		self.estado_siguiente = estado_siguiente

	def get_simbolo_min (self):
		return self.simbolo_min

	def get_simbolo_max (self):
		return self.simbolo_max

def Crear ():
	os.system ("cls")
	#Simbolo para crear el AFN Básico
	simbolo = input ('\n\n\n¿Con qué simbolo deseas crear el AFN?\t')
	#Se crea el AFN con el símbolo seleccionado por el usuario
	Automata = AFN (simbolo)
	print ('\n\n\nAutomata básico con símbolo \'' + simbolo + '\' creado correctamente.\n\n\n')
	print ('Alfabeto: ', Automata.Alfabeto)
	num_automata = int (input ('¿En qué posición deseas guardar el autómata (1 / 2 / 3)?\t')) - 1
	#Guardamos el automata creado en una de las 3 posiciones que se tienen
	Automatas [num_automata] = Automata

def Unir ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata 1:\t')) - 1
	automata2 = int (input ('\n\n\nSelecciona el autómata 2:\t')) - 1
	#Cuando ya regrese el automata, descomentar la siguiente linea y eliminar la que sigue
	#nuevo_AFN = (Automatas [automata1]).Unir_AFN ((Automatas [automata2]))
	(Automatas [automata1]).Unir_AFN ((Automatas [automata2]))

def Concatenar ():
	os.system ("cls")

def Positiva ():
	os.system ("cls")

def Kleene ():
	os.system ("cls")

def Opcional ():
	os.system ("cls")

def Validacion ():
	os.system ("cls")

def Salir ():
	for i in range (len (Automatas)):
		Automatas.pop ()
	sys.exit ()

def Menu ():
	#Diccionario para seleccionar la opcion que desee el usuario
	funciones = {1:Crear, 2:Unir, 3:Concatenar, 4:Positiva, 5:Kleene, 6:Opcional, 7:Validacion, 8:Salir}
	option = 1
	while option < 8 and option > 0:
		os.system ("cls")
		print ('\n\n')
		print ('\t\tMENÚ\n\n')
		print ('1. Crear AFN básico')
		print ('2. Unir AFN\'s')
		print ('3. Concatenar AFN\'s')
		print ('4. Operación cerradura +')
		print ('5. Operación cerradura *')
		print ('6. Operación ?')
		print ('7. Validar cadena')
		print ('8. Salir\n\n\n')
		option = int (input ('Selecciona una opción:\t'))
		#Llamar a la función según la opción seleccionada
		funciones [option] ()

#Lista de 3 elementos para guardar los automatas creados por el usuario
Automatas = [1, 2, 3]

Menu ()