#coding:utf-8

#Este programa sera una calculadora sencilla
###############################VARIABLES############################
sortir=False
total=0
###############################MOSTRAR MENU#########################
def menu():
	print "¿Que desea hacer amo?"

	print "S.-salir"

	print "1.-Sumar"

	print "2.-Restar"

	print "3.-Multiplicar"

	print "4.-Dividir"

####################################FUNCION MULTIPLICACION##########
def multiplicacion(a,b):
	total=a*b
	return total 
##################################FUNCION DIVISION#################
def division(a,b):
	total=a/b
	return total 
####################################FUNCION RESTA####################
def resta(a,b):
	total=a-b
	return total 	
####################################FUNCION SUMA####################
def suma(a,b):
	total=a+b
	return total 
####################################################################

while sortir== False:
	menu()
	tecla=raw_input("Introdice una opcion ")
	if tecla =="s" or tecla=="S":
		sortir = True 
	else:
		numero1=input("Introduce un numero ")
		numero2=input("Introduce un numero ")
		if tecla=="1":
			print suma(numero1,numero2)
		if tecla=="2":
			total=resta(numero1,numero2)
		if tecla=="4":
			print division(numero1,numero2)
		if tecla=="3":
			print multiplicacion(numero1,numero2)
		
	
		
