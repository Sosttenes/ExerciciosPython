lista = [[], []]
for i in range(1, 9):
    valor = int(input(f'Digite o {i}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista.sort()
print(f'Os valores são {lista}')
lista[0].sort()
print(f'Os valores pares são {lista[0]}')
lista[1].sort()
print(f'Os números impares foram {lista[1]}')
