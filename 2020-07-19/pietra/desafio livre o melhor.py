print('bem vindo a loja de roupas femininas "MARESSA" ')
valor = 0
opção = 0
blusas = 0
shorts = 0
calças = 0
vestidos = 0
escolha = 0
total = blusas, shorts, calças, vestidos
while escolha != 5:
    print('nós vendemos: ')
    print('''
    1-blusa
    2-short
    3-calça
    4-vestido
    5-sair''')
    escolha = int(input('oque você vai levar: '))
    if escolha == 1:
        print('''
        [1] blusa do mickey. usada pela esposa de waltdisney.custando apenas $991.000
        [2] blusa listrada preta e branca. $20
        [3] blusa com flocos de neve. usada e autografada pela elsa. por ser uma princesa conhecida mundialmente esta valendo $10000000''')
        opção = int(input('qual você vai querer? '))
        if opção == 1:
            blusas = 'blusa do mickey'
            valor += 991000
        if opção == 2:
            blusas = 'blusa listrada'
            valor += 20
        if opção == 3:
            blusas = 'blusa com flocos'
            valor += 10000000
    if escolha == 2:
        print('''
        [1] short preto basico. valendo $10
        [2] short jeans tumbler. como esta na moda vai custar um pouco mais caro. valendo $50
        [3] short saia. valendo $35''')
        opção = int(input('qual voce quer? '))
        if opção == 1:
            shorts = 'short preto'
            valor += 10
        if opção == 2:
            shorts = 'short tumbler'
            valor += 50
        if opção == 3:
            shorts = 'short saia'
            valor += 35
    if escolha == 3:
        print('''
        [1] calça jeans. valendo $30
        [2] calça legging. valendo $20''')
        opção = int(input('qual vc vai comprar? '))
        if opção == 1:
            calças = 'calça jeans'
            valor += 30
        if opção == 2:
            calças = 'calça legging'
            valor += 20
    if escolha == 4:
        print('''
        [1] vestido de tubo. valendo $35
        [2] vestido largo. valendo $25
        [3] vestido longo.valendo $40''')
        opção = int(input('oq tu quieres?'))
        if opção == 1:
            vestidos = 'tubo'
            valor += 35
        if opção == 2:
            vestidos = 'largo'
            valor += 25
        if opção == 3:
            vestidos = 'longo'
            valor += 40
    if escolha == 5:
        break
print('tchauuuu!o valor dessa compra foi ${}.00'.format(valor))
