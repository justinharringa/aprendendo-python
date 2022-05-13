aleatoriedade_aleatoria = [int(input('digite um número: ')), int(input('digite um número: ')), int(input('digite um número: ')), int(input('digite um número: ')), int(input('digite um número: '))]
maior = -99999999999999999999
menor = 99999999999999999999
contador_menor = 0
contador_maior = 0
maior_tupla = (maior, 0)
menor_tupla = (menor, 0)
for contador, valor in enumerate(aleatoriedade_aleatoria):
    print('index: {}, valor: {}'.format(contador, valor))
    if valor > maior:
        print('maior rapaz: {}'.format(valor))
        maior = valor
        contador_maior = contador
        maior_tupla = (valor, contador)
    if valor < menor:
        print('menor rapaz: {}'.format(valor))
        menor = valor
        contador_menor = contador
        menor_tupla = (valor, contador)
print('esses foram os números digitados: {} {} {} {} {}'.format(aleatoriedade_aleatoria[0], aleatoriedade_aleatoria[1], aleatoriedade_aleatoria[2], aleatoriedade_aleatoria[3], aleatoriedade_aleatoria[4]))
print('esse foi o maior número: {} e ele foi {}° digitado '.format(maior, contador_maior + 1))
print('esse foi o menor número: {} e ele foi {}° digitado '.format(menor, contador_menor + 1))
print('maior: {} index: {}'.format(maior_tupla[0], maior_tupla[1]))
print('menor: {} index: {}'.format(menor_tupla[0], menor_tupla[1]))