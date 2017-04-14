#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


from random import randint

#Jugador humà
jugador1=raw_input("PAra lanzar un dado presione enter")
aleatori=randint(1,6)
aleatori2=randint(1,6)
jugador1=aleatori+aleatori2

#Jugador machine
aleatori3=randint(1,6)
aleatori4=randint(1,6)
jugador2=aleatori3+aleatori4



# Empat (3 combinacions)
if (jugador1==jugador2):
	print "Mi jugada es: ",jugador2
	print "Tu jugada es: ",jugador1
	print "Empat"
	
else: # 6 combinacions
	# Guanya jugador1 (3 combinacions)
	if (jugador1>jugador2):
		print "Mi jugada es: ",jugador2
		print "Tu jugada es: ",jugador1
		print "Tu guanyes!!!!!"
		
	else: # Guanya jugador2 (3 combinacions)
		print "Mi jugada es: ",jugador2
		print "Tu jugada es: ",jugador1
		print "Ets un .... has perdut !!!!"
