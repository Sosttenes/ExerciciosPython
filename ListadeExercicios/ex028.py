dis = float(input('Qual a distância da viagem? '))
if dis <= 200.00:
    print('O valor da sua viagem é de: R${:.2f}'.format(dis*0.50))
else:
    print("O valor de sua viagem é de: R${:.2f}".format(dis*0.45))
print('Para uma viagem de {}Km'.format(dis.__trunc__()))
