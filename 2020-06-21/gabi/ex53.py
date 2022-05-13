# 53 - Crie um programa que leia uma frase qualquer e diga se ela é um
# palindromo, desconsiderando os espaços (não usam accentos de qq jeito... só vai complicar)
# https://youtu.be/cL4YDtFnCt4?t=1858
frase = str(input('digite uma frase: ')).strip().upper()
print("frase: {}".format(frase))
palavras = frase.split()
print("palavras: {}".format(palavras))
print("length (tamanho) -> len(palavras): {}".format(len(palavras)))
junto = ''.join(palavras)
print("junto: {}".format(junto))
inverso = ''
print("length (tamanho) -> len(junto): {}".format(len(junto)))
for letra in range(len(junto)-1, -1, -1):
  inverso += junto[letra]
print("inverso: {}".format(inverso))
if inverso == junto:
  print('tem palindromo')
else:
  print('nao tem palindromo ai')
