import random
print('Sorteio de ordem')
a1 = str(input('Seu nome: '))
a2 = str(input('Seu nome: '))
a3 = str(input('Seu nome: '))
lista = [a1, a2, a3]
random.shuffle(lista)
print('A ordem é {}'.format(lista))
