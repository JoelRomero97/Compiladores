import os
import sys

class AFN:
	def __init__ (self, simbolo = ''):
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
			#Se agregan los estados al conjunto de Estados del AFN
			self.Estados.add (self.Estado_Inicial)
			self.Estados.add (Estado_Final)
			#El conjunto de estados de aceptación se inicializa como un conjunto vacío
			self.Estados_Aceptacion = set ()
			#Se agrega el estado final del AFN como un estado de aceptación
			self.Estados_Aceptacion.add (Estado_Final)
			#Se agrega una transición del estado inicial al estado final con el caracter 'simbolo'
			(self.Estado_Inicial).AddTransition (Estado_Final, simbolo)
	
	def Unir_AFN (self, AFN_2):
		#Se crea un nuevo estado inicial
		Nuevo_Inicio = Estado ()
		#Se crea un nuevo estado final
		Nuevo_Fin = Estado ()
		#Se agrega una transición del nuevo estado inicial al estado inicial del AFN_1
		Nuevo_Inicio.AddTransition (self.Estado_Inicial, '')
		#Se agrega una transición del nuevo estado inicial al estado inicial del AFN_2
		Nuevo_Inicio.AddTransition (AFN_2.Estado_Inicial, '')
		#Agregar una transición con epsilon de todos los estados finales al nuevo fin
		for e in self.Estados_Aceptacion:
			e.AddTransition (Nuevo_Fin, '')
			e.Estado_Aceptacion = False
		#Agregar una transición con epsilon de todos los estados finales al nuevo fin
		for e in AFN_2.Estados_Aceptacion:
			e.AddTransition (Nuevo_Fin, '')
			e.Estado_Aceptacion = False
		#Eliminar los estados de aceptación de ambos automatas
		self.Estados_Aceptacion = set ()
		AFN_2.Estados_Aceptacion = set ()
		#Agregar el nuevo estado de inicio al conjunto de estados del nuevo AFN
		self.Estados.add (Nuevo_Inicio)
		#Agregar el nuevo estado final al conjunto de estados del nuevo AFN
		self.Estados.add (Nuevo_Fin)
		#Se hace la union de alfabetos
		self.Estados = self.Estados.union (AFN_2.Estados)
		#Se asigna el estatus de estado de aceptación al nuevo estado final
		Nuevo_Fin.Estado_Aceptacion = True
		#Se agrega el nuevo estado final al conjunto de estados de aceptación
		self.Estados_Aceptacion.add (Nuevo_Fin)
		#Se actualiza el estado inicial del AFN
		self.Estado_Inicial = Nuevo_Inicio
		#Se actualiza el alfabeto del AFN con la unión de los alfabetos
		self.Alfabeto = (self.Alfabeto).union (AFN_2.Alfabeto)
		return self

	def Concatenar_AFN (self, AFN_2):
		#Cambiar las transiciones del estado inicial del AFN 2
		for e in self.Estados_Aceptacion:
			for t in AFN_2.Estado_Inicial.Transiciones:
				#Al estado final del AFN_1 se le agregan las transiciones del estado inicial de AFN_2
				e.AddTransition (t.estado_siguiente, t.simbolo_min, t.simbolo_max)
		#Eliminamos el estado inicial del AFN_2
		AFN_2.Estados.discard (AFN_2.Estado_Inicial)
		#Eliminamos todos los estados de aceptación del AFN
		for e in self.Estados_Aceptacion:
			e.Estado_Aceptacion = False
		self.Estados_Aceptacion = set ()
		#Los nuevos estados de aceptación serán los estados de aceptación del AFN_2
		self.Estados_Aceptacion = (self.Estados_Aceptacion).union (AFN_2.Estados_Aceptacion)
		#El nuevo alfabeto será la unión de ambos alfabetos
		self.Alfabeto = (self.Alfabeto).union (AFN_2.Alfabeto)
		#El nuevo conjunto de estados será la union de los estados de ambos AFN
		self.Estados = (self.Estados).union (AFN_2.Estados)
		return self

	def Cerradura_Positiva (self):
		#Se crea un nuevo estado inicial
		Nuevo_Inicio = Estado ()
		#Se crea un nuevo estado final
		Nuevo_Fin = Estado ()
		#Se agrega una transición del nuevo estado inicial al estado inicial del AFN
		Nuevo_Inicio.AddTransition (self.Estado_Inicial, '')
		#Agregar una transición con epsilon de todos los estados finales al estado inicial del AFN
		for e in self.Estados_Aceptacion:
			e.AddTransition (self.Estado_Inicial, '')
			e.Estado_Aceptacion = False
		#Eliminar los estados de aceptación del AFN
		self.Estados_Aceptacion = set ()
		#Agregar el nuevo estado de inicio al conjunto de estados del nuevo AFN
		self.Estados.add (Nuevo_Inicio)
		#Agregar el nuevo estado final al conjunto de estados del nuevo AFN
		self.Estados.add (Nuevo_Fin)
		#Se asigna el estatus de estado de aceptación al nuevo estado final
		Nuevo_Fin.Estado_Aceptacion = True
		#Se agrega el nuevo estado final al conjunto de estados de aceptación
		self.Estados_Aceptacion.add (Nuevo_Fin)
		#Se actualiza el estado inicial del AFN
		self.Estado_Inicial = Nuevo_Inicio
		return self

	def Cerradura_Kleene (self):
		#Se crea un nuevo estado inicial
		Nuevo_Inicio = Estado ()
		#Se crea un nuevo estado final
		Nuevo_Fin = Estado ()
		#Se agrega una transición del nuevo estado inicial al nuevo estado final del AFN
		Nuevo_Inicio.AddTransition (Nuevo_Fin, '')
		#Se agrega una transición del nuevo estado inicial al estado inicial del AFN
		Nuevo_Inicio.AddTransition (self.Estado_Inicial, '')
		#Agregar una transición con epsilon de todos los estados finales al estado inicial del AFN
		for e in self.Estados_Aceptacion:
			e.AddTransition (self.Estado_Inicial, '')
			e.Estado_Aceptacion = False
		#Eliminar los estados de aceptación del AFN
		self.Estados_Aceptacion = set ()
		#Agregar el nuevo estado de inicio al conjunto de estados del nuevo AFN
		self.Estados.add (Nuevo_Inicio)
		#Agregar el nuevo estado final al conjunto de estados del nuevo AFN
		self.Estados.add (Nuevo_Fin)
		#Se asigna el estatus de estado de aceptación al nuevo estado final
		Nuevo_Fin.Estado_Aceptacion = True
		#Se agrega el nuevo estado final al conjunto de estados de aceptación
		self.Estados_Aceptacion.add (Nuevo_Fin)
		#Se actualiza el estado inicial del AFN
		self.Estado_Inicial = Nuevo_Inicio
		return self

	def Cerradura_Opcional (self):
		#Se crea un nuevo estado inicial
		Nuevo_Inicio = Estado ()
		#Se crea un nuevo estado final
		Nuevo_Fin = Estado ()
		#Se agrega una transición del nuevo estado inicial al estado inicial del AFN
		Nuevo_Inicio.AddTransition (self.Estado_Inicial, '')
		#Se agrega una transición del nuevo estado inicial al nuevo estado final
		Nuevo_Inicio.AddTransition (Nuevo_Fin, '')
		#Agregar una transición con epsilon de todos los estados finales al nuevo estado final
		for e in self.Estados_Aceptacion:
			e.AddTransition (Nuevo_Fin, '')
			e.Estado_Aceptacion = False
		#Eliminar los estados de aceptación del AFN
		self.Estados_Aceptacion = set ()
		#Agregar el nuevo estado de inicio al conjunto de estados del nuevo AFN
		self.Estados.add (Nuevo_Inicio)
		#Agregar el nuevo estado final al conjunto de estados del nuevo AFN
		self.Estados.add (Nuevo_Fin)
		#Se asigna el estatus de estado de aceptación al nuevo estado final
		Nuevo_Fin.Estado_Aceptacion = True
		#Se agrega el nuevo estado final al conjunto de estados de aceptación
		self.Estados_Aceptacion.add (Nuevo_Fin)
		#Se actualiza el estado inicial del AFN
		self.Estado_Inicial = Nuevo_Inicio
		return self

	def get_estados (self):
		a = set ()
		for e in self.Estados:
			a.add (e.id_estado)
		return a

	def get_estado_inicial (self):
		a = set ()
		a.add (self.Estado_Inicial.id_estado)
		return a

	def get_edos_aceptacion (self):
		a = set ()
		for e in self.Estados_Aceptacion:
			a.add (e.id_estado)
		return a

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

	def AddTransition (self, estado_siguiente, simbolo_min, simbolo_max = ''):
		#Si solo se ingresa un simbolo
		if (len (simbolo_max) == 0):
			(self.Transiciones).add (Transicion (estado_siguiente, simbolo_min))
		#Si se ingresa un rango
		else:
			(self.Transiciones).add (Transicion (estado_siguiente, simbolo_min, simbolo_max))

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

def Crear ():
	os.system ("cls")
	#Simbolo para crear el AFN Básico
	simbolo = input ('\n\n¿Con qué simbolo deseas crear el AFN?\t')
	#Se crea el AFN con el símbolo seleccionado por el usuario
	Automata = AFN (simbolo)
	print ('\n\nAutomata básico con símbolo \'' + simbolo + '\' creado correctamente.\n\n\n')
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata (1 / 2 / 3)?\t')) - 1
	#Guardamos el automata creado en una de las 3 posiciones que se tienen
	Automatas [num_automata] = Automata

def Unir ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata 1:\t')) - 1
	automata2 = int (input ('\n\n\nSelecciona el autómata 2:\t')) - 1
	Automata = AFN ()
	#Se unen los AFN seleccionados y se guarda en otro AFN
	Automata = (Automatas [automata1]).Unir_AFN ((Automatas [automata2]))
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata (1 / 2 / 3)?\t')) - 1
	#Guardamos el automata creado en una de las 3 posiciones que se tienen
	Automatas [num_automata] = Automata

def Concatenar ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata 1:\t')) - 1
	automata2 = int (input ('\n\n\nSelecciona el autómata 2:\t')) - 1
	Automata = AFN ()
	#Se concatenan los 2 AFN y se guarda en otro AFN
	Automata = (Automatas [automata1]).Concatenar_AFN ((Automatas [automata2]))
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata (1 / 2 / 3)?\t')) - 1
	#Guardamos el automata creado en una de las 3 posiciones que se tienen
	Automatas [num_automata] = Automata

def Positiva ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata sobre el que deseas aplicar la operación +:\t')) - 1
	Automata = AFN ()
	#Se unen los AFN seleccionados y se guarda en otro AFN
	Automata = (Automatas [automata1]).Cerradura_Positiva ()
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata (1 / 2 / 3)?\t')) - 1
	#Guardamos el automata creado en una de las 3 posiciones que se tienen
	Automatas [num_automata] = Automata

def Kleene ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata sobre el que deseas aplicar la operación *:\t')) - 1
	Automata = AFN ()
	#Se unen los AFN seleccionados y se guarda en otro AFN
	Automata = (Automatas [automata1]).Cerradura_Kleene ()
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata (1 / 2 / 3)?\t')) - 1
	#Guardamos el automata creado en una de las 3 posiciones que se tienen
	Automatas [num_automata] = Automata

def Opcional ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata sobre el que deseas aplicar la operación ?:\t')) - 1
	Automata = AFN ()
	#Se unen los AFN seleccionados y se guarda en otro AFN
	Automata = (Automatas [automata1]).Cerradura_Opcional ()
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata (1 / 2 / 3)?\t')) - 1
	#Guardamos el automata creado en una de las 3 posiciones que se tienen
	Automatas [num_automata] = Automata

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