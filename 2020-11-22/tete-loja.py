print('bem vindo a Jsurfing')
escolha = []
while True:
    opção = input("""aqui nos temos vários tipos de pranchas como:  
    1. Usadas
    2. Bravas
    3. Transparentes
    4. Relíquias 
    qual vc quer? """)
    # analisar a escolha
    if opção == 'Usadas':
        print(""" entre essa opção temos:
    1. Norkvalley: foi a prancha usada por Tio Justin para surfar no vilarejo de mesmo nome
    2. Avoa Passarin!!: foi a prancha que foi usada pelo melhor surfista do mundo quando ele caiu de uma onda de 30 metros""")
        escolha.append(input('qual a sua escolha? '))
        quer = input('quer continuar? ')
        if quer == 'não':
            break
    if opção == 'Bravas':
        print(""" entre essa opção temos:
    1. Tatooine: foi a prancha usada por Tio Justin quando ele ficou submerso por 10 minutos, onde disseram que ele foi pra Tatooine
    2. Everest: foi a prancha usada pelo maior surfista do mundo qunado ele pegou uma onda de 32.7 metros
    3. Samba: foi a prancha onde ele escorregou e acabou perdendo seu primeiro campeonato, era o começo da historia""")
        escolha.append(input('qual a sua escolha? '))
        quer = input('quer continuar? ')
        if quer == 'não':
            break
print(escolha)