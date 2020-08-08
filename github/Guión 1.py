print ("Años bisiestos")
fecha = int(input("Escriba el año y le diré es bisiesto: "))

if fecha %400== 0 or (fecha % 100 != 0 and fecha % 4 == 0):
    print("verdadero. ")
else:
    print("falso. ")
