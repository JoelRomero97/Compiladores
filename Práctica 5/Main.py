from tkinter import *
from tkinter import font
from tkinter import ttk
from AFN import *
from AFD import *
from Lexic import *
from Lexema import *
from Expresion_Regular import *
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
		self.boton_convertir_AFN = None
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
		#Label que muestra el mensaje de correcto
		self.label_correcto = None
		#Label que muestra 'Cadena:'
		self.label_cadena = None
		#Label que muestra la secuencia de tokens
		self.label_tokens = None
		#Boton para regresar al menu principal
		self.boton_menu_principal = None
		#Boton para crear otro AFN
		self.boton_otro_AFN = None
		#Boton para validar otra cadena
		self.boton_otra_cadena = None
		#Boton para crear el AFN
		self.boton_crear_AFN_2 = None
		#Boton para validar cadena
		self.boton_validar_cadena_2 = None
		#Boton para unir el autómata
		self.boton_union_especial_2 = None
		#Boton para analizar léxicamente una cadena
		self.boton_analisis_lexico_2 = None
		#Boton para unir otro autómata
		self.boton_si = None
		#Boton para dejar de unir autómatas
		self.boton_no = None
		#Lista para guardar las posiciones a unir de los AFN
		self.posiciones_unir = []
		#Boton para convertir otro AFN
		self.boton_convertir_otro_AFN = None

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
		self.boton_convertir_AFN = Button (self.ventana, text = 'Convertir a AFD', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.convertir_AFN)
		self.boton_lexico = Button (self.ventana, text = 'Análisis Léxico', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.analisis_lexico)
		self.boton_crear_AFN.place (x = posicion_x, y = posicion_y)
		self.boton_validar_cadena.place (x = posicion_x, y = posicion_y + 50)
		self.boton_union_especial.place (x = posicion_x, y = posicion_y + 100)
		self.boton_convertir_AFN.place (x = posicion_x, y = posicion_y + 150)
		self.boton_lexico.place (x = posicion_x, y = posicion_y + 200)

	def ocultar_menu_principal (self):
		self.label_menu.place_forget ()
		self.boton_union_especial.place_forget ()
		self.boton_validar_cadena.place_forget ()
		self.boton_crear_AFN.place_forget ()
		self.boton_convertir_AFN.place_forget ()
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
		self.label_posicion = Label (self.ventana, text = 'Posición:', font = fuente_label, fg = color_gris2, bg = 'white')
		self.label_posicion.place (x = posicion_x - 110, y = posicion_y + 52)
		self.combo_posicion = ttk.Combobox (self.ventana, state = 'readonly', font = fuente_entrada2, width = 22)
		self.combo_posicion ['values'] = Posiciones
		self.combo_posicion.place (x = posicion_x, y = posicion_y + 58)
		self.boton_crear_AFN_2 = Button (self.ventana, text = 'Crear Autómata', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.crear_AFN_2)
		self.boton_crear_AFN_2.place (x = posicion_x - 45, y = posicion_y + 105)

	def crear_AFN_2 (self):
		self.label_expresion.place_forget ()
		self.entrada_expresion.place_forget ()
		self.label_posicion.place_forget ()
		self.combo_posicion.place_forget ()
		self.boton_crear_AFN_2.place_forget ()
		expresion = self.entrada_expresion.get ()
		posicion = self.combo_posicion.current ()
		correcto = 'AFN creado correctamente'
		Automata = AFN ()
		Lexico = Lexema (expresion)
		expresion_regular = Expresion_Regular (Lexico)
		if (expresion_regular.E (Automata)):
			correcto = 'AFN creado correctamente'
		else:
			correcto = 'Error al crear el AFN :('
		Automatas [posicion] = Automata
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_correcto = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		posicion_y = 120
		posicion_x = 60
		self.label_correcto = Label (self.ventana, text = correcto, font = fuente_correcto, fg = color_gris, bg = 'white')
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
		fuente_entrada2 = font.Font (family = 'Microsoft YaHei UI Light', size = 12)
		fuente_label = font.Font (family = 'Microsoft YaHei UI Light', size = 16, weight = 'bold')
		fuente_boton = font.Font (family = 'Microsoft YaHei UI Light', size = 12)
		color_azul = '#214E77'
		color_gris = '#CDD0D2'
		color_gris2 = '#686B6D'
		posicion_y = 115
		posicion_x = 220
		self.label_cadena = Label (self.ventana, text = 'Cadena:', font = fuente_label, fg = color_gris2, bg = 'white')
		self.label_cadena.place (x = posicion_x - 106, y = posicion_y - 4)
		self.entrada_cadena = Entry (self.ventana, bg = color_gris, bd = 0, font = fuente_entrada, cursor = 'ibeam')
		self.entrada_cadena.place (x = posicion_x, y = posicion_y)
		self.label_posicion = Label (self.ventana, text = 'Autómata:', font = fuente_label, fg = color_gris2, bg = 'white')
		self.label_posicion.place (x = posicion_x - 130, y = posicion_y + 52)
		self.combo_posicion = ttk.Combobox (self.ventana, state = 'readonly', font = fuente_entrada2, width = 22)
		self.combo_posicion ['values'] = Posiciones
		self.combo_posicion.place (x = posicion_x, y = posicion_y + 58)
		self.boton_validar_cadena_2 = Button (self.ventana, text = 'Validar cadena', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.validar_cadena_2)
		self.boton_validar_cadena_2.place (x = posicion_x - 35, y = posicion_y + 105)

	def validar_cadena_2 (self):
		self.entrada_cadena.place_forget ()
		self.label_cadena.place_forget ()
		self.label_posicion.place_forget ()
		self.combo_posicion.place_forget ()
		self.boton_validar_cadena_2.place_forget ()
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_correcto = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		cadena = self.entrada_cadena.get ()
		posicion = self.combo_posicion.current ()
		Automata = AFN ()
		Automata = (Automatas [posicion])
		if (Automata.Validar_Cadena (cadena)):
			correcto = 'Cadena aceptada por el AFN'
			self.label_correcto = Label (self.ventana, text = correcto, font = fuente_correcto, fg = color_gris,
								bg = 'white')
			self.label_correcto.place (relx = 0.08, rely = 0.2)
		else:
			correcto = 'Cadena no aceptada por el AFN'
			self.label_correcto = Label (self.ventana, text = correcto, font = fuente_correcto, fg = color_gris,
								bg = 'white')
			self.label_correcto.place (relx = 0.045, rely = 0.2)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command=self.regresar_menu_principal_2)
		self.boton_menu_principal.place (relx = 0.26, rely = 0.35)
		self.boton_otra_cadena = Button (self.ventana, text = 'Validar otra cadena', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.validar_otra_cadena)
		self.boton_otra_cadena.place (relx = 0.32, rely = 0.45)

	def regresar_menu_principal_2 (self):
		self.label_correcto.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otra_cadena.place_forget ()
		self.mostrar_menu_principal ()

	def validar_otra_cadena (self):
		self.label_correcto.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otra_cadena.place_forget ()
		self.validar_cadena ()

	def union_especial (self):
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
		self.label_automata = Label (self.ventana, text = 'Autómata:', font = fuente_label, fg = color_gris2,
									bg = 'white')
		self.label_automata.place (x = posicion_x - 130, y = posicion_y)
		self.combo_posicion = ttk.Combobox (self.ventana, state = 'readonly', font = fuente_entrada2, width = 22)
		self.combo_posicion ['values'] = Posiciones
		self.combo_posicion.place (x = posicion_x, y = posicion_y + 6)
		self.boton_union_especial_2 = Button (self.ventana, text = 'Unir autómata', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.union_especial_2)
		self.boton_union_especial_2.place (x = posicion_x - 30, y = posicion_y + 55)

	def union_especial_2 (self):
		self.label_automata.place_forget ()
		self.combo_posicion.place_forget ()
		self.boton_union_especial_2.place_forget ()
		(self.posiciones_unir).append (self.combo_posicion.current ())
		unir_otro = '¿Deseas unir otro AFN?'
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_correcto = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		self.label_correcto = Label (self.ventana, text = unir_otro, font = fuente_correcto, fg = color_gris,
								bg = 'white')
		self.label_correcto.place (relx = 0.15, rely = 0.2)
		self.boton_si = Button (self.ventana, text = 'Si', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.union_especial_3)
		self.boton_si.place (relx = 0.45, rely = 0.35)
		self.boton_no = Button (self.ventana, text = 'No', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.union_especial_4)
		self.boton_no.place (relx = 0.44, rely = 0.45)

	def union_especial_3 (self):
		self.label_correcto.place_forget ()
		self.boton_si.place_forget ()
		self.boton_no.place_forget ()
		self.union_especial ()

	def union_especial_4 (self):
		self.label_correcto.place_forget ()
		self.boton_si.place_forget ()
		self.boton_no.place_forget ()
		correcto = 'AFN unido correctamente'
		color_azul = '#214E77'
		color_gris = '#686B6D'
		posicion_y = 115
		posicion_x = 220
		fuente_entrada2 = font.Font (family = 'Microsoft YaHei UI Light', size = 12)
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_label = font.Font (family = 'Microsoft YaHei UI Light', size = 16, weight = 'bold')
		fuente_correcto = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		self.label_correcto = Label (self.ventana, text = correcto, font = fuente_correcto, fg = color_gris,
								bg = 'white')
		self.label_correcto.place (relx = 0.14, rely = 0.15)
		self.label_posicion = Label (self.ventana, text = 'Posición:', font = fuente_label, fg = color_gris, bg = 'white')
		self.label_posicion.place (x = posicion_x - 110, y = posicion_y + 62)
		self.combo_posicion = ttk.Combobox (self.ventana, state = 'readonly', font = fuente_entrada2, width = 22)
		self.combo_posicion ['values'] = Posiciones
		self.combo_posicion.place (x = posicion_x, y = posicion_y + 68)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command=self.regresar_menu_principal_3)
		self.boton_menu_principal.place (relx = 0.27, rely = 0.45)

	def regresar_menu_principal_3 (self):
		self.label_correcto.place_forget ()
		self.label_posicion.place_forget ()
		self.combo_posicion.place_forget ()
		self.boton_menu_principal.place_forget ()
		posicion = self.combo_posicion.current ()
		Automatas_Unir = []
		for i in self.posiciones_unir:
			Automatas_Unir.append (Automatas [i])
		Automata = AFN ()
		Automata = Automata.Union_Especial (Automatas_Unir)
		Automatas [posicion] = Automata
		self.mostrar_menu_principal ()

	def convertir_AFN (self):
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
		self.label_posicion = Label (self.ventana, text = 'Posición:', font = fuente_label, fg = color_gris2, bg = 'white')
		self.label_posicion.place (x = posicion_x - 110, y = posicion_y - 4)
		self.combo_posicion = ttk.Combobox (self.ventana, state = 'readonly', font = fuente_entrada2, width = 22)
		self.combo_posicion ['values'] = Posiciones
		self.combo_posicion.place (x = posicion_x, y = posicion_y + 2)
		self.boton_convertir_AFN_2 = Button (self.ventana, text = 'Convertir AFN a AFD', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.convertir_AFN_2)
		self.boton_convertir_AFN_2.place (x = posicion_x - 50, y = posicion_y + 50)

	def convertir_AFN_2 (self):
		self.label_posicion.place_forget ()
		self.combo_posicion.place_forget ()
		self.boton_convertir_AFN_2.place_forget ()
		posicion = self.combo_posicion.current ()
		correcto = 'AFN convertido correctamente'
		Automata = AFD ()
		Automata = (Automatas [posicion]).AFN_To_AFD ()
		Automatas [posicion] = Automata
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_correcto = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		posicion_y = 120
		posicion_x = 60
		self.label_correcto = Label (self.ventana, text = correcto, font = fuente_correcto, fg = color_gris, bg = 'white')
		self.label_correcto.place (x = posicion_x - 30, y = posicion_y)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command=self.regresar_menu_principal_4)
		self.boton_menu_principal.place (relx = 0.25, rely = 0.35)
		self.boton_convertir_otro_AFN = Button (self.ventana, text = 'Convertir otro autómata', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.convertir_otro_AFN)
		self.boton_convertir_otro_AFN.place (relx = 0.28, rely = 0.45)

	def regresar_menu_principal_4 (self):
		self.label_correcto.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_convertir_otro_AFN.place_forget ()
		posicion = self.combo_posicion.current ()
		self.mostrar_menu_principal ()

	def convertir_otro_AFN (self):
		self.label_correcto.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_convertir_otro_AFN.place_forget ()
		self.convertir_AFN ()

	def analisis_lexico (self):
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
		self.label_cadena = Label (self.ventana, text = 'Cadena:', font = fuente_label, fg = color_gris2, bg = 'white')
		self.label_cadena.place (x = posicion_x - 106, y = posicion_y - 4)
		self.entrada_cadena = Entry (self.ventana, bg = color_gris, bd = 0, font = fuente_entrada, cursor = 'ibeam')
		self.entrada_cadena.place (x = posicion_x, y = posicion_y)
		self.label_posicion = Label (self.ventana, text = 'Autómata:', font = fuente_label, fg = color_gris2, bg = 'white')
		self.label_posicion.place (x = posicion_x - 130, y = posicion_y + 52)
		self.combo_posicion = ttk.Combobox (self.ventana, state = 'readonly', font = fuente_entrada2, width = 22)
		self.combo_posicion ['values'] = Posiciones
		self.combo_posicion.place (x = posicion_x, y = posicion_y + 58)
		self.boton_analisis_lexico_2 = Button (self.ventana, text = 'Validar cadena', font = fuente_boton,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd = 0, command = self.analisis_lexico_2)
		self.boton_analisis_lexico_2.place (x = posicion_x - 35, y = posicion_y + 105)

	def analisis_lexico_2 (self):
		self.entrada_cadena.place_forget ()
		self.label_cadena.place_forget ()
		self.label_posicion.place_forget ()
		self.combo_posicion.place_forget ()
		self.boton_analisis_lexico_2.place_forget ()
		cadena = self.entrada_cadena.get ()
		posicion = self.combo_posicion.current ()
		correcto = 'Secuencia de tokens:'
		Automata = AFD ()
		Automata = (Automatas [posicion])
		Lex = Lexic (Automata, cadena)
		token = 1
		tokens = ''
		while (token != 0):
			token, lexema = Lex.get_token ()
			tokens = tokens + 'Token: ' + str (token) + '\t\tLexema: ' + str (lexema) + '\n'
		color_azul = '#214E77'
		color_gris = '#686B6D'
		fuente_botones = font.Font (family = 'Microsoft YaHei UI Light', size = 12, weight = 'bold')
		fuente_correcto = font.Font (family = 'Microsoft YaHei UI Light', size = 22, weight = 'bold')
		fuente_correcto2 = font.Font (family = 'Microsoft YaHei UI Light', size = 14, weight = 'bold')
		self.label_correcto = Label (self.ventana, text = correcto, font = fuente_correcto, fg = color_gris,
								bg = 'white')
		self.label_correcto.place (relx = 0.12, rely = 0.04)
		self.label_tokens = Label (self.ventana, text = tokens, font = fuente_correcto2, fg = color_gris,
								bg = 'white')
		self.label_tokens.place (relx = 0.2, rely = 0.15)
		self.boton_menu_principal = Button (self.ventana, text = 'Regresar al menu principal', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command=self.regresar_menu_principal_5)
		self.boton_menu_principal.place (relx = 0.26, rely = 0.85)
		self.boton_otra_cadena = Button (self.ventana, text = 'Validar otra cadena', font = fuente_botones,
								cursor = 'hand2', fg = color_azul, bg = 'white', bd=0, command = self.otro_analisis_lexico)
		self.boton_otra_cadena.place (relx = 0.32, rely = 0.92)

	def regresar_menu_principal_5 (self):
		self.label_correcto.place_forget ()
		self.label_tokens.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otra_cadena.place_forget ()
		self.mostrar_menu_principal ()

	def otro_analisis_lexico (self):
		self.label_correcto.place_forget ()
		self.label_tokens.place_forget ()
		self.boton_menu_principal.place_forget ()
		self.boton_otra_cadena.place_forget ()
		self.analisis_lexico ()

os.system ("cls")
global Automatas
Automatas = []
Posiciones = []
for i in range (5):
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