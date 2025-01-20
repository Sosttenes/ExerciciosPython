matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l].append(valor)
print('=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()