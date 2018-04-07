from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys

class Interfaz:

	def __init__ (self, ventana):
		#Ventana principal
		self.ventana = ventana
		#Label que muestra 'Menú:'
		self.label_menu = None
		#Boton para mandar a ventana de ingresar expresión regular
		self.boton_crear_AFN = None
		#Boton para mandar a ventana de validar cadena
		self.boton_validar_cadena = None
		#Boton para mandar a ventana de unir autómatas
		self.boton_union_especial = None
		#Boton para mandar a ventana de convertir AFN a AFD
		self.boton_convertir_AFD = None
		#Boton para mandar a ventana de validar cadena léxicamente
		self.boton_lexico = None
		#Textbox para ingresar expresión regular
		self.entrada_expresion = None
		#Label que muestra 'Expresión:'
		self.label_expresion = None
		#Label que muestra 'Posición:'
		self.label_posicion = None
		#Combobox para mostrar las posiciones donde guardar el autómata
		self.combo_posicion = None
		#Label que muestra 'Resultado:'
		self.label_resultado = None
		#Label para mostrar el mensaje de correcto
		self.label_correcto = None
		#Boton para regresar al menu principal
		self.boton_menu_principal = None
		#Boton para ingresar otra expresión a resolver o convertir a posfijo/prefijo
		self.boton_otro_AFN = None
		#Boton para resolver la expresión ingresada
		self.boton_crear_AFN_2 = None
		#Boton para convertir a posfijo la expresión ingresada
		self.boton_validar_cadena_2 = None
		#Boton para convertir a posfijo la expresión ingresada
		self.boton_union_especial_2 = None

	def mostrar_menu_principal (self):
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 16, weight = 'bold')
		fuente_menu = font.Font (family = 'Microsoft YaHei UI Light', size = 32, weight = 'bold')
		posicion_y = 25
		posicion_x = 220
		self.label_menu = Label (self.ventana, text = 'Menú:', font = fuente_menu, fg = color_gris, bg = 'white')
		self.label_menu.place (relx = 0.1, rely = 0.2)
		self.boton_crear_AFN = Button (self.ventana, text = 'Crear Autómata', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.crear_AFN)
		self.boton_validar_cadena = Button (self.ventana, text = 'Validar Cadena', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.validar_cadena)
		self.boton_union_especial = Button (self.ventana, text = 'Unir Autómatas', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.union_especial)
		self.boton_convertir_AFD = Button (self.ventana, text = 'Convertir a AFD', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.convertir_AFD)
		self.boton_lexico = Button (self.ventana, text = 'Análisis Léxico', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.analisis_lexico)
		self.boton_crear_AFN.place (x = posicion_x, y = posicion_y)
		self.boton_validar_cadena.place (x = posicion_x, y = posicion_y + 50)
		self.boton_union_especial.place (x = posicion_x, y = posicion_y + 100)
		self.boton_convertir_AFD.place (x = posicion_x, y = posicion_y + 150)
		self.boton_lexico.place (x = posicion_x, y = posicion_y + 200)

	def ocultar_menu_principal (self):
		self.label_menu.place_forget ()
		self.boton_union_especial.place_forget ()
		self.boton_validar_cadena.place_forget ()
		self.boton_crear_AFN.place_forget ()
		self.boton_convertir_AFD.place_forget ()
		self.boton_lexico.place_forget ()

	def crear_AFN (self):
		self.ocultar_menu_principal ()
		fuente_entrada = font.Font (family = 'Microsoft YaHei UI Light', size = 14)
		fuente_entrada2 = font.Font (family = 'Microsoft YaHei UI Light', size = 12)
		fuente_label = font.Font (family = 'Microsoft YaHei UI Light', size = 16, weight = 'bold')
		fuente_boton = font.Font (family = 'Microsoft YaHei UI Light', size = 12)
		color_azul = '#214E77'
		color_gris = '#CDD0D2'
		color_gris2 = '#686B6D'
		posicion_y = 115
		posicion_x = 220
		self.label_expresion = Label (self.ventana, text = 'Expresión regular:', font = fuente_label, fg = color_gris2,
									bg = 'white')
		self.label_expresion.place (x = posicion_x - 200, y = posicion_y - 4)
		self.entrada_expresion = Entry (self.ventana, bg = color_gris, bd = 0, font = fuente_entrada, cursor = 'ibeam')
		self.entrada_expresion.place (x = posicion_x, y = posicion_y)
		self.label_posicion = Label (self.ventana, text = 'Posición:', font = fuente_label, fg = color_gris2,
									bg = 'white')
		self.label_posicion.place (x = posicion_x - 110, y = posicion_y + 52)
		self.combo_posicion = ttk.Combobox (self.ventana, state = 'readonly', font = fuente_entrada2, width = 22)
		self.combo_posicion ['values'] = Posiciones
		self.combo_posicion.place (x = posicion_x, y = posicion_y + 58)
		self.boton_crear_AFN_2 = Button (self.ventana, text = 'Crear Autómata', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.crear_AFN_2)
		self.boton_crear_AFN_2.place (x = posicion_x - 45, y = posicion_y + 105)

	def crear_AFN_2 (self):
		self.entrada_expresion.place_forget ()
		self.label_expresion.place_forget ()
		self.label_posicion.place_forget ()
		self.combo_posicion.place_forget ()
		self.boton_crear_AFN_2.place_forget ()
		expresion = self.entrada_expresion.get ()
		posicion = self.combo_posicion.current ()
		correcto = 'AFN creado correctamente'
		"""
		AQUI SE TENE QUE CREAR EL AUTOMATA CON 'expresion'
		"""
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_resultado = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		posicion_y = 120
		posicion_x = 60
		self.label_correcto = Label (self.ventana, text = str (correcto), font = fuente_resultado, fg = color_gris,
								bg = 'white')
		self.label_correcto.place (x = posicion_x, y = posicion_y)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.regresar_menu_principal)
		self.boton_menu_principal.place (relx = 0.25, rely = 0.35)
		self.boton_otro_AFN = Button (self.ventana, text = 'Crear otro autómata', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.ingresar_otra_expresion)
		self.boton_otro_AFN.place (relx = 0.3, rely = 0.45)
	
	def regresar_menu_principal (self):
		self.label_correcto.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otro_AFN.place_forget ()
		self.mostrar_menu_principal ()

	def ingresar_otra_expresion (self):
		self.label_correcto.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otro_AFN.place_forget ()
		self.crear_AFN ()

	def validar_cadena (self):
		self.ocultar_menu_principal ()
		fuente_entrada = font.Font (family = 'Microsoft YaHei UI Light', size = 14)
		fuente_label = font.Font (family = 'Microsoft YaHei UI Light', size = 16, weight = 'bold')
		fuente_boton = font.Font (family = 'Microsoft YaHei UI Light', size = 12)
		color_azul = '#214E77'
		color_gris = '#CDD0D2'
		color_gris2 = '#686B6D'
		posicion_y = 120
		posicion_x = 220
		self.entrada_expresion = Entry (self.ventana, bg = color_gris, bd = 0, font = fuente_entrada, cursor = 'ibeam')
		self.entrada_expresion.place (x = posicion_x, y = posicion_y)
		self.label_expresion = Label (self.ventana, text = 'Expresión:', font = fuente_label, fg = color_gris2,
									bg = 'white')
		self.label_expresion.place (x = posicion_x - 140, y = posicion_y - 5)
		self.boton_validar_cadena_2 = Button (self.ventana, text = 'Convertir a posfijo', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.posfijo)
		self.boton_validar_cadena_2.place (x = posicion_x - 25, y = posicion_y + 50)

	def posfijo (self):
		self.entrada_expresion.place_forget ()
		self.label_expresion.place_forget ()
		self.boton_validar_cadena_2.place_forget ()
		expresion = self.entrada_expresion.get ()
		print ('Expresion ingresada: ' + expresion)
		label_correcto = expresion
		"""
		label_correcto = convertir_posfijo (expresion)
		En la variable 'expresion' ya está guardada la expresión a convertir a posfijo en un string.
		En resultado se almacena la expresión convertida en posfijo.
		BORRAR LÍNEA 156 Y DEJAR LÍNEA 158
		"""
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_resultado = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		self.label_resultado = Label (self.ventana, text = 'Posfijo:', font = fuente_resultado, fg = color_gris,
								bg = 'white')
		self.label_resultado.place (relx = 0.15, rely = 0.2)
		self.label_correcto = Label (self.ventana, text = str (label_correcto), font = fuente_resultado, fg = color_gris,
								bg = 'white')
		self.label_correcto.place (relx = 0.38, rely = 0.2)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.regresar_menu_principal)
		self.boton_menu_principal.place (relx = 0.25, rely = 0.35)
		self.boton_otro_AFN = Button (self.ventana, text = 'Ingresar otra expresión', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.ingresar_otra_posfijo)
		self.boton_otro_AFN.place (relx = 0.27, rely = 0.45)

	def ingresar_otra_posfijo (self):
		self.label_resultado.place_forget ()
		self.label_correcto.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otro_AFN.place_forget ()
		self.validar_cadena ()

	def union_especial (self):
		self.ocultar_menu_principal ()
		fuente_entrada = font.Font (family = 'Microsoft YaHei UI Light', size = 14)
		fuente_label = font.Font (family = 'Microsoft YaHei UI Light', size = 16, weight = 'bold')
		fuente_boton = font.Font (family = 'Microsoft YaHei UI Light', size = 12)
		color_azul = '#214E77'
		color_gris = '#CDD0D2'
		color_gris2 = '#686B6D'
		posicion_y = 120
		posicion_x = 220
		self.entrada_expresion = Entry (self.ventana, bg = color_gris, bd = 0, font = fuente_entrada, cursor = 'ibeam')
		self.entrada_expresion.place (x = posicion_x, y = posicion_y)
		self.label_expresion = Label (self.ventana, text = 'Expresión:', font = fuente_label, fg = color_gris2,
									bg = 'white')
		self.label_expresion.place (x = posicion_x - 140, y = posicion_y - 5)
		self.boton_union_especial_2 = Button (self.ventana, text = 'Convertir a prefijo', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.prefijo)
		self.boton_union_especial_2.place (x = posicion_x - 25, y = posicion_y + 50)

	def prefijo (self):
		self.entrada_expresion.place_forget ()
		self.label_expresion.place_forget ()
		self.boton_union_especial_2.place_forget ()
		expresion = self.entrada_expresion.get ()
		print ('Expresion ingresada: ' + expresion)
		label_correcto = expresion
		"""
		label_correcto = convertir_prefijo (expresion)
		En la variable 'expresion' ya está guardada la expresión a convertir a prefijo en un string.
		En resultado se almacena la expresión convertida en prefijo.
		BORRAR LÍNEA 212 Y DEJAR LÍNEA 214
		"""
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_resultado = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		self.label_resultado = Label (self.ventana, text = 'Prefijo:', font = fuente_resultado, fg = color_gris,
								bg = 'white')
		self.label_resultado.place (relx = 0.15, rely = 0.2)
		self.label_correcto = Label (self.ventana, text = str (label_correcto), font = fuente_resultado, fg = color_gris,
								bg = 'white')
		self.label_correcto.place (relx = 0.38, rely = 0.2)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.regresar_menu_principal)
		self.boton_menu_principal.place (relx = 0.25, rely = 0.35)
		self.boton_otro_AFN = Button (self.ventana, text = 'Ingresar otra expresión', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.ingresar_otra_prefijo)
		self.boton_otro_AFN.place (relx = 0.27, rely = 0.45)

	def ingresar_otra_prefijo (self):
		self.label_resultado.place_forget ()
		self.label_correcto.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otro_AFN.place_forget ()
		self.union_especial ()

	def convertir_AFD (self):
		self.ocultar_menu_principal ()

	def analisis_lexico (self):
		self.ocultar_menu_principal ()

os.system ("cls")
global Automatas
Automatas = []
Posiciones = []
for i in range (8):
	Automatas.append (i)
	Posiciones.append (i + 1)
ventana_principal = Tk ()											#Declara una ventana
ventana_principal.title ('Calculadora')								#Titulo de la ventana
ventana_principal.geometry ('510x550')								#Tamaño de la ventana
#Configuración del fondo de la ventana
ventana_principal.config (bg = 'white')
imagen = ImageTk.PhotoImage (file = "Fondo.jpg")
fondo = Label (ventana_principal, image = imagen, bd = 0)
fondo.place (relx = 0.01, rely = 0.5)
interfaz = Interfaz (ventana_principal)
interfaz.mostrar_menu_principal ()
interfaz.ventana.mainloop ()										#Muestra la ventana