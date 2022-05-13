# 55 - Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for x in range(1, 6):
    peso_da_pessoa = float(input('digite seu peso '))
    if x == 1:
        maior = peso_da_pessoa
        menor = peso_da_pessoa
    else:
        if peso_da_pessoa > maior:
            maior = peso_da_pessoa
        if peso_da_pessoa < menor:
            menor = peso_da_pessoa
print('o peso menor foi {} e o maior foi {}'.format(menor, maior))
#cade dia eles ficam mais dificeis