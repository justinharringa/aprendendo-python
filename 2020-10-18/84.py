# Faça um programa que leia _nome e peso_
# de _varias pessoas_ guardando tudo em
# uma _lista_.
pesos_e_nomes = list()
while True:
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    pesos_e_nomes.append([nome, peso])
    # vamos sair assim
    continuar = input(f'Quer continuar? [s/n] ')
    if continuar == 'n':
        break

# print pra ajudar
print(f'Nomes e pesos: {pesos_e_nomes}')
#
# No final, mostre:
# 1. _Quantas_ pessoas foram cadastrados
# print(f'{len(pesos_e_nomes)} pessoas foram cadastrados')
# 2. Uma listagem com as pessoas mais _pesadas_
maior_peso = 0
### a. descrobrir o maior peso
for pessoa in pesos_e_nomes:
    print(f'---maior peso até agora é {maior_peso}')
    ##### I. accessa o peso da pessoa
    peso = pessoa[1]
    print(f'nome: {pessoa[0]}')
    print(f'peso: {peso}')
    ##### II. esse peso tá maior do que maior_peso que já encontramos??
    if peso > maior_peso:
        ##### III. caso sim, maior_peso = peso dessa pessoa
        maior_peso = peso
print(f'O maior peso é {maior_peso}')
### b. quais são as pessoas com esse peso
gordaos = list()
for pessoa in pesos_e_nomes:
    #### se peso for egual maior_peso, imprimir o nome
    if maior_peso == pessoa[1]:
        print(f'{pessoa[0]} é um gordao')
        gordaos.append(pessoa[0])
    else:
        print(f'{pessoa[0]} não é um gordao - tem peso de {pessoa[1]}')
print(f'os forties: {gordaos}')

# 3. Uma listagem com as pessoas mais _leves_
