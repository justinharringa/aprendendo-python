import random
lista = ['tigree', 'tapioca', 'booné', 'floor', 'sacola']
escolhido = []
contador = 0
contador1 = 0
contador_geral = 0
escolhido.append(random.choice(lista))
print('vai começar o jogo da forca!!')
print(escolhido)
while True:
    pergunta2 = input('diga uma letra: ')
    contador_geral = contador1 + contador
    if pergunta2 in escolhido[0]:
        times = 0
        for letra in escolhido[0]:
            if letra == pergunta2:
                times += 1
        contador1 += times
        print(f'você acertou!! falta {len(escolhido[0])-contador1} letras')
    else:
        contador += 1
        print('você errou!! se vc perder 6 vidas vc perde o jogo')
    if contador1 == len(escolhido[0]):
        print(f'você ganhou!! vc jogou {contador_geral + 1} vezes')
        break
    if contador == 6:
        print(f'você perdeu!! vc jogou {contador_geral + 1} vezes')
        break