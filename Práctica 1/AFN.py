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
			#El conjunto de estados se inicializa como un conjunto vacío
			self.Estados = set ()
			#El conjunto de estados de aceptación se inicializa como un conjunto vacío
			self.Estados_Aceptacion = set ()
			#Se agrega una transición del estado inicial al estado final con el caracter 'simbolo'
			#Estado_Inicial.AddTransition (simbolo, Estado_Final)

class Estado:
	def __init__ (self):
		#Se le asigna un id único a cada estado creado
		self.id_estado = id_global
		#El id incrementa después de ser asignado al estado
		id_global + 1
		#Siempre que se crea un estado, no es de aceptación (si si lo es, hay que cambiar la bandera a True)
		self.Estado_Aceptacion = False
		#El conjunto de transiciones se inicializa como un conjunto vacío
		self.transiciones = set ()

class Transiciones:
	def __init__ (self, edo_salida, simbolo_min, simbolo_max):
		self.simbolo_min = simbolo_min
		if (len (simbolo_max) == 0):
			self.simbolo_max = simbolo_min
		else:
			self.simbolo_max = simbolo_max
		self.edo_salida = edo_salida

	def get_simbolo_min (self):
		return self.simbolo_min

	def get_simbolo_max (self):
		return self.simbolo_max

def Crear ():
	os.system ("cls")
	simbolo = input ('\n\n\n¿Con qué simbolo deseas crear el AFN?\t')
	Automata = AFN (simbolo)
	print ('\n\n\nAutomata básico con símbolo \'' + simbolo + '\' creado correctamente.\n\n\n')
	num_automata = int (input ('¿En qué posición deseas guardar el autómata (1 / 2 / 3)?\t')) - 1
	Automatas.insert (num_automata, Automata)

def Unir ():
	os.system ("cls")

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
	sys.exit ()

def Menu ():
	os.system ("cls")
	#Diccionario para seleccionar la opcion que desee el usuario
	funciones = {1:Crear, 2:Unir, 3:Concatenar, 4:Positiva, 5:Kleene, 6:Opcional, 7:Validacion, 8:Salir}
	option = 1
	while option < 8 and option > 0:
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

#Main
id_global = 0
#Lista vacía para guardar los automatas creados por el usuario
Automatas = []

Menu ()