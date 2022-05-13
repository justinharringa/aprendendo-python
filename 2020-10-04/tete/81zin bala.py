vezes = int(input('quantos números vc quer digitar?: '))
lista = []
total = 0
for c in range(vezes):
    numero = int(input('digite um número: '))
    total += numero
    lista.append(numero)
print(f'depois do laço: {total}')
if 5 in lista:
    print('tem cinco na lista')
else:
    print('não tem cinco na lista')
print(lista)
print(lista.sort(reverse=True))
print(lista)
print('descending 1: {}'.format(reversed(sorted(lista))))
for index, valor in enumerate(reversed(sorted(lista))):
    print('valor {}: {}'.format(index, valor))
print('descending 2: {}'.format(sorted(lista, reverse=True)))
print('foram digitados {} números'.format(len(lista)))
