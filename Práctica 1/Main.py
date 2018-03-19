import os
import sys
from AFN import *

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

def Salir ():
	for i in range (len (Automatas)):
		Automatas.pop ()
	print ('\n\n\nAutomatas eliminados.\n\n\n')
	sys.exit ()

def Menu ():
	#Diccionario para seleccionar la opcion que desee el usuario
	funciones = {1:Crear, 2:Unir, 3:Concatenar, 4:Positiva, 5:Kleene, 6:Opcional, 7:Validacion, 8:Salir}
	option = 1
	while option < 9 and option > 0:
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

#Lista de n elementos para guardar los automatas creados por el usuario
Automatas = []
for i in range (3):
	Automatas.append (i)

Menu ()