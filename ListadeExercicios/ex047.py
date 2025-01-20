# entrada de dados
num = int(input('Digite um número: '))
# contador
cont = 0
# estruturas de repetição
for n in range(1, num+1):
    if num % n == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(n), end=' ')
# estruturas de controle
if cont > 2:
    print('\033[m\n'
          'O número {} não é primo\n'
          'Foi divídido {} vezes'
          ''.format(num, cont))
else:
    print('\033[m\n'
          'O número {} é primo\n'
          'Foi divídido {} vezes'
          ''.format(num, cont))
