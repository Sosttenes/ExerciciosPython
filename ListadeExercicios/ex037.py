# possibilidade de um triângulo
# Importações
from colorama import Fore, Style, init
import time
init()
# Resposta do usurious
print(Fore.BLUE + 'Analisador de triângulos' + Style.RESET_ALL)
r1 = float(input('tamanho da primeira reta: '))
r2 = float(input('tamanho da segunda reta: '))
r3 = float(input('tamanho da terceira reta: '))
print('Analisando...')
# Analise
time.sleep(2)
# Resposta do computador
if r1+r2 > r3 and r3+r2 > r1 and r1+r3 > r2:
    print('-=-'*20)
    print(Fore.GREEN + 'Estes segmentos de reta podem formar um triângulo' + Style.RESET_ALL)
    print('-=-' * 20)
    if r2 == r3 == r1:
        print(Fore.CYAN + 'É possível formar um triângulo equilátero' + Style.RESET_ALL)
        print('-=-' * 20)
    elif r2 == r3 or r3 == r1 or r2 == r1:
        print(Fore.MAGENTA + 'É possível formar um triângulo isóceles' + Style.RESET_ALL)
        print('-=-' * 20)
    elif r1 != r2 or r2 != r3 or r3 != r1:
        print(Fore.YELLOW + 'É possível formar um triângulo escaleno' + Style.RESET_ALL)
        print('-=-' * 20)
else:
    print('-=-' * 20)
    print(Fore.RED + 'Estes segmentos não podem formar um triângulo' + Style.RESET_ALL)
    print('-=-' * 20)
