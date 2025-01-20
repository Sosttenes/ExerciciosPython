# importações
from colorama import Fore, Style
# introdução dos valores
casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
anos = int(input('Quantos anos de financiamento? '))
# cálculo dos valores
parcela = casa/anos/12
porcentagem = 30/100*salario
# Condicionais
if parcela >= porcentagem:
    print(Fore.RED + 'Seu empréstimo foi negado pois a parcela\n'
          'R${:.2f} é mais alta que seu perncentual salárial.'.format(parcela) + Style.RESET_ALL)
else:
    print(Fore.GREEN + 'Seu empréstimo foi aprovado, sua parcela será de R${:.2f}'.format(parcela) + Style.RESET_ALL)
