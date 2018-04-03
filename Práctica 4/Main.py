from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import os
import sys

class Interfaz:

	def __init__ (self, ventana):
		#Ventana principal
		self.ventana = ventana
		#Label que muestra 'Menú:'
		self.label_menu = None
		#Boton para mandar a ventana de resolver expresión
		self.boton_resolver = None
		#Boton para mandar a ventana de convertir a posfijo
		self.boton_posfijo = None
		#Boton para mandar a ventana de convertir a prefijo
		self.boton_prefijo = None
		#Textbox para ingresar expresión a resolver o convertir a prefijo/posfijo
		self.entrada_expresion = None
		#Label que muestra 'Expresión:'
		self.label_expresion = None
		#Label que muestra 'Resultado:'
		self.label_resultado = None
		#Label para mostrar el resultado de la expresión o la expresión en prefijo/posfijo
		self.resultado = None
		#Boton para regresar al menu principal
		self.boton_menu_principal = None
		#Boton para ingresar otra expresión a resolver o convertir a posfijo/prefijo
		self.boton_otra_expresion = None
		#Boton para resolver la expresión ingresada
		self.boton_resolver_2 = None
		#Boton para convertir a posfijo la expresión ingresada
		self.boton_posfijo_2 = None
		#Boton para convertir a posfijo la expresión ingresada
		self.boton_prefijo_2 = None

	def mostrar_menu_principal (self):
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 16, weight = 'bold')
		fuente_menu = font.Font (family = 'Microsoft YaHei UI Light', size = 32, weight = 'bold')
		posicion_y = 75
		posicion_x = 220
		self.label_menu = Label (self.ventana, text = 'Menú:', font = fuente_menu, fg = color_gris, bg = 'white')
		self.label_menu.place (relx = 0.1, rely = 0.2)
		self.boton_resolver = Button (self.ventana, text = 'Resolver expresión', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.resolver_expresion)
		self.boton_posfijo = Button (self.ventana, text = 'Convertir a posfijo', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.expresion_posfijo)
		self.boton_prefijo = Button (self.ventana, text = 'Convertir a prefijo', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.expresion_prefijo)
		self.boton_resolver.place (x = posicion_x, y = posicion_y)
		self.boton_posfijo.place (x = posicion_x, y = posicion_y + 50)
		self.boton_prefijo.place (x = posicion_x, y = posicion_y + 100)
		#for name in sorted(font.families()):
		#	print (name)

	def ocultar_menu_principal (self):
		self.label_menu.place_forget ()
		self.boton_prefijo.place_forget ()
		self.boton_posfijo.place_forget ()
		self.boton_resolver.place_forget ()

	def resolver_expresion (self):
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
		self.boton_resolver_2 = Button (self.ventana, text = 'Resolver expresión', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.solve)
		self.boton_resolver_2.place (x = posicion_x - 25, y = posicion_y + 50)

	def solve (self):
		self.entrada_expresion.place_forget ()
		self.label_expresion.place_forget ()
		self.boton_resolver_2.place_forget ()
		expresion = self.entrada_expresion.get ()
		print ('Expresion ingresada: ' + expresion)
		resultado = expresion
		"""
		resultado = calcular (expresion)
		En la variable 'expresion' ya está guardada la expresión a resolver en un string.
		En resultado se almacena el resultado final de la expresión para mostrarse posteriormente.
		BORRAR LÍNEA 91 Y DEJAR LÍNEA 93
		"""
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_resultado = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		posicion_y = 120
		posicion_x = 150
		self.label_resultado = Label (self.ventana, text = 'Resultado:', font = fuente_resultado, fg = color_gris,
								bg = 'white')
		self.label_resultado.place (x = posicion_x, y = posicion_y)
		self.resultado = Label (self.ventana, text = str (resultado), font = fuente_resultado, fg = color_gris,
								bg = 'white')
		self.resultado.place (x = posicion_x + 160, y = posicion_y)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.regresar_menu_principal)
		self.boton_menu_principal.place (relx = 0.25, rely = 0.35)
		self.boton_otra_expresion = Button (self.ventana, text = 'Ingresar otra expresión', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.ingresar_otra_expresion)
		self.boton_otra_expresion.place (relx = 0.27, rely = 0.45)
	
	def regresar_menu_principal (self):
		self.label_resultado.place_forget ()
		self.resultado.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otra_expresion.place_forget ()
		self.mostrar_menu_principal ()

	def ingresar_otra_expresion (self):
		self.label_resultado.place_forget ()
		self.resultado.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otra_expresion.place_forget ()
		self.resolver_expresion ()

	def expresion_posfijo (self):
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
		self.boton_posfijo_2 = Button (self.ventana, text = 'Convertir a posfijo', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.posfijo)
		self.boton_posfijo_2.place (x = posicion_x - 25, y = posicion_y + 50)

	def posfijo (self):
		self.entrada_expresion.place_forget ()
		self.label_expresion.place_forget ()
		self.boton_posfijo_2.place_forget ()
		expresion = self.entrada_expresion.get ()
		print ('Expresion ingresada: ' + expresion)
		resultado = expresion
		"""
		resultado = convertir_posfijo (expresion)
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
		self.resultado = Label (self.ventana, text = str (resultado), font = fuente_resultado, fg = color_gris,
								bg = 'white')
		self.resultado.place (relx = 0.38, rely = 0.2)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.regresar_menu_principal)
		self.boton_menu_principal.place (relx = 0.25, rely = 0.35)
		self.boton_otra_expresion = Button (self.ventana, text = 'Ingresar otra expresión', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.ingresar_otra_posfijo)
		self.boton_otra_expresion.place (relx = 0.27, rely = 0.45)

	def ingresar_otra_posfijo (self):
		self.label_resultado.place_forget ()
		self.resultado.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otra_expresion.place_forget ()
		self.expresion_posfijo ()

	def expresion_prefijo (self):
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
		self.boton_prefijo_2 = Button (self.ventana, text = 'Convertir a prefijo', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.prefijo)
		self.boton_prefijo_2.place (x = posicion_x - 25, y = posicion_y + 50)

	def prefijo (self):
		self.entrada_expresion.place_forget ()
		self.label_expresion.place_forget ()
		self.boton_prefijo_2.place_forget ()
		expresion = self.entrada_expresion.get ()
		print ('Expresion ingresada: ' + expresion)
		resultado = expresion
		"""
		resultado = convertir_prefijo (expresion)
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
		self.resultado = Label (self.ventana, text = str (resultado), font = fuente_resultado, fg = color_gris,
								bg = 'white')
		self.resultado.place (relx = 0.38, rely = 0.2)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.regresar_menu_principal)
		self.boton_menu_principal.place (relx = 0.25, rely = 0.35)
		self.boton_otra_expresion = Button (self.ventana, text = 'Ingresar otra expresión', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.ingresar_otra_prefijo)
		self.boton_otra_expresion.place (relx = 0.27, rely = 0.45)

	def ingresar_otra_prefijo (self):
		self.label_resultado.place_forget ()
		self.resultado.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otra_expresion.place_forget ()
		self.expresion_prefijo ()

os.system ("cls")
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