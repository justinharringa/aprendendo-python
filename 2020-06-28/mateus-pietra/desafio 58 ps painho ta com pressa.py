# from random import randint
# computador = randint(0, 10)
from random import choice
computador = choice(list(range(10)))
contador_basiqueira_topssons_3000 = 0
palpite = 0
while palpite != computador:
    palpite = int(input('o computador escolheu um número tente adivinha-lo: '))
    contador_basiqueira_topssons_3000 += 1
    if palpite != computador:
        print('você errou! tente novamente')
print('parábens você acertou, levou {} vezes seu chato'.format(contador_basiqueira_topssons_3000))
