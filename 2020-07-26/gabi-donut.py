print('BEM VINDO A LOJA DE DUNOTS DA GABY')
print('cardapio: donot de morango, chocolate e baunilha; bebidas: cafe, cha, chocolate quente preços: dunot: R$ 5 cafe: R$ 2 cha: R$ 2 chocolate quente: R$ 2')
soma = 0
mais_coisa = "sim"
while mais_coisa == "sim":
  pedido_donut  = int(input('quantos donuts voce vai querer'))
  preço_donut = 5
  preço_total = pedido_donut * preço_donut
  preço_total_cafe = 0
  cafe = input('voce vai querer cafe ou cha ou chocolate quente?: ')
  if cafe == 'sim':
    pedido_cafe = int(input('quantos?: '))
    preço_cafe = 2
    preço_total_cafe = pedido_cafe * preço_cafe
  soma += preço_total + preço_total_cafe
  mais_coisa = input('voce quer mais coisas: ')
  print('voce vai paga R$ {}'.format(soma))