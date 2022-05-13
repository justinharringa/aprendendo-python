peso_e_nomes = []
peso = []
nomes2 = []
nomes = []
mais_pesado = -999999999999999
menos_pesado = 9999999999999
contador2 = 0
lista = []
gordalhasos = []
magrins = []
# pegar o nome e o peso
while True:
    nome_pesos = [input('digte seu nome: '), int(input('digite seu peso: '))]
    # acrescentar os pesos e os nomes em uma lista
    lista.append(nome_pesos)
    # ver se vai ter mais pessoas
    pergunta = input('vc quer continuar? ')
    contador2 += 1
    # se não tiver mais pessoas fechar o loop
    if pergunta == 'não':
        break
print(lista)
for iuris in lista:
    # analisar a lista, pegando o menor e o maior
    peso = iuris[1]
    if peso > mais_pesado:
        mais_pesado = peso
        nomes = iuris[0]
    if peso < menos_pesado:
        menos_pesado = peso
        nomes2 = iuris[0]
    if mais_pesado == peso:
        gordalhasos.append(iuris[0])
    if menos_pesado == peso:
        magrins.append(iuris[0])
#for peso_e_nomes in range(mais_coisas):
#    if peso_e_nomes[1 + mais_coisas] > mais_pesado:
#        mais_pesado = peso_e_nomes[1]
#    if peso_e_nomes[1 + mais_coisas] < menos_pesado:
#        menos_pesado = peso_e_nomes[1 + contador2]
print(f'{mais_pesado}kg foi o maior peso encontrado' , f'pesadões: {gordalhasos}')
print(f'{menos_pesado}kg foi o menor peso encontrado', f'magrins: {magrins}')
#for gente in peso_e_nomes:
 #   mais_coisas_ainda = mais_coisas
  #  if muito_mais_coisas > mais_pesado:
#print(f'tá ai o maior peso {mais_pesado[1]}')

