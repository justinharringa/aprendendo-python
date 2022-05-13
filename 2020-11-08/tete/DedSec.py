preço = 0
preço_total = 0
blá = ''
gleb = []
pedido = []
print('Lukepe: Eae mulekão!! Bem vindo ao restaurante do Lukepe')
print('Gleb: Eae mulekão!! Tem oq nesse cardápio?')
while True:
    garçon_preço = [input('o que tem no cardápio garçon?: '), float(input('qual é o preço?: '))]
    pedido.append(garçon_preço)
    escolha = input('tem mais garçon? ')
    if escolha == 'não':
        break
while True:
    print(f'Lukepe: essas são as opções mulekão!!: {pedido}')
    blá = input('Gleb: eu vou querer: ')
    gleb.append(blá)
    escolhendo = input('Lukepe: Vai querer algo mais mulekão? ')
    if escolhendo == 'não':
        break
for tudo in pedido:
    if tudo[0] in gleb:
        preço_total += tudo[1]
print(f'Lukepe: seu pedido foi esse mulekão {gleb}, ele deu R${preço_total}')