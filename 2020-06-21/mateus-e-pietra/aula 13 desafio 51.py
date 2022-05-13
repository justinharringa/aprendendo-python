# 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética.
# No final, mostre os 10 primeiros termos dessa progressão.
# exemplo - PA primeiro termo: 2, razão: 3
# aí vai imprimir:
# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29
# https://youtu.be/cL4YDtFnCt4?t=1778
primeiro_termo = int(input(' diga um número : '))
razão = int(input(' diga outro numero : '))
# dezinho_bolado = 30 ou 31(ou mais - mas não pode ser 32
# primeiro_termo = 2 + 9 * 3
# 2 + 27 = 29
#
dezinho_bolado = (primeiro_termo + 9 * razão) + 1
# dezinho_bolado = primeiro_termo + (10 - 1) * razão
for numero in range(primeiro_termo, dezinho_bolado, razão):
    print(numero)
# numero = primeiro_termo
# for alguma_coisa in range(10):
#     print(numero)
#     numero += razão