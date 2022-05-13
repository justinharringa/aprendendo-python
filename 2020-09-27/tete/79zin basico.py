pergunta = int(input('quantos números vc vai digitar? '))
lista = []
copia = lista
print('lista: {}, copia: {}, tio jota: surfista que nunca surfou ;-;'.format(lista, copia))
for x in range(pergunta):
    o_numero = int(input('digite um número: '))
    if o_numero in lista:
        print('caraca, {} tá na lista já safado'.format(o_numero))
    if o_numero not in lista:
        lista.append(o_numero)
    print('no {} lista ficou assim: {}'.format(x, lista))
    copia == lista
    print('no {} copia ficou assim: {}'.format(x, copia))
# if copia == lista:
#     print('copia é: {} lista é: {}'.format(copia, lista))
#     lista.remove(copia)
print('lista: {}'.format(lista))
print('lista sorted: {}'.format(sorted(lista)))
print('copia: {}'.format(copia))