# Faça uma programa que leia alguns números:
# 1. Aonde vamos começar
# 2. Aonde vamos parar
# 3. Número dividido
# Vamos ver QUANTOS números são divisivel pelo terceiro numero
começar = int(input("Digite aonde vamos começar: "))
parar = int(input("Digite aonde vamos parar: "))
dividido = int(input("Digite o número que sera dividido: "))

contador = 0
# quantos numeros de começar até parar:
for numero in range(começar, parar + 1):
    print("numero:", numero)
    # Google
    if numero != 0 and numero % dividido == 0:
        print("é divisivel!")
        contador += 1
    #  dividir pelo dividido e ver se o restante é 0
    #  - talvez precisamos de um variavel?
    #  - se o restante for 0, adicionar na contador
print("{} números são divisiveis pelo {}".format(contador, dividido))