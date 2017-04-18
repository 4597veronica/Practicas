# coding:utf-8
from random import randint
saldo=100
sortir=False
minima=10
while sortir== False:
	print"¿Cuanto quieres apostar?"
	print"Apuesta minima 10€"
	sortir3=False
	while sortir3==False:
		apuesta=input("Introduce tu apuesta ")
		if apuesta==-1:
			sortir3=True 
		else: 
			if apuesta>=10 and apuesta<=saldo:
				sortir3=True 
	if not apuesta==-1:
		saldo=saldo-apuesta
		
	if not apuesta==-1:
		# Generem la tirada de jugador1
		banca=randint(2,14)
		bancapal=randint(1,4)

		numero=banca
		if (banca==11):
			numero="J"
		if (banca==12):
			numero="Q"
		if (banca==13):
			numero="K"
		if (banca==14):
			numero="A"
			
		if (bancapal==1):
			pal="P"
		if (bancapal==2):
			pal="T"
		if (bancapal==3):
			pal="D"
		if (bancapal==4):
			pal="C"


		print "Jugador 1 te: " , numero, "de " , pal


		# Generem la tirada de jugador2 (agafa una carta aleatoria)
		#Ho fem amb un bucle perque aquesta no coinciseixo amb l'anterior

		sortir2=False

		while sortir2==False:
			
			j2num=randint(2,14)
			j2pal=randint(1,4)
			numero=j2num
			#Generem el numero
			if (j2num==11):
				numero="J"
			if (j2num==12):
				numero="Q"
			if (j2num==13):
				numero="K"
			if (j2num==14):
				numero="A"
				
			#Generem el pal
			if (j2pal==1):
				pal="P"
			if (j2pal==2):
				pal="T"
			if (j2pal==3):
				pal="D"
			if (j2pal==4):
				pal="C"
			#Condicio se salida: SI SON DIFERENTS
			if not j2num==banca :
				sortir2=True

		print "Jugador 2 te: " , numero, "de " , pal

		# Comprovem si hi ha empat
		if (banca==j2num):
			print "Empat"
		else:
			if (banca>j2num):
				print "Guanya jugador1"
			else:
				if (banca<j2num):
					print "Guanya jugador2"
					saldo=saldo+(apuesta*2)
			print "Tu saldo es de:",saldo
	
	print saldo
	if saldo<10 or apuesta==-1:
		sortir = True
