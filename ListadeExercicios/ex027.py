from colorama import Fore
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('Este número é:', Fore.BLUE + 'PAR')
else:
    print('Este número é:', Fore.MAGENTA + 'ÍMPAR')
