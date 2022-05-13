jota = 800000.0
leta = 100000.0
jota_com_1000 = jota
leta_com_1000 = leta
for month in range(24):
    print(f'jota com 1000: {jota_com_1000:.2f}')
    print(f'leta com 1000: {jota_com_1000:.2f}')
    jota_com_1000 += 1000
    leta_com_1000 += 1000
    interest = 1 + (0.04 / 12)
    jota_com_1000 = jota_com_1000 * interest
    jota = jota * interest
    leta_com_1000 = leta_com_1000 * interest
    leta = leta * interest
    print(f'month: {month}')
    jota_total = jota_com_1000 + leta
    print(f'jota take 1000: jota: {jota_com_1000:.2f} leta: {leta:.2f} total = {jota_total:.2f}')
    leta_total = jota + leta_com_1000
    print(f'leta take 1000: jota: {jota:.2f} leta: {leta_com_1000:.2f} total = {leta_total:.2f}')
    print(f'esse total tá egual? {round(jota_total, 2) == round(leta_total, 2)}')

