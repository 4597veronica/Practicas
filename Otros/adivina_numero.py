#coding:utf8

oculto = input("El número que hay que adivinar: ")

contador = 1
import os
os.system('clear') 

num1 = input("Adivina que nombre oculto: ")

while num1 != oculto :
    
    if num1 > oculto :
        print "Te has pasado, es algo menos"
    if num1 < oculto :
        print "Te quedaste corto, es algo mas"
    contador = contador +1
    num1 = input("Vuelve a intentarlo: ")
if num1 == oculto :
    print "Lo has adivinado en " , contador , "intentos"
