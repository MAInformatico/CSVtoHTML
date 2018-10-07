#!/usr/bin/python

import urllib2

response=urllib2.urlopen('http://unadireccion')
cod=response.read()

#Obtenemos el codigo de la pagina
#Ahora debemos almacenarlo en un archivo de texto

#abrimos un flujo de escritura
a=open("archivoprueba.txt","w") #abrimos/creamos el archivo con permiso de escritura
a.write(cod) #escribimos el codigo obtenido de la web
a.close() #cerramos el flujo de escritura
