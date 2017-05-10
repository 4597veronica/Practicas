# coding:utf-8


mes=input("Introduce el numero del mes ")
year=input("Introduce el año ")
filas=0
columnas=0
def my_range(inici, fi, increment):
	while inici <= fi:
		#Retorna l'element actual del rang (llista)
		yield inici
		inici = inici + increment
contador=1
#Si el mes es alguno de los que tienen treita dias
if mes==4 or mes==6 or mes==9 or mes==11: 
	tope=30

if mes==2:
		#Si el año es bisiesto(multiplo de cuatro)
		if year%4==0:
			tope=29
		else: 
			tope=28
#Si no es ninguno de los anterioeres casos, es un mes con 31 dias
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10: 
	tope=31
print " L  M  X  J  V  S  D"
for filas in my_range(1,6,1):
	for columnas in my_range(1,7,1):
		if contador<=tope:
			if contador<=9: #Este if esta hecho para cuadrar los numeos.
				print "",contador,
			else:
				print contador ,
		contador=contador+1
	print " "
