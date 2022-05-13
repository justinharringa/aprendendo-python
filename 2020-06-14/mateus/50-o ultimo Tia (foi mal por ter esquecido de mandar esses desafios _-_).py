# 50 - Desenvolva u programa que leia seis números inteiros e
# mostra a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.
soma = 0
contar = 0
for j in range(1, 7):
    n = int(input('digite um número '))
    if n % 2 == 0:
        soma += n
        contar += 1
print('pelos {} números que foram pares que você falou a soma vai dar {}'.format(contar, soma))
#tia esse eu só entendi depois do Guanabra fazer mas entendi de vez agora :)