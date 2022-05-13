soma = 0
contador = 0
número_boladasso_da_pepudex = 0
while True:
    número_boladasso_da_pepudex = int(input('digite um número: '))
    if número_boladasso_da_pepudex == 999:
        break
    contador += 1
    soma += número_boladasso_da_pepudex
print('obrigado por jogar, você fez {} tentativas para digitar o número 999'.format(contador))
print('essa é a soma dos números que você digitou {}'.format(soma))