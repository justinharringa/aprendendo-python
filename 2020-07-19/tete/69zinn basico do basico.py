contador3 = 0
contador = 0
contador1 = 0
while True:
    pergunta1 = input('qual é seu sexo? ')
    pergunta2 = int(input('qual é sua idade? '))
    pergunta_final = input('quer continuar? ')
    if pergunta1 == 'masculino':
        contador += 1
    if pergunta2 >= 18:
        contador1 += 1
    if pergunta1 == 'feminino' and pergunta2 < 20:
        contador3 += 1
    if pergunta_final == 'não':
        break
print('Com essa pesquisa podemos notificar que dos entrevistados temos {} homens, {} maiores de idade e {} mulheres com menos de 20 anos'.format(contador, contador1, contador3))