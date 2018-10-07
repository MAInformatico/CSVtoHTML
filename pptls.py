#!/usr/bin/python

import random

v=['piedra','papel','tijera','largarto','spock'] #valores posibles
ajug=input("Escriba el numero correspondiente al arma elegida: 0-piedra, 1-papel, 2-tijera, 3-lagarto o 4-spock ")
jug1=v[ajug]
def aleatoria(v):
	b=random.randint(0, 4)
	return b

a=aleatoria(v)
jug2=v[a]
#ARMAS ESCOGIDAS POR EL JUGADOR Y LA MAQUINA

def Juego(jug1,jug2): #Definimos el juego
	if jug1==v[0]:
		piedra(jug1,jug2)
	else:
		if jug1==v[1]:
			papel(jug1,jug2)
		else:
			if jug1==v[2]:
				tijera(jug1,jug2)
			else:
				if jug1==v[3]:
					lagarto(jug1,jug2)
				else:
					if jug1==v[4]:
						spock(jug1,jug2)
#Fin def juego

#Reglas del juegp
def piedra(jug1,jug2):
		if jug2==v[3]:
			print "Piedra lapida lagarto"
		else:
			if jug2==v[2]:
				print "Piedra aplasta tijera"
			else:		#derrotas
				if jug2==v[1]:
					print "Papel tapa piedra"
				else:
					if jug2==v[4]:
						print "Spock vaporiza piedra"
					else:
						if jug1==v[0] and jug2==v[0]:
							print "Empate"

#FIN DE LA PIEDRA

def papel(jug1,jug2):
		if jug2==v[0]:
			print "Papel tapa piedra"
		else:
			if jug2==v[4]:
				print "Papel desautoriza Spock"
			else:		#derrotas
				if jug2==v[2]:
					print "Tijera corta papel"
				else:
					if jug2==v[3]:
						print "Lagarto come papel"
					else:
						if jug1==v[1] and jug2==v[1]:
							print "Empate"

#FIN DEL PAPEL

def tijera(jug1,jug2):
		if jug2==v[3]:
			print "Tijera decapita lagarto"
		else:
			if jug2==v[1]:
				print "Tijera corta papel"
			else:		#derrotas
				if jug2==v[0]:
					print "Piedra aplasta tijera"
				else:
					if jug2==v[4]:
						print "Spock rompe tijera"
					else:
						if jug1==v[2] and jug2==v[2]:
							print "Empate"

#FIN DEL TIJERA

def lagarto(jug1,jug2):
		if jug2==v[1]:
			print "Lagarto come papel"
		else:
			if jug2==v[4]:
				print "Lagarto envenena Spock"
			else:		#derrotas
				if jug2==v[2]:
					print "Tijera decapita lagarto"
				else:
					if jug2==v[0]:
						print "Piedra lapida lagarto"
					else:
						if jug1==v[3] and jug2==v[3]:
							print "Empate"

#FIN DE LAGARTO

def spock(jug1,jug2):
		if jug2==v[0]:
			print "Spock vaporiza piedra"
		else:
			if jug2==v[2]:
				print "Spock rompe tijera"
			else:		#derrotas
				if jug2==v[1]:
					print "Papel desautoriza Spock"
				else:
					if jug2==v[3]:
						print "Lagarto envenena Spock"
					else:
						if jug1==v[4] and jug2==v[4]:
							print "Empate"

#FIN DE SPOCK



Juego(jug1,jug2)

