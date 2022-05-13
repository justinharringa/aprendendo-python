maior = -9999
roupa = ['calca', 'camisa', 'chapeu']

for index, valor in enumerate(roupa):
    print('chegou na {}'.format(index))
    if valor == 'camisa':
        print('eita! achamos a {} no index {}'.format(valor, index))

numeros = [34, 2, 49, 28, 19, 3, 23, 34]
index = 0
for valor in numeros:
    print('agora é {}'.format(valor))
    if maior < valor:
        print('caraca! {} < {}'.format(maior, valor))
        maior = valor
    index += 1

print(maior)

roupas = [('camisa', 50), ('calca chaves', 20)]
for valor in roupas:
    print('price of {} is {}'.format(valor[0], valor[1]))
