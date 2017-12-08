# coding: utf-8
edad=input("Indique su edad ")
if edad >=18 and edad <=23:
    print "Puedes pasar"
    print "Te pertenece la sesión de jovenes"
else:
    if edad <18:
        print "Menores, no"
    else: 
        if edad >23:
            print "Solo entre 18 y 23"

# coding: utf-8
edad=input("Indique su edad ")
if edad >=18 and edad <=23 or edad == 17:
    print "Puedes pasar"
    print "Te pertenece la sesión de jovenes"
else: 
    if edad >23:
        print "Pasa a todas las sesiones"
    else: 
        if edad <18:
            print "Eres menor, no puedes pasar"
