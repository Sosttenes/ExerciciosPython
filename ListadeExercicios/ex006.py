print('Conversor de moedas')
r = float(input('Valor em Real: R$'))
d = r/5
e = r/5.28
li = r/6.05
pa = r/0.014
print('Dollar: {:.2f}\n'
      'Euro: {:.2f}\n'
      'Libras Esterlinas: {:.2f}\n'
      'Pesos Argentinos: {:.2f}'.format(d, e, li, pa))
