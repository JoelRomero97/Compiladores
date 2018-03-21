import os
import sys
from AFN import *
from AFD import *
from Lexic import *

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

def Convertir_AFN ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata que deseas convertir a AFD:\t')) - 1
	Automata = AFD ()
	#Se convierte al automata AFN a un AFD
	Automata = (Automatas [automata1]).AFN_To_AFD ()
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nTabla de transiciones:\n\n')
	Automata.get_tabla ()
	num_automata = int (input ('\n\n¿En qué posición deseas guardar el autómata ' + posiciones () + ' ?\t')) - 1
	#Guardamos el automata creado en una de las n posiciones que se tienen
	Automatas [num_automata] = Automata

def Mostrar_Quintupla ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el autómata del que deseas ver la quintupla:\t')) - 1
	Automata = Automatas [automata1]
	print ('\n\nAlfabeto: ', Automata.Alfabeto)
	print ('\n\nEstados: ', Automata.get_estados ())
	print ('\n\nEstado inicial: ', Automata.get_estado_inicial ())
	print ('\n\nEstados de aceptación: ', Automata.get_edos_aceptacion ())
	input ('\n\n\n\nPresiona cualquier tecla para continuar...')

def Analisis_Lexico ():
	os.system ("cls")
	automata1 = int (input ('\n\n\nSelecciona el AFD sobre el que deseas validar cadenas:\t')) - 1
	#Obtenemos el automata deseado en un AFD
	Automata = AFD ()
	Automata = (Automatas [automata1])
	cadena = ''
	while ((cadena != 'Salir') and (cadena != 'salir')):
		os.system ("cls")
		print ('\n\n\nEscribe \'Salir\' o \'salir\' para terminar regresar al menu principal')
		cadena = input ('\n\n\nIngresa la cadena a ser analizada lexicamente:\t')
		print ('\n')
		if ((cadena == 'Salir') or (cadena == 'salir')):
			break
		Lex = Lexic (Automata, cadena)
		token = 1
		while (token != 0):
			token, lexema = Lex.get_token ()
			print ('Token: ' + str (token) + '\tLexema: \'' + str (lexema) + '\'')
		input ('\n\n\n\nPresiona cualquier tecla para continuar...')

def Salir ():
	for i in range (len (Automatas)):
		Automatas.pop ()
	print ('\n\nAutomatas eliminados.\n\n\n')
	sys.exit ()

def Menu ():
	#Diccionario para seleccionar la opcion que desee el usuario
	funciones = {1:Crear, 2:Unir, 3:Concatenar, 4:Positiva, 5:Kleene, 6:Opcional, 7:Validacion,
				8:Unir_Especial, 9: Convertir_AFN, 10: Mostrar_Quintupla, 11: Analisis_Lexico, 12:Salir}
	option = 1
	while option < 11 and option > 0:
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
		print ('9. Convertir a AFD')
		print ('10. Mostrar Quintupla de Automata')
		print ('11. Analisis_Lexico')
		print ('12. Salir\n\n\n')
		option = int (input ('Selecciona una opción:\t'))
		#Llamar a la función según la opción seleccionada
		funciones [option] ()

#Lista de n elementos para guardar los automatas creados por el usuario
global Automatas
Automatas = []
for i in range (8):
	Automatas.append (i)

Menu ()  