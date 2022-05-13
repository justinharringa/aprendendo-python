
# perguntar se quer continuar pra acrescentar mais pessoas
# criar a lista pra as pessoas pra todas as rodadas do laço
pepolino = []
while True:
    # pegar o nome da pessoa
    nome = input('qual o seu nome? ')
    # pegar e peso da pessoa
    peso = int(input('qual seu peso? '))

    # acrescentar informacao a uma lista pra cada pessoa
    # criar lista nova pra essa pessoa
    pessoa = [nome, peso]
    # append o nome e peso na lista pra essa pessoa
    print('essa pessoa {}'.format(pessoa))

    # adicionar pessoa no pepolino
    pepolino.append(pessoa)
    print('pepolino mlk {}'.format(pepolino))

    # pra continuar acrescentando pessoas e nomes na lista
    continuar = input('quer continuar s/n? ')
    # se não, sai do laço
    if continuar == 'n':
        break
    # se quer continuar, continuar o laço pra pegar dados pra mais uma pessoa

# analisar a lista pepolino pra ver quantas pessoa inscritas
# ver a quantidade das pessoas no pepolino
print('tem {} pessoas'.format(len(pepolino)))

# analisar a lista pepolino pra ver mais leves e mais pesadas