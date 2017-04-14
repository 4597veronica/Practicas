#coding:utf-8

#En este codigo coimpararemos dos numeros

numero1=input ("Introduce el primer numero: ")

numero2=input ("Introduce el segundo numero: ")

if numero1<numero2:
	print "El numero", numero2, "es mas grande que el numero" ,numero1
else :
	if numero1>numero2:
		print "El numero", numero1, "es mas grande que el numero" ,numero2
	else:
		print "Los numeros son iguales"
