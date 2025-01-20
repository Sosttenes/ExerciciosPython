# importações
from colorama import Style, Fore
# introdução dos valores
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
# cálculo da média
med = (n1+n2+n3)/3
# condicionais
if med >= 7.0:
    print(Fore.GREEN + 'Parabéns, sua média foi {:.1f} e você foi \n'
          'APROVADO'.format(med) + Style.RESET_ALL)
elif 5.0 <= med <= 6.9:
    print(Fore.YELLOW + 'Sua média foi de {:.1f} e você está de\n'
          'RECUPERAÇÃO'.format(med) + Style.RESET_ALL)
elif med <= 4.9:
    print(Fore.RED + 'Sua média foi de {:.1f} e você está \n'
          'REPROVADO'.format(med) + Style.RESET_ALL)
print('Fim')
