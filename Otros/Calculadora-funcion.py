#coding:utf-8

#Este programa sera una calculadora sencilla
###############################VARIABLES############################
sortir=False

###############################MOSTRAR MENU#########################
def menu():
	print "¿Que desea hacer amo?"

	print "S.-salir"

	print "1.-Sumar"

	print "2.-Restar"

	print "3.-Multiplicar"

	print "4.-Dividir"

####################################FUNCION MULTIPLICACION##########
def multiplicacion():
	total=numero1*numero2
	print "El numero es" , total
##################################FUNCION DIVISION#################
def division():
	total=numero1/numero2
	print "El numero es" , total 	
####################################FUNCION RESTA####################
def resta():
	total=numero1-numero2
	print "El numero es" , total 
####################################FUNCION SUMA####################
def suma():
	total=numero1+numero2
	print "El numero es" , total 

####################################################################

while sortir== False:
	menu()
	tecla=raw_input("Introdice una opcion ")
	if tecla =="x" or tecla=="X":
		sortir = True 
	else:
		numero1=input("Introduce un numero ")
		numero2=input("Introduce un numero ")
		if tecla=="1":
			suma()
		if tecla=="2":
			resta()
		if tecla=="4":
			division()
		if tecla=="3":
			multiplicacion()
		
    
	
