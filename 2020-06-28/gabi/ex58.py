from random import randint
computador = randint(0, 10)
print('digite um numero de 0 a 10 !!!')
acertou = False
palpites = 0
while not acertou:
  jogador= int(input('qual seu palpite?'))
  palpites += 1
  if jogador == computador:
    acertou = True
  else:
       if jogador < computador:
         print('mais tente denovo')
       elif jogador > computador:
         print('menos tente denovo')  
print('voce acertou com {}'.format(palpites))

