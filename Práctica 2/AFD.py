import os
import sys

class AFD:
	def __init__ (self):
		#Inicialización del estado inicial a 'null'
		self.Estado_Inicial = None
		#El conjunto del alfabeto se inicializa como un conjunto vacío
		self.Alfabeto = set ()
		#El conjunto de estados se inicializa como un conjunto vacío
		self.Estados = set ()
		#El conjunto de estados de aceptación se inicializa como un conjunto vacío
		self.Estados_Aceptacion = set ()

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
				#Se agrega una transición del estado inicial al estado final con el caracter 'simbolo'
				(self.Estado_Inicial).AddTransition (Estado_Final, simbolo)
			else:
				(self.Estado_Inicial).AddTransition (Estado_Final, simbolo [0], simbolo [2])
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
		for e in self.Estados_Aceptacion:
			#Agregar una transición con epsilon de todos los estados finales al estado inicial del AFN
			e.AddTransition (self.Estado_Inicial, '')
			#Agregar una transición con epsilon de todos los estados finales al nuevo estado final
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

	def Cerradura_Kleene (self):
		#Se crea un nuevo estado inicial
		Nuevo_Inicio = Estado ()
		#Se crea un nuevo estado final
		Nuevo_Fin = Estado ()
		#Se agrega una transición del nuevo estado inicial al nuevo estado final del AFN
		Nuevo_Inicio.AddTransition (Nuevo_Fin, '')
		#Se agrega una transición del nuevo estado inicial al estado inicial del AFN
		Nuevo_Inicio.AddTransition (self.Estado_Inicial, '')
		for e in self.Estados_Aceptacion:
			#Agregar una transición con epsilon de todos los estados finales al estado inicial del AFN
			e.AddTransition (self.Estado_Inicial, '')
			#Agregar una transición con epsilon de todos los estados finales al nuevo estado final
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

	def Cerradura_Epsilon (self, Estado, Conjunto = False):
		Conjunto_Estados = set ()
		pila = []
		#Si 'Estado' es un conjunto
		if (Conjunto == True):
			#Recorremos cada uno de los estados del conjunto de estados
			for e in Estado:
				#Agregamos al conjunto solucion la cerradura epsilon de cada estado
				Conjunto_Estados = Conjunto_Estados.union (self.Cerradura_Epsilon (e))
		else:
			#Agregamos el estado a la pila para analizarlo
			pila.append (Estado)
			#Mientras la pila tenga elementos
			while (len (pila) > 0):
				#Sacamos el ultimo elemento de la pila
				Estado_Aux = pila.pop ()
				#Si no está contenido ese estado en el conjunto, lo agregamos
				if (Estado_Aux not in Conjunto_Estados):
					Conjunto_Estados.add (Estado_Aux)
					for t in Estado_Aux.Transiciones:
						#Si la transicion de ese estado nos lleva a un estado con epsilon
						if (len (t.simbolo_min) == 0):
							#Se agrega a la pila para ser analizado
							pila.append (t.estado_siguiente)
		return Conjunto_Estados

	def Mover (self, Estado, simbolo, Conjunto = False):
		Conjunto_Estados = set ()
		#Si 'Estado' es un conjunto
		if (Conjunto == True):
			#Recorremos cada uno de los estados del conjunto de estados
			for e in Estado:
				#Agregamos al conjunto solucion la operacion mover de cada estado
				Conjunto_Estados = Conjunto_Estados.union (self.Mover (e, simbolo))
		else:
			#Recorremos cada una de las transiciones del estado
			for t in Estado.Transiciones:
				#Si la transicion con ese simbolo nos lleva a un estado
				if ((t.simbolo_min <= simbolo) and (t.simbolo_max >= simbolo)):
					#Agregamos el estado siguiente al conjunto solucion de estados
					Conjunto_Estados.add (t.estado_siguiente)
		return Conjunto_Estados

	def Ir_A (self, Estado, simbolo):
		Conjunto_Estados = set ()
		#Se calcula la operación mover de todo el conjunto recibido
		Conjunto_Estados = Conjunto_Estados.union (self.Mover (Estado, simbolo, True))
		#Se retorna la operación cerradura epsilon de todo el conjunto resultado de la operación mover
		return self.Cerradura_Epsilon (Conjunto_Estados, True)

	def Validar_Cadena (self, cadena):
		#Conjunto de estados para obtener la cerradura epsilon
		Conjunto_Estados = set ()
		#Calculamos la cerradura epsilon del estado inicial del AFN
		Conjunto_Estados = self.Cerradura_Epsilon (self.Estado_Inicial)
		for simbolo in cadena:
			#Calculamos la operacion Ir_A de cada estado con cada simbolo de la cadena
			Conjunto_Estados = self.Ir_A (Conjunto_Estados, simbolo)
			if (len (Conjunto_Estados) == 0):
				return False
		for estado in self.Estados_Aceptacion:
			if (estado in Conjunto_Estados):
				return True
		return False

	def Union_Especial (self, automatas):
		#Se crea un AFN vacío para guardar el resultado
		Nuevo_Automata = AFN ()
		#Se crea un nuevo estado inicial
		Nuevo_Inicio = Estado ()
		#Se crea un nuevo estado final
		Nuevo_Fin = Estado ()
		#Se agregan todos los estados al nuevo automata
		for a in automatas:
			Nuevo_Automata.Estados = (Nuevo_Automata.Estados).union (a.Estados)
		#Se crea el alfabeto del nuevo automata con la union de alfabetos de los otros automatas
		for a in automatas:
			Nuevo_Automata.Alfabeto = (Nuevo_Automata.Alfabeto).union (a.Alfabeto)
		#Se agrega una transición del nuevo estado inicial a los estados iniciales de los automatas
		for a in automatas:
			Nuevo_Inicio.AddTransition (a.Estado_Inicial, '')
		#Agregar una transición con epsilon de todos los estados finales de los automatas al nuevo fin
		for a in automatas:
			for e in a.Estados_Aceptacion:
				e.AddTransition (Nuevo_Fin, '')
				e.Estado_Aceptacion = False
		#Agregar el nuevo estado de inicio al conjunto de estados del nuevo AFN
		(Nuevo_Automata.Estados).add (Nuevo_Inicio)
		#Agregar el nuevo estado final al conjunto de estados del nuevo AFN
		(Nuevo_Automata.Estados).add (Nuevo_Fin)
		#Se asigna el nuevo estado inicial del AFN
		Nuevo_Automata.Estado_Inicial = Nuevo_Inicio
		#Se asigna el estatus de estado de aceptación al nuevo estado final
		Nuevo_Fin.Estado_Aceptacion = True
		#Se agrega el nuevo estado final al conjunto de estados de aceptación
		(Nuevo_Automata.Estados_Aceptacion).add (Nuevo_Fin)
		return Nuevo_Automata

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

class Estados_Si:
	#Id global para los conjuntos de estados
	id_global_si = 0

	def __init__ (self, Estados):
		#Se le asigna un id único a cada estado creado
		self.id_estado = Estados_Si.id_global_si
		#El id incrementa después de ser asignado al estado
		Estados_Si.id_global_si = Estados_Si.id_global_si + 1
		#Valor booleano para saber si ya fue analizado ese conjunto
		self.Analizado = False
		#El conjunto de transiciones se inicializa como un conjunto vacío
		self.Estados = Estados

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

def posiciones ():
	pos = '('
	for i in range (len (Automatas)):
		pos = pos + str (i + 1) + ' / '
	pos = pos.rstrip ('/ ')
	pos = pos + ')'
	return pos

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
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata ' + posiciones () + ' ?\t')) - 1
	#Guardamos el automata creado en una de las n posiciones que se tienen
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
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata ' + posiciones () + ' ?\t')) - 1
	#Guardamos el automata creado en una de las n posiciones que se tienen
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
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata ' + posiciones () + ' ?\t')) - 1
	#Guardamos el automata creado en una de las n posiciones que se tienen
	Automatas [num_automata] = Automata

def Positiva ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata sobre el que deseas aplicar la operación +:\t')) - 1
	Automata = AFN ()
	#Se calcula la cerradura positiva del AFN
	Automata = (Automatas [automata1]).Cerradura_Positiva ()
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata ' + posiciones () + ' ?\t')) - 1
	#Guardamos el automata creado en una de las n posiciones que se tienen
	Automatas [num_automata] = Automata

def Kleene ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata sobre el que deseas aplicar la operación *:\t')) - 1
	Automata = AFN ()
	#Se calcula la cerradura de kleene del AFN
	Automata = (Automatas [automata1]).Cerradura_Kleene ()
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata ' + posiciones () + ' ?\t')) - 1
	#Guardamos el automata creado en una de las n posiciones que se tienen
	Automatas [num_automata] = Automata

def Opcional ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata sobre el que deseas aplicar la operación ?:\t')) - 1
	Automata = AFN ()
	#Se calcula la cerradura opcional del AFN
	Automata = (Automatas [automata1]).Cerradura_Opcional ()
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata ' + posiciones () + ' ?\t')) - 1
	#Guardamos el automata creado en una de las n posiciones que se tienen
	Automatas [num_automata] = Automata

def Validacion ():
	os.system ("cls")
	#Cadena a ser validada
	cadena = ''
	flag = True
	automata1 = int (input ('\n\n\nSelecciona el autómata sobre el que deseas validar cadenas:\t')) - 1
	#Obtenemos el automata deseado en un AFN
	Automata = AFN ()
	Automata = (Automatas [automata1])
	while ((cadena != 'Salir') and (cadena != 'salir')):
		os.system ("cls")
		print ('\n\n\nEscribe \'Salir\' o \'salir\' para terminar regresar al menu principal')
		cadena = input ('\n\nIngresa una cadena para ser validada:\t')
		if ((cadena == 'Salir') or (cadena == 'salir')):
			break
		flag = Automata.Validar_Cadena (cadena)
		#Si la cadena es aceptada
		if (flag == True):
			print ('\n\nLa cadena \'' + cadena + '\' es aceptada por el AFN :)')
			input ('\n\n\n\nPresiona cualquier tecla para continuar...')
		else:
			print ('\n\nLa cadena \'' + cadena + '\' no es aceptada por el AFN :(')
			input ('\n\n\n\nPresiona cualquier tecla para continuar...')

def Unir_Especial ():
	i = 1
	automata1 = 1
	Automatas_Unir = []
	Automata = AFN ()
	#Mientras el usuario siga seleccionando automatas, se van a unir
	while (automata1 > -1):
		os.system ("cls")
		print ('\n\n\nSelecciona el automata \'0\' para dejar de unir automatas')
		automata1 = int (input ('\n\n\nSelecciona el autómata ' + str (i) + ':\t')) - 1
		if (automata1 == -1):
			break
		i = i + 1
		#Se agrega el automata seleccionado a la lista para realizar la union de todos
		Automatas_Unir.append (Automatas [automata1])
	#Obtener automata de todas las uniones de automatas
	Automata = Automata.Union_Especial (Automatas_Unir)
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata ' + posiciones () + ' ?\t')) - 1
	#Guardamos el automata creado en una de las n posiciones que se tienen
	Automatas [num_automata] = Automata

def Salir ():
	for i in range (len (Automatas)):
		Automatas.pop ()
	print ('\n\nAutomatas eliminados.\n\n\n')
	sys.exit ()

def Menu ():
	#Diccionario para seleccionar la opcion que desee el usuario
	funciones = {1:Crear, 2:Unir, 3:Concatenar, 4:Positiva, 5:Kleene, 6:Opcional, 7:Validacion, 8:Unir_Especial, 9:Salir}
	option = 1
	while option < 10 and option > 0:
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
		print ('8. Unión especial')
		print ('9. Salir\n\n\n')
		option = int (input ('Selecciona una opción:\t'))
		#Llamar a la función según la opción seleccionada
		funciones [option] ()

#Lista de n elementos para guardar los automatas creados por el usuario
Automatas = []
for i in range (6):
	Automatas.append (i)

Menu ()