# percentage salárial
sal = float(input('Qual seu salário? R$'))
if sal <= 1250:
    # cálculo salárial
    aum = sal*15/100+sal
else:
    aum = sal*10/100+sal
print('O seu salário de R${:.2f} agora será de: R${:.2f}'.format(sal, aum))
