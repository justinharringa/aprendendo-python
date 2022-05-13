oiii = []
preço = 0
preço_inteiro = 0
# apresentar o restaurante
print('dono do restaurante: seja bemvindo ao restaurante do surfista')
print('jovem: e ai rapaz? vc tem o que hoje nesse restaurante? tô com fome!')
# dá o cardapio
while True:
    # pedir o prato do dia
    prato = input('me de o nome do prato garçon: ')
    # pedir o preço
    preço = input('certo, qual é o preço: ')
    # perguntar se tem mais pratos
    pratos = input('tem mais garçon? (s,n) ')
    # acrescentar o prato e o preço numa lista
    oiii.append(prato)
    oiii.append(preço)
    if pratos == 'n':
        break
# dá as opções
print(f'dono: então... as opções são: {oiii}')
while True:
