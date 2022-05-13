m1 = 0
m2 = 0
for d in range(1, 6):
    peso = float(input('digite seu peso '))
    if d == 1:
        m1 = peso
        m2 = d
    else:
        if peso > d:
            m1 = peso
        if peso < d:
            m2 = peso
print('o menor peso foi {} e maior foi {}'.format(m1, m2))

