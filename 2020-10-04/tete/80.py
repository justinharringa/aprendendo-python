# Usuario            Lista
# 3                  []
# 2                  [3]
# 4                  [2,3]
# 5                  [2,3,4]
# 1                  [2,3,4,5]
#                    [1,2,3,4,5]
numeros = []
for _ in range(5):
    print(f'a lista agora é: {numeros}')
    numero = int(input("me de um numero rapaz: "))
    lugar = len(numeros)
    for index, valor in enumerate(numeros):
        # se for menor, tem que colocar antes
        if numero < valor:
            lugar = index
            break
        # se for maior, tem que colocar antes
    numeros.insert(lugar, numero)
print(numeros)