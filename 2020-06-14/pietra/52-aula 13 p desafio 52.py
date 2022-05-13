# 52 - Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
numero = int(input('digite um numero : '))
numero_e_primo = True
# só é primo se é divisivel pelo 1 e ele mesmo
for numero_considerado in range(2,  numero):
    # print("numero: {}".format(numero_considerado))
    if numero % numero_considerado == 0:
        print("não é primo safado pq {}".format(numero_considerado))
        numero_e_primo = False

if numero_e_primo:
    print("{} é primo!".format(numero))
else:
    print("{} não é primo :'(".format(numero))