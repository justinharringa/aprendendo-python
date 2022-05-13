from random import randint
desaf1 = randint(0, 10)
desaf2 = 0
desaf3 = ''
desaf4 = ''
escolha = 0
opção = 0
mais_uma_escolha = 0
perg1 = ''
perg2 = ''
perg3 = ''
perg4 = ''
perg5 = ''
contador = 0
while escolha != 5:
    print('''
    1. desafio do número aleátorio
    2. desafio da charáda dos números
    3. desafio do enigma
    4. desafio do quiz
    5. sair''')
    escolha = int(input('oq vc vai querer jogar hj? '))
    if escolha == 1:
        opção = (input('escolha um número de 1 a 10 '))
        if opção == desaf1:
            print('parabéns vc acertou!!')
        else:
            print('vc errou')
        mais_uma_escolha = input('vc quer jogar mais uma vêz? ')
        if mais_uma_escolha == 'sim':
            while mais_uma_escolha != 'não':
                opção = (input('escolha um número de 1 a 10 '))
                if opção == desaf1:
                    print('parabéns vc acertou!!')
                else:
                    print('vc errou')
                mais_uma_escolha = input('vc quer jogar mais uma vêz? ')
    if escolha == 2:
        print('vamos ver se vc consegue compreender essa charada hehehehehheheh')
        print('a charáda é o seguinte eu tenho um número, o antecessor desse número multiplicado pelo sucessor desse número menos esse número vai dar 3905')
        opção = int(input('digite esse número da charáda: '))
        if opção == 63:
            print('parabéns vc acertou!!')
        else:
            print('vc errou tente novamente!!!')
    if escolha == 3:
        print('o enigma é......... O que é? O que é? Que corre deitado e dorme em pé?')
        opção = input('digite a resposta: ')
        if opção == 'pé':
            print('parabéns filho do Einstein!!! Sobrinho do Elon Musk!!! Neto de Nikola Tesla!!!')
        else:
            print('vc errou!!!')
            mais_uma_escolha = input('vc quer jogar mais uma vêz? ')
            if mais_uma_escolha == 'sim':
                while mais_uma_escolha != 'não':
                    print('O enigma, como vc já sabe, é o que corre deitado e dorme em pé? ')
                    opção = input('digite a resposta: ')
                    if opção == 'pé':
                        print('parabéns entiado do Einstein!!! Sobrinho distante do Elon Musk!!!')
                    else:
                        print('vc errou tente denovo!!!')
                        mais_uma_escolha = input('vc quer jogar mais uma vêz? ')
    if escolha == 4:
        print('Bem vindo ao quiz mais dificil do multiverso meu amigo!!! ehhehehhehehhehehhehehhe')
        perg1 = input('1° pergunta: Qual é a capital da Indía? ')
        if perg1 == 'Nova Delhi':
            print('parabéns vc acertou!!')
        else:
            print('Tu errou macho!!!')
            contador += 1
        perg2 = input('2° pergunta: Qual é a cidade onde o mundialmente famoso surfista Tio Justin mora? ')
        if perg2 == 'São Francisco':
            print('parabéns vc acertou!!')
        else:
            print('Tu errou macho!!!')
            contador += 1
        perg3 = input('3° pergunta: Qual é o melhor time do mundo? e pq é o Nautico? ')
        if perg3 == perg3 :
            print('parabéns vc acertou!!')
        if perg3 == 'sport':
            print('Foi mal mas eu aceitava qualquer resposta menos essa!!!!!')
            contador += 1
        perg4 = input('4° pergunta: Qual é o estado onde o artista br Tio Lú mora? ')
        if perg4 == 'Pernambuco' :
            print('parabéns vc acertou!!')
        else:
            print('Tu errou macho!!!')
            contador += 1
        perg5 = input('5° pergunta: Qual é o nome da maior manobra de surf do mundo? Back Flip Invertido ao Contrario ou Girosflin? ')
        if perg5 == 'Back Flip Invertido ao Contrario':
            print('parabéns vc acertou!!')
        else:
            print('Tu errou macho!!!')
            contador += 1
        print('em todo esse quiz vc errou {} e acertou {}'.format(contador, 5 - contador))
    if escolha == 5:
        break
