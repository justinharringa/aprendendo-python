contador2 = 0
contador3 = 0
contador1 = 0
while True:
    sexo = input('qual é seu sexo? m/f: ')
    anos = int(input('quantos anos você tem? '))
    final = input('você quer continuar? ')
    if sexo == 'm':
        contador3 += 1
    if anos >= 18:
        contador1 += 1
    if sexo == 'f' and anos < 20:
        contador2 += 1
    if final == 'não':
        break
print(' temos {} homens, {} maiores de idade e {} mulheres que tem menos de 20 anos de idade'.format(contador3, contador1, contador2))