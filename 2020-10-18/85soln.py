# Crie um programa onde o usuario possa
# digitar _sete valores numericos_ e
# cadastre-os em uma _lista unica_ que mantenha
# separados of valores _pares_ e _impares_
# No final, mostre os valores pares e impares
# em ordem crescente
print('Me de sete valores por favor')
valores = [[], []]
for num in range(7):
    valor = int(input(f'Me de valor {num + 1}: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'Beleza na Veneza? Os pares são: {sorted(valores[0])}')
print(f'Os impares são: {sorted(valores[1])}')
