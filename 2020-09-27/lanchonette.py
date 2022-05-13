# Cara 1:
# - arroz
# - milho
# - yakisoba
# Cara 2:
# - arroz
# - feijao
# - cuzcuz
# Cara 3:
# - coxinha
# - feijao
# - sorvete
# Voces vao comer: arroz, feijao
pedidos = []
vao_comer = []
for amigo in range(3):
    print('amigo {}: vai querer comer o que?'.format(amigo + 1))
    for numero in range(3):
        print('pedidos ate agora: {}'.format(pedidos))
        pedido = input('Pedido {}: '.format(numero + 1))
        if pedido in pedidos:
            vao_comer.append(pedido)
        else:
            pedidos.append(pedido)

print('vcs vao comer: {}'.format(vao_comer))

