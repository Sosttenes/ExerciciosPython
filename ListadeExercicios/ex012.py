print('Aluguel de carros')
km = float(input('Quantos Kms você percorreu? '))
dias = float(input('Quantos dias você utilizou? '))
print('O seu aluguel custou: {:.2f}'.format(dias*60+km*0.15))
