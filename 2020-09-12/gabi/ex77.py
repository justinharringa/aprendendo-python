print('app das vogais')
palavras = (
'feliz', 'triste', 'avocada', 'bff', 'roblox', 'tik tok', 'python', 'caneta', 'musica', 'love', 'harry potter')
for c in palavras:
    print(f'-na palavra {c} nos temos:')
    for letra in c:
        if letra in 'aeiou':
            # print(f' na palavra {c} nos temos {letra}')
            print(letra, end='')
    print()
