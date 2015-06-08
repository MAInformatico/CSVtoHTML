#!/usr/bin/python

import urllib2
import csv

class Web:

	def __init__(self,fichero,cod):
		self.fichero=fichero #Nombre del archivo

	def dameFichero(self):
		self.fichero=raw_input("Introduzca el nombre del fichero CSV: ")
	
	def creaPagina(self):
		nombre=raw_input("Introduzca el nombre del archivo .htm que desee crear: ")
		self.cod=open(nombre,"w") #creamos el archivo con el fuente HTML

	def codCabecera(self):
		self.cod.write("<html>")
		self.cod.write("<head>")
		self.cod.write("<title>Proyecto Python</title>")
		self.cod.write("</head>")
		self.cod.write("<body>")

	def creaTabla(self): #convertimos el .CSV en una tabla
		self.cod.write("<table border=1 align=center>")
		self.cod.write("<tr><th>Nombre<th>Apellido1</th><th>Apellido2</th><th>E-mail</th></tr>")
		self.fichero=open(self.fichero,"r") #abrimos el .csv
		mi_csv=csv.reader(self.fichero) #leemos todo el archivo
		for x,y,z,i in mi_csv:
			self.cod.write("<tr>")
			self.cod.write("<td>")
			self.cod.write(x)
			self.cod.write("</td>")
			self.cod.write("<td>")
			self.cod.write(y)			
			self.cod.write("</td>")
			self.cod.write("<td>")
			self.cod.write(z)
			self.cod.write("</td>")
			self.cod.write("<td>")
			self.cod.write(i)
			self.cod.write("</td>")
			self.cod.write("</tr>")

	def cierraTabla(self):				
		self.cod.write("</table>")

	def finCodigo(self): #</body>
		self.cod.write("</body>")
		self.cod.write("</html")
		self.fichero.close()
		self.cod.close()

#Creamos nuestro objeto web
miPagina=Web("archivo.csv","index.htm")
miPagina.dameFichero()
miPagina.creaPagina()
miPagina.codCabecera()
miPagina.creaTabla()
miPagina.cierraTabla()
miPagina.finCodigo()
