#é o 52 :D
x = int(input('digite um número '))
total = 0
for c in range(1, x + 1):
    total += 1
    if x % c == 0:
        print('ele é primo')
    else:
        print('ele não é primo')
