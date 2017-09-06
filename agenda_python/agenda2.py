# coding:utf-8

######################VARIABLES#########################################
import locale

import datetime
sortir=False
     ################LISTA_CALENDARIO###############
"""Para crear la lista que necesita el for"""
def my_range(inici, fi, increment):
	while inici <= fi:
		"""Retorna l'element actual del rang (llista)"""
		yield inici
		inici = inici + increment
     

####CALENDARIO######################################

def calendario():
    ################VARIABLES_CALENDARIO###############
	"""Pedimos el mes a mostrar"""
	year=input("Dime un año ")
	mes=input("Dime un mes ")

	"""Declaramos las variables que vamos a necesitar para el calendario"""
	filas=0
	columna=0
	contador=1
	if mes==4 or mes==6 or mes==9 or mes==11:
		top=31
	else:
		if mes==2:
			if year%4==0:
				top=28
			else:30
		else:
			top=32

	"""Guardamos la fecha introducida, para que el sistema la reconozca como tal	"""	
	fecha_nacimiento=datetime.datetime(year, mes, 1)

	"""guardamos en una variable el día de la semana de la fecha"""
	dia_semana=datetime.datetime.weekday(fecha_nacimiento)

	##########Creamos el calendario#############
	print " L  M  X  J  V  S  D"
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

#################################VER_TAREAS##############################
def vertareas():
	archivo_2 = open('tareas.txt' , 'r')
	tareas_2=archivo_2.read()
	print tareas_2


#############################CREAR_TAREA################################
def crear_tarea():
	archivo = open('tareas.txt', 'a')
	cadena1=raw_input("Introduzca la asignatura")
	cadena3=raw_input("Introduzca la tarea")
	cadena2=raw_input("Introduce la fecha de la tarea ")
	cadena4="________________________________"
	tarea_crear=archivo.write(cadena1 + '\n' + cadena2 + '\n'  +  cadena3 + '\n' + cadena4 + '\n')
	
############################VER_HORARIO##################################
def ver_horario():
	archivo = open('horario.txt' , 'r')
	horario=archivo.read()
	print horario
		


#########################PROGRAMA_PRINCIPAL#############################
print "0-Salir"
print "1-Ver el horario"
print "2-Ver el calendario"
print "3-Ver tareas"
print "4-Crear tareas"
	


while sortir== False:
	opciones=input("¿Que desea hacer? ")
  
	if opciones == 1:
		ver_horario()
		
		
	if opciones == 2:
		calendario()
		
	if opciones == 3:
		vertareas()
		
		
	if opciones == 4:
		crear_tarea()
		
	if opciones ==0:
		sortir = True 
		
############################################################
