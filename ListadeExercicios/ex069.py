from random import randint
# Isso me sorteara 4 números
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# Apresentação dos números sorteados.
print('Os números sorteados são: ', end='')
for n in numeros:
    print(n, end=' ')
# Utilização da função max e min.
print(f'\nO maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')
