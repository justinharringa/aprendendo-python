dinheiro = int(input('Quanto será sacado? '))
total = dinheiro
contar_as_cedulas = 0
cedula = 50
while True:
    if total >= cedula:
        total -= cedula
        contar_as_cedulas += 1
    else:
        if contar_as_cedulas > 0:
            print('Serão {} cedulas de {}'.format(contar_as_cedulas, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if cedula == 0:
            break
print('tchauuuuuu!  ')
#tio j esse ta impossivel