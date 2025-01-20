# entrada de dados
kg = float(input('Qual seu peso em Kg? '))
alt = float(input('Qual sua altura em M? '))
# Cálculo
imc = kg/(alt**2)
# condicionais
if imc<=16.9:
    print('seu IMC é {:.2f} você está muito abaixo do peso'.format(imc))
elif 17<=imc<=18.4:
    print('seu IMC é {:.2f} você está abaixo do peso'.format(imc))
elif 18.5<=imc<=24.9:
    print('seu IMC é {:.2f} você está no peso normal'.format(imc))
elif 25<=imc<=29.9:
    print('seu IMC é {:.2f} você está acima do peso'.format(imc))
elif 30<=imc<=34.9:
    print('seu IMC é {:.2f} você está obesidade grau I'.format(imc))
elif 35<=imc<=40:
    print('seu IMC é {:.2f} você está obesidade grau II'.format(imc))
else:
    print('seu IMC é {:.2f} você está obesidade mórbida'.format(imc))
