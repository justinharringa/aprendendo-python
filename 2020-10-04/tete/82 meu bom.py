vezes = int(input('quantos números vc quer digitar?: '))

todos_os_numeros = []
pares = []
impares = []
for c in range(vezes):
    valor = int(input('digite {}° número: '.format(c + 1)))
    todos_os_numeros.append(valor)
    print(f'valor é {valor}')
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# if todos_os_numeros[0] % 2 == 0:
#     pares.append(todos_os_numeros[0])
# else:
#     impares.append(todos_os_numeros[0])
# if todos_os_numeros[1] % 2 == 0:
#     pares.append(todos_os_numeros[1])
# if todos_os_numeros[2] % 2 == 0:
#     pares.append(todos_os_numeros[2])
# if todos_os_numeros[3] % 2 == 0:
#     pares.append(todos_os_numeros[3])
# if todos_os_numeros[4] % 2 == 0:
#     pares.append(todos_os_numeros[4])
#
# if not todos_os_numeros[1] % 2 == 0:
#     impares.append(todos_os_numeros[1])
# if not todos_os_numeros[2] % 2 == 0:
#     impares.append(todos_os_numeros[2])
# if not todos_os_numeros[3] % 2 == 0:
#     impares.append(todos_os_numeros[3])
# if not todos_os_numeros[4] % 2 == 0:
#     impares.append(todos_os_numeros[4])
print('esses foram os números digitados: {}'.format(todos_os_numeros))
print('esses foram os pares digitados: {} '.format(pares))
print('esses foram os ímpares digitados: {} '.format(impares))