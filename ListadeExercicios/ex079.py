from random import randint
from time import sleep
lista = list()
jogos = []
print(f'JOGUE NA MEGA SENA')
qtdjogos = int(input('Quantos jogos você quer? '))
for c in range(0, qtdjogos):
    cont = 0
    while True:
        num = randint(1, 61)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('='*6, f'Sorteando {qtdjogos} jogos', '='*7)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.9)
print('='*10, f'Boa Sorte!', '='*10)
