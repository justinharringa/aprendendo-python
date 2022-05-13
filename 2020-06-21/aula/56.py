# 56 - Desenvolva um programa que leia o nome, idade, e sexo de
# 4 pessoas. No final do programa, mostre:
#  1. A média de idade do grupo
#  2. Qual é o nome do homem mais velho
#  3. Quantas mulheres têm menos de 20 anos
#
# https://youtu.be/cL4YDtFnCt4?t=1963
soma_de_idades = 0
idade_do_homem_mais_velho = 0
nome_de_homem_mais_velho = ''
mulher_jovem = 0
for pessoas in range(0, 4):
    idade = int(input("qual é sua idade? "))
    nome = input("Qual é seu nome? ")
    sexo = input("Qual é seu sexo (M/F)? ")
    soma_de_idades += idade
    if sexo == 'F' and idade < 20:
        mulher_jovem += 1
    if sexo == 'M' and idade > idade_do_homem_mais_velho:
        nome_de_homem_mais_velho = nome
        idade_do_homem_mais_velho = idade
media_de_idades = soma_de_idades / 4
print("media de idades: {}".format(media_de_idades))
if nome_de_homem_mais_velho != '':
    print("homem mais velho: {}".format(nome_de_homem_mais_velho))
print("mulheres com idade menos de 20: {}".format(mulher_jovem))