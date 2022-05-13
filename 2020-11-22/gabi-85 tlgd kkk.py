varyavels = 0
numbers = []
number_par = []
number_impar = []
# criar uma lista para pegar os números
for x in range(7):
    number = int(input('digite um número: '))
    # pegar os ímpars e os pares
    if number % 2 == 0:
        number_par.append(number)
    if number % 2 == 1:
        number_impar.append(number)
numbers.append(number_par)
numbers.append(number_impar)
print(f'esses os pares digitados: {numbers[0]} e esses foram os impares: {numbers[1]}')