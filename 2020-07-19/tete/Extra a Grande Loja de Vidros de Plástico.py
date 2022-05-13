print('Bem Vindo a Plastic Glass a melhor loja de vidro feito 100% de plástico da região')
custo = 0
opção = 0
escolha = 0
Temperados = 0
Molhados = 0
Bluetooths = 0
Especiais = 0
while escolha != 5:
    print('''    (1) Temperados
    (2) Molhados
    (3) Bluetooths
    (4) Especiais
    (5) Sair''')
    escolha = int(input('Qual será sua escolha hoje? '))
    if escolha == 1:
        print('''    (1) "Wulsfwert", vidro utilizado por Napoleão IIV para lavar a ferida de sua amada após a sangrenta batalha de Lutterswald.
        O custo dele é avaliado em 320 R$ 
        (2) Vidros Hungaros, ressistentes e reconhecidos por todo mundo por sua coloração avermelhada. O custo dele é avaliado em 200 R$
        (3) "Vidreiro", uma obra de arte feita pelo grande artista Tio Lu em viagem ao Japão. O custo dele é avaliado em 20 R$''')
        opção = int(input('Qual vc quer? '))
        if opção == 1:
            Temperados = "Wulsfwert"
            custo += 320
        if opção == 2:
            Temperados = "Vidros Hungaros"
            custo += 200
        if opção == 3:
            Temperados = "Vidreiro"
            custo += 20
    if escolha == 2:
        print('''    (1) "Ducha-Forte", essa obra de arte em forma de vidro de plástico foi molhada pelo surfista Tio Justin em seu "Back Flip Invertido ao contrário duplo"
        e as palavras ditas pelo surfista sobre essa obra foi agora o nome que lhe é dado "Ducha-Forte". O custo dessa obra é avaliado em 30000000 R$
        (2) "Vishhh...", essas foram as palavras de Julinha a nova presidenta do Brasil após ver o presente que ela ganhou. O custo dessa obra é avaliado em 120000 R$
        (3) "O maoir e explendido vidro que nós achamos no esgoto.... :)", bem o nome já mostra que é especial e com a super promoção que estamos tendo
        fez com que o custo dele se tornasse apenas 2 R$''')
        opção = int(input('Qual vc quer? '))
        if opção == 1:
            Molhados = "Ducha-Forte"
            custo += 30000000
        if opção == 2:
            Molhados = "Vishhh..."
            custo += 12000
        if opção == 3:
            Molhados = "O maoir e explendido vidro que nós achamos no esgoto.... :)"
            custo += 2
    if escolha == 3:
        print('''    (1) "Ividro 10", novo lançamento da Apple!! um marco para a historia dos vidros de plástico. O custo tá avaliado em 3000 R$
        (2) "MotoV 17", se nós temos o lançamento da Apple nós também teriamos o da Motorola e agora coms eu Bluetooth funcionando a 40000 Km de distância
        . O custo é avaliado em cerca de 2500
        (3) "Nokia Indestrutível em Versão Vidro", bem o nome explica né?... basciamente é o único vidro inquebrável do mundo!!
        O custo dele é cerca de 100000000 R$''')
        opção = int(input('Qual vc quer? '))
        if opção == 1:
            Bluetooths = "Ividro 10"
            custo += 3000
        if opção == 2:
            Bluetooths = "MotoV 17"
            custo += 2500
        if opção == 3:
            Bluetooths = "Nokia Indestrutível em Versão Vidro"
            custo += 100000000
    if escolha == 4:
        print('''    (1) "Poka", essa obra foi achada após o cometa Harlley passar muito perto da Terra trazendo junto com ele uma mensagem do futuro de acordo com os cientistas
            O custo dessa obra espacial brilhante estranha é 10 R$
            (2) "Esfiha de Vidro Brilhante", um presente feito a Donald Trump após sua reeleição em 2088. O custo da obra equivale a 670 R$
            (3) "Vida", essa foi uma obra feita por Deus e por isso não dá para compralá por que ela já te foi dada :)''')
        opção = int(input('Qual vc quer? '))
        if opção == 1:
                Especiais = "Poka"
                custo += 10
        if opção == 2:
                Especiais = "Esfiha de Vidro Brilhante"
                custo += 670
        if opção == 3:
                Especiais = "Vida"
                custo += 0
        if escolha == 5:
            break
compra_final = Temperados, Molhados, Bluetooths, Especiais
print('até mais!!, esse é o valor da sua compra {} e esses foram os itens comprados {}, volte sempre :)'.format(custo, compra_final))
#tio eu só não consegui botar os itens que eles compraram o resto deu certo