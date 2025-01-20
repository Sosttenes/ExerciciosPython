from time import sleep
from math import factorial
num = int(input('Digite um número para'
                'calcular seu fatorial: '))
fat = factorial(num)
cont = num
print('Calculando {}! = '.format(num), end='')
sleep(2)
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont = cont - 1
sleep(2)
print('{}'.format(fat))
