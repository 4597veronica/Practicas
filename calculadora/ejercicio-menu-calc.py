#coding:utf-8
print("suma:              1")
print("resta:             2")
print("multiplicación:    3")
print("división:          4")
print("salir:             5")
a = input("Selecciona una operación:")
if int(a) == 1:
	print("suma")
	b = input("primer número:")
	b = int(b)
	c = input("segundo número:")
	c = int(c)
	print("el resultado es:", b + c)
elif int(a) == 2:
	print("resta")
	b = input("primer número")
	b = int(b)
	c = input("segundo número")
	c = int(c)
	print("el resultado es:", b - c)


elif int(a) == 3:
        print("multiplicación")
        b = input("primer número")
        b = int(b)
        c = input("segundo número")
        c = int(c)
        print("el resultado es:", b * c)

elif int(a) == 4:
        print("división")
        b = input("primer número:")
        b = int(b)
        c = input("segundo número:")
        c = int(c)
        print("el resultado es:", b / c)

elif int(a) == 5:
        print("salir")
        

