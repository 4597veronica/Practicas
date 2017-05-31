#coding:utf-8

"""En este codigo haremos que el usuario introduzca los dias de la semana
 Además podra consultarlos borarlos y modificarlos. """

######################VARIABLES#####################################
sortir=False 
dias_semana = []
######################MENU##############################################
def inprimir():
	print "________________"	 
	print"¿Que desea hacer?" 
	print"1-Consultar datos" 
	print"2-Introducir datos" 
	print"3-Borrar datos"
	print"4-Introducir un elemento donde desee" 
	print"0-Salir"
###################CONSULTAR LISTA######################################
""" Consultar la lista """
def consultar():
	for dia in dias_semana:
		print dia ,
###################AÑADIR ELEMENTO######################################
""" Introducir un elemento a la lista """
def introduce():
	sem=raw_input("Introduce el dia de la semana ")
	dias_semana.append(sem)
###################BORRAR ELEMENTO###################################### 
"""Te pide el elemnto que quieres borar """
def borar():
	for dia in dias_semana:
		print dia ,
	print""
	sem=raw_input("Introduce el dia que borrar ")
	for dia in dias_semana:
		if dia==sem:
			dias_semana.remove(sem)
		else:
			print sem , "no existe en la lista"
###################INTRODUCIR ELEMENTO##################################
def introducir():
	sem=raw_input("Introduce el dia de la semana ")
	posicion=input("Introduce el numero de la posicion, donde quiere colocalo")
	 #La lista empieza por 0, asi que le resto 1, ya que normalmente el usuario empezara a contar en 1
	dias_semana.insert(posicion-1,sem)
########################################################################
while sortir==False:
	inprimir()
	consulta=input("Intoduce una opcion ")
	print ""
	if consulta==1:		
		consultar() 
	if consulta==2:
		introduce()
	if consulta==3:
		borar()
	if consulta==4:
		introducir()
	if consulta==0:
		sortir=True
