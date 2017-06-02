#coding:utf-8

"""En este programa haremos un calendario. Utilizaremos un modulo de fechas y dos for, el primero para crear las semanas y el segundo los dias"""

"""importamos un modulo para trabajar con fechas"""
import datetime

"""Pedimos el mes a mostrar"""
year=input("Dime un año ")
mes=input("Dime un mes ")


"""Declaramos las variables que vamos a necesitar para el calendario"""
filas=0
columna=0
contador=1
if mes==4 or mes==6 or mes==9 or mes==11:
	top=30
else:
	if mes==2:
		if year%4==0:
			top=28
		else:29
	else:
		top=31


"""Para crear la lista que necesita el for"""
def my_range(inici, fi, increment):
	while inici <= fi:
		"""Retorna l'element actual del rang (llista)"""
		yield inici
		inici = inici + increment

"""Guardamos la fecha introducida, para que el sistema la reconozca como tal	"""	
fecha_nacimiento=datetime.datetime(year, mes, 1)

"""guardamos en una variable el día de la semana de la fecha"""
dia_semana=datetime.datetime.weekday(fecha_nacimiento)

"""Creamos el calendario"""
for filas in my_range(1,6,1):
	for columna in my_range(1,7,1):
		if not contador>=top:
			if filas==1: #Creamos la 1 semana
				if columna<=dia_semana:
					print"  ", 
					#Si el mes no empieza en lunes escribira 3 especios y el contador no subira
				else:
					print "", contador,
					contador=contador+1	
					"""En la primera semana, empezara a escribir el dia que 
					toque. Para que quede encuadrado y bonito muestra un 
					espacio y el contador, este augmentara en este caso"""
					
			else:
				if contador<=9:
					print "",contador,
					contador=contador+1	
				else:
					print contador,
					contador=contador+1	
				""" Si no nos encontramos en la 1 fila, escribira los dias
				 normalmente para que quede más visual si el numero es de
				 una cifra tambien escribira un espacio """
	print""

