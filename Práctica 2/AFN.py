from Estado import *
from Estados_Si import *
from AFD import *

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
		for a in automatas:
			#Se agregan todos los estados al nuevo automata
			Nuevo_Automata.Estados = (Nuevo_Automata.Estados).union (a.Estados)
			#Se crea el alfabeto del nuevo automata con la union de alfabetos de los otros automatas
			Nuevo_Automata.Alfabeto = (Nuevo_Automata.Alfabeto).union (a.Alfabeto)
			#Se agrega una transición del nuevo estado inicial a los estados iniciales de los automatas
			Nuevo_Inicio.AddTransition (a.Estado_Inicial, '')
			
		#Agregar el nuevo estado de inicio al conjunto de estados del nuevo AFN
		(Nuevo_Automata.Estados).add (Nuevo_Inicio)
		#Se asigna el nuevo estado inicial del AFN
		Nuevo_Automata.Estado_Inicial = Nuevo_Inicio
		token = 10
		for a in automatas:
			for e in a.Estados_Aceptacion:
				#Se agregan los estados de aceptación al conjunto de estado de aceptación de los AFN
				(Nuevo_Automata.Estados_Aceptacion).add (e)
				#Se asigna un token distinto a cada estado de aceptación
				e.Token = token
				token = token + 10
		return Nuevo_Automata

	def AFN_To_AFD (self):
		automata = AFD ()
		#Asignar el mismo alfabeto del AFN al AFD
		automata.Alfabeto = self.Alfabeto
		#Obtenemos el tamaño del alfabeto
		num_columnas = (len (self.Alfabeto) + 1)
		#Se crea una lista de estados si vacío
		estados_si = []
		#Calculamos la cerradura epsilon del estado inicial del AFN
		Si = self.Cerradura_Epsilon (self.Estado_Inicial)
		#Se agrega el conjunto de estados obtenido S0
		estados_si.append (Estados_Si (Si))
		#Agregamos la primera fila de la tabla
		fila = [-1] * num_columnas
		for c in automata.Alfabeto:
			fila [(list(automata.Alfabeto)).index (c)] = c
		fila [num_columnas - 1] = '¿Acept?'
		(automata.Tabla).append (fila)
		#Recorremos el conjunto de estados si
		j = 0
		while (j < len (estados_si)):
			i = 0
			fila = [-1] * num_columnas
			for simbolo in automata.Alfabeto:
				#Obtenemos un conjunto de estados con la operación Ir A
				Si = self.Ir_A ((estados_si [j]).Estados, simbolo)
				#Verificamos que no sea un conjunto vacío
				if (len (Si) == 0):
					i = i + 1
					continue
				#Variable bool para saber si ya existe el estado
				existe = False
				#Verificamos si el conjunto obtenido ya existe
				k = 0
				while (k < len (estados_si)):
					if (Si == (estados_si [k]).Estados):
						existe = True
						fila [i] = (estados_si [k]).id_estado
						break
					k = k + 1
				#Si el conjunto auxiliar no existe y no está vacío
				if (not existe):
					estados_si.append (Estados_Si (Si))
					k = len (estados_si) - 1
					fila [i] = (estados_si [k]).id_estado
				i = i + 1
			(automata.Tabla).append (fila)
			j = j + 1
		row = 0
		last = num_columnas - 1
		for s in estados_si:
			for e in s.Estados:
				if (e.Estado_Aceptacion):
					automata.Tabla [row][last] = e.Token
			row = row + 1
		return automata

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