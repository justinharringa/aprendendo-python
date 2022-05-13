m1 = 0
m2 = 0
for d in range(1, 6):
    peso = float(input('digite seu peso '))
    if d == 1:
        m1 = peso
        m2 = peso
    else:
        if peso > m1:
            m1 = peso
        if peso < m2:
            m2 = peso
print('o maior peso foi {} e menor foi {}'.format(m1, m2))
#consegui fazer esse com o guanabara mas eu ainda quero entender umas coisinhas
