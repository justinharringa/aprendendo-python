pietra = 0
for x in range(1, 7):
    livy = int(input('digite a sua idade '))
    if livy < 18:
        print('você não está na maior idade ainda')
    else:
        pietra = pietra + 1
        print('você está na maior idade')
print('o número de pessoas q estão na maior idade é igual a {}'.format(pietra))