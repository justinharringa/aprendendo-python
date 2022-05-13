# 53 - Crie um programa que leia uma frase qualquer e diga se ela é um
# palindromo, desconsiderando os espaços (não usam accentos de qq jeito... só vai complicar)
# https://youtu.be/cL4YDtFnCt4?t=1858
frase = str(input(' escreva uma frase : '))
separando = frase.split()
vamo_juntar = ''.join(separando)
ao_contrario = ''
for bla in range(len(vamo_juntar) - 1, -1, -1):
    ao_contrario += vamo_juntar[bla]
if ao_contrario == vamo_juntar:
    print('É uma palíndromo que top!')
else:
    print('Não é palíndromo kkkk ;-;')