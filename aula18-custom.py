# Vc vai num restaurante pequeno e o restaurante não tem cardapio
#
# 1. Vc vai perguntar o dono do restaurante quais são os pratos e os precos e vai guardar numa lista pra lembrar
## a. cada prato tem um nome e preço
## b. vc vai perguntar o dono do restaurante se ele tem mais pratos (s/n)
# 2. Quando o dono não tem mais pratos disponiveis, pode pedir você quer entre as opções
## a. o que vc quer dessas opções (imprimir as opções)
## b. guardar o nome do item numa lista
## c. perguntar se eles querem mais itens (s/n)?
# No final, mostra o preço total que eles pediram


print('Dono do restaurante: Seja bemvindo ao restaurante do surfista!')
print('Jovem: E aí rapaz? Vc tem o que hoje nesse restaurante? Tô com fome!')
continuar = 's'
opcoes = []
while continuar == 's':
    item = input('       Me de o nome do prato garçon: ')
    preco = float(input('       Certo, qual é o preço: '))
    continuar = input('       Tem mais garçon? (s/n) ')
    opcoes.append([item, preco])

continuar = 's'
jovem_pratos = []
while continuar == 's':
    print(f'Dono: então... as opções são: {opcoes}')
    item = input('Jovem: Eu acho que vou querer: ')
    continuar = input('Dono: Certo, vai querer mais? (s/n) ')
    jovem_pratos.append(item)

print(f'Dono: beleza rapaz... vc pediu: {jovem_pratos}')
total = 0.0
for prato in jovem_pratos:
    for opcao in opcoes:
        if opcao[0] == prato:
            total += opcao[1]
print(f'Dono: aí o total seria: {total}')
