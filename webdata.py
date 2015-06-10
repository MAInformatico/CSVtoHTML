#!/usr/bin/python

#It's a source code to obtain the source code of a webpages that it's executed on the client.

import urllib2

response=urllib2.urlopen('http://www.unapaginacualquiera.com') #poner aquí el nombre de la página que nos interesa
cod=response.read()

#Obtenemos el codigo de la pagina
#Ahora debemos almacenarlo en un archivo de texto

#abrimos un flujo de escritura
a=open("archivoejemplo.txt","w") #abrimos/creamos el archivo con permiso de escritura
a.write(cod) #escribimos el codigo obtenido de la web
a.close() #cerramos el flujo de escritura
