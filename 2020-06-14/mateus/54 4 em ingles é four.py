# 54 - Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já são maiores.
pessoas_de_maior_idade = 0
for c in range(1, 8):
    idade = int(input('digite a sua idade '))
    if idade < 18:
        print('você não está na maior idade ainda')
    else:
        pessoas_de_maior_idade = pessoas_de_maior_idade + 1
        print('você está na maior idade')
print('o número de pessoas q estão na maior idade é igual a {}'.format(pessoas_de_maior_idade))
#tio eu não estou conseguindo mostra na tela o número de pessoas acima da idade ;-;