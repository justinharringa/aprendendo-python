soma_dos_numeros = 0
valor = 0
for P in range(6, 12):
    number = int(input('digite um número '))
    soma_dos_numeros += number
    valor += 1
print('pelos {} números que você falou a soma vai dar {}'.format(valor, soma_dos_numeros))