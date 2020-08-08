from calendar import monthrange

def cantidad_dias_mes(mes, agnio):
    return monthrange(agnio, mes)[1]

print(cantidad_dias_mes(2, 2020))
print(cantidad_dias_mes(2, 2021))
print
