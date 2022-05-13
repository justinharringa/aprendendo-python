preço = 0
preço_total = 0
blá = ''
gleb = []
pedido = []
print('Lukepe: Eae mulekão!! Bem vindo ao restaurante do Lukepe')
print('Gleb: Eae mulekão!! Tem oq nesse cardápio?')
# mostrar o cardápio
while True:
    garçon_preço = [input('o que tem no cardápio garçon?: '), float(input('qual é o preço?: '))]
    # guardar o cardápio e o preço
    pedido.append(garçon_preço)
    # perguntar se tem mais coisa
    escolha = input('tem mais garçon? ')
    # se não tiver mais coisas fechar o loop
    if escolha == 'não':
        break
# analisar o cardápio
while True:
    print(f'Lukepe: essas são as opções mulekão!!: {pedido}')
    # escolher o que vai querer
    blá = input('Gleb: eu vou querer: ')
    gleb.append(blá)
    # perguntar se vai querer mais coisas
    escolhendo = input('Lukepe: Vai querer algo mais mulekão? ')
    # se não quiser fechar o loop
    if escolhendo == 'não':
        break
for tudo in pedido:
    # somar os preços dos pedidos
    if tudo[0] in gleb:
        preço_total += tudo[1]
print(f'Lukepe: seu pedido foi esse mulekão {gleb}, ele deu R${preço_total}')