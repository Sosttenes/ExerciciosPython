from math import fsum
matriz = [[], [], []]
pares = []
somacoluna = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].append(valor)
        if valor % 2 == 0:
            pares.append(valor)
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('A soma dos valores pares é: ', fsum(pares))
# print(f'A soma dos elementos da 3° coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
for l in range(0, 3):
    somacoluna += matriz[l][2]
print(f'A soma dos elementos da 3° coluna é {somacoluna}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior elemento da 2° coluna é {mai}')