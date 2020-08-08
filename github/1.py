def es_bisiesto(agnio):
    if agnio % 400 == 0:
        return True
    elif agnio % 100 == 0:
        return False
    elif agnio % 4 == 0:
        return True
    else:
        return False

agnio = 1900
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))
agnio = 2000
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))
agnio = 2016
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))
agnio = 2016
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))
agnio = 1987
print('¿El año %i es bisiesto?: %s' % (agnio, es_bisiesto(agnio)))


