anio=int(input("Año:"))
if anio%4 == 0:
    if anio%100 != 0 or anio%400 == 0:
        print("Bisiesto")
    else:
        print("No bisiesto")
else:
    print("No bisiesto")
