#coding:utf-8
# Haremos un menu de una calculadora

print "¿Que desea hacer amo?"

print "S.-salir"

print "1.-Sumar"

print "2.-Restar"

print "3.-Multiplicar"

print "4.-Dividir"

obcion=raw_input ("Introduce una obcion: ")


		#if not obcion>=1 and obcion<=4:
			
if obcion == "s" : 
    print "Introduce una S mayuscula"
else : 
	if not obcion>="1" and obcion<="4" :
		print "Esa opción no existe"

