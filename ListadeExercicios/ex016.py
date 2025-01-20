import random
print('Sorteio')
a1 = str(input('Nome: '))
a2 = str(input('Nome: '))
a3 = str(input('Nome: '))
a4 = str(input('Nome: '))
lista = [a4, a3, a2, a1]
sor = random.choice(lista)
print('O resultado é: {}'.format(sor))
