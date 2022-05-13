sexo = input('me diga seu sexo: [M/F]')
print('typo {}'.format(type(sexo)))
while sexo not in 'MmFf':
  sexo = input('dados errados. fale o certo por favor:')
print('dados certos')
