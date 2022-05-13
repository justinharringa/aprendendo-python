# Faça um prorgrama que leia _nome a peso_
# de _varias pessoas_ guardando tudo em
# uma _lista_. No final, mostre:
# 1. _Quantas_ pessoas foram cadastrados
# 2. Uma listagem com as pessoas mais _pesadas_
# 3. Uma listagem com as pessoas mais _leves_
pessoas = []
continuar = 's'
mais_pesada = 0
mais_leve = 0
while continuar == 's':
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    continuar = input('Quer continuar? [S/N] ').lower()
    if len(pessoas) == 0:
        mais_leve = peso
        mais_pesada = peso
    else:
        if peso < mais_leve:
            mais_leve = peso
        if peso > mais_pesada:
            mais_pesada = peso
    pessoas.append([nome, peso])
print(f'Voce cadastrou {len(pessoas)} pessoas')
print(f'O peso maior foi de {mais_pesada}')
print(f'As pessoas com esse peso foram: ')
for pessoa in pessoas:
    if pessoa[1] == mais_pesada:
        print(pessoa[0])
print(f'O peso menor foi de {mais_pesada}')
print(f'As pessoas com esse peso foram: ')
for pessoa in pessoas:
    if pessoa[1] == mais_leve:
        print(pessoa[0])
