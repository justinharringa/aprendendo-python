prato_principal = '''
1. camarao na moranga
2. carneiro
3. churras
'''
prato_secundario = '''
1. file a parmigiana
2. arroz com feijão
3. sopa de cogumelo
4. espetinho de coração
'''
cardapio = ''

bebidas = '''
1. milkshake de chiclete
2. suco de mangaba
3. guarana
4. coca
'''

sobremesas = '''
1. mouse de maracuja
2. petit gateu
'''
escolhas = '''
1. sobremesa
2. prato principal
3. prato secondario
4. bebidas
5. sair
'''

# se ele digita sobremesa
while True:
    print(escolhas)
    escolha = input("o que vc vai querer hj? ")
    if escolha == '1':
        print('''%s''' % sobremesas)
        opcao = input('qual vc vai querer? ')
        if opcao == '1':
            cardapio += 'mouse de maracuja\n'
        elif opcao == '2':
            cardapio += 'petit gateu\n'
        else:
            print('nao sei o que vc bebeu... tais bebado')
    elif escolha == '2':
        print(prato_principal)
        opcao = input('qual vc vai querer? ')
        if opcao == '1':
            cardapio += 'camarao na moranga\n'
        elif opcao == '2':
            cardapio += 'carneiro\n'
        elif opcao == '3':
            cardapio += 'churras\n'
        else:
            print('ta doidinho hein?')
    elif escolha == '3':
        print(prato_secundario)
        opcao = input('qual vc vai querer? ')
        if opcao == '1':
            cardapio += 'file a parmigiana\n'
        elif opcao == '2':
            cardapio += 'arroz com feijão\n'
        elif opcao == '3':
            cardapio += 'sopa de cogumelo\n'
        elif opcao == '4':
            cardapio += 'espetinho de coração\n'
        else:
            print('ta doidinho hein?')
    elif escolha == '4':
        print(bebidas)
        opcao = input('qual vc vai querer? ')
        if opcao == '1':
            cardapio += 'milkshake de chiclete\n'
        elif opcao == '2':
            cardapio += 'suco de mangaba\n'
        elif opcao == '3':
            cardapio += 'guarana\n'
        elif opcao == '4':
            cardapio += 'coca\n'
        else:
            print('ta maluco doido?')
    elif escolha == '5':
        break
print("cardapio:\n{}".format(cardapio))