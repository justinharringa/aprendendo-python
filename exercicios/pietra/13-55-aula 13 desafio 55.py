p1 = 0
p2 = 0
for d in range(1, 6):
    peso = float(input('digite seu peso '))
    if d == 1:
        p1 = peso
        p2 = d
    else:
        if peso > d:
            p1 = peso
        if peso < d:
            p2 = peso
print('o peso menor foi {} e o maior foi {}'.format(p1, p2))
#cade dia eles ficam mais dificeis