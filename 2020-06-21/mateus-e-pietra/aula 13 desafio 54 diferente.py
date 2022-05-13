# 54 - só que vocês tem que receber o ano de nascimento e calcular a idade - Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já são maiores.
import datetime
now = datetime.datetime.now()
maiores = 0
for p in range(7):
    ano = int(input(' diga o seu ano de nacimento : '))
    if ano <= (now.year - 18):
        print('você é maior de idade ')
        maiores += 1
    else:
        print('você é menor de idade ')
print("numero de pessoas maior de idade: {}".format(maiores))
