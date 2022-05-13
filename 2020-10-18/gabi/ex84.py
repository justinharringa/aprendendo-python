print('turo bão povo nois vai fazer hj e joga o joguinho ex84 ta bão bora la ne vem com gaby que susseso')
print('.......................................................................................................................................................')
informaçoes = []
peso = []
while True:
   informaçoes.append(input('qual seu nome moç(a)?:  '))
   peso.append(float(input('qual seu peso fio?:  ')))
   cnt = input('quer continuar? [sim/não]')
   print(f'oq  vc colocou foi: {peso} e {informaçoes}')
   print(len(informaçoes))
   if cnt == 'não':
        break
maximo = max(peso)
print(f'o maior peso foi: {maximo}')
minimo = min(peso)
print(f'o menor peso foi: {minimo}')