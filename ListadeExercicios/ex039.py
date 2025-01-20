# Apresentação da loja
print('{:=^40}'.format('LOJAS DO ENOS'))
# Entrada de dados
pn = float(input('Preço das compras: R$'))
# Formas de pagamento
print('1 - Avista')
print('2 - Cartão avista')
print('3 - Cartão 2x')
print('4 - Cartão 3x ou mais')
# Forma de pagamento
fp = str(input('Forma de pagamento:')).strip()
# cálculos
avista = pn - (pn*10/100)
cartao = pn - (pn*5/100)
cartao3x = (pn*20/100)
# condicionais
if '1' in fp:
    print('com 10% de desconto sua compra ficou por {}'.format(avista))
elif '2' in fp:
    print('Com 5% de desconto sua compra ficou por {}'.format(cartao))
elif '3' in fp:
    print('S ua compra ficou por {:.2f}'.format(pn))
elif '4' in fp:
    # Parcelamento
    par = int(input('Em quantas vezes? '))
    # Cálculos
    juros = pn + cartao3x
    parcela = juros/par
    print('adicionado 20% de juros sua compra ficou por R${:.2f}\n'
          'dividido em {}x de R${:.2f}'.format(juros, par, parcela))
print('OBRIGADO PELA COMPRA')
