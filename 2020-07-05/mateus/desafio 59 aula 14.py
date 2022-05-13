numero1 = int(input('me diga um numero: '))
numero2 = int(input('me diga um outro numero: '))
escolha = 0
while escolha != 5:
    print('''    (1) somar
    (2) multiplicar
    (3) maior
    (4) novos numeros
    (5) sair do programa''')
    escolha = int(input('qual é a sua escolha? '))
    if escolha == 1:
        soma = numero1 + numero2
        print('a resposta da soma é {}'.format(soma))
    elif escolha == 2:
        multiplicação = numero1 * numero2
        print('a resposta dessa multiplicação é {}'.format(multiplicação))
    elif escolha == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print('a resposta do maior numero é {}'.format(maior))
    elif escolha == 4:
        print('digite novamente')
        numero1 = int(input('me diga um numero: '))
        numero2 = int(input('me diga um outro numero: '))
    elif escolha == 5:
        print('tchauuuuu ')
    else:
        print('invalido, escreva outro')
print('acabou!!! ')
