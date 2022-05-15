# -*- coding: utf-8 -*-
"""
@author: luis mendoza y efren mancilla
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from ColorLabel import ColorLabel
from kivy.uix.textinput import TextInput
import json
import pymysql.cursors

class AccesoLogin(App):
	def btnacce_press(self,obj):
		if self.connection :
			nick = self.txtusuario.text
			passwd = self.txtpassw.text
			MiCursor = self.connection.cursor()
			SQL = 'Select * from usuario where nick = %s and password = sha2(%s,256);'
			MiCursor.excute(SQL,[nick,passwd])
			Resultado = MiCursor.fetchone()
			if Resultado:
				self.col2.text = "Acceso concedido"
				print("Acceso concedido")
			else:
				self.col2.text = "Acceso no concedido"
				print("Acceso no concedido")
	
	def iniciarDB(self):
		self.Conf = None
		with open("db.json") as jsonfile:
			self.Conf =  json.load(jsonfile)
		
		self.conecction = pymsql.connect(
			host=self.Conf["HOST"],user=self.Conf["DBUSER"],
			password=self.Conf["BDPASS"],database=self.Conf["DBNAME"],
			charset='utf8mb4',port=self.Conf["PORT"])
	
	def build(self):
		self.gcols3 = GridLayout(cols=3)
		self.gfila5 = GridLayout(rows=5)
		self.lblusuario = ColorLabel(text='Usuario')
		self.lblusuario.background_color = [1,0,0,1]
		self.txtusuario = TextInput(text='',multiline=False)
		self.lblpassw = ColorLabel(text='Contraseña')
		self.lblpassw.background_color = [1,0,0,1]
		self.txtpassw = TextInput(text='',password=True,multiline=False)
		self.btnacce = Button(text="Acceder")
		self.btnacce.background_color = [0,0,0,1]
		
		self.fila5.add_widget(self.lblusuario)
		self.fila5.add_widget(self.txtusuario)
		self.fila5.add_widget(self.lblpassw)
		self.fila5.add_widget(self.txtpassw)
		self.fila5.add_widget(self.btnacce)
		#-----------------
		self.btnacce.bind(on_press=self.btnacce_press)
		#-------------------
		col1 = ColorLabel(text='')
		col1.background_color = [0.5,0.7,1,1]
		self.col2 = ColorLabel(text='')
		self.col2.background_color = [0.5,0.7,1,1]
		self.gcols3.add_widge(col1)
		self.gcols3.add_widget(self.gfila5)
		self.gcols3.add_widget(self.col2)
		return self.gcols3


if __name__ == '__main__':
	Miapp = AccesoLogin()
	Miapp.iniciarDB()
	Miapp().run()
