pares = []
impares = []
todos = []
while True:
    n = int(input('Digite um valor: '))
    todos.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar? ')).strip().upper()[0]
    if r in 'SN':
        if 'N' in r:
            break
    if r not in 'NS':
        print('Não entendi, tente outra vez.')
        r = str(input('Quer continuar? ')).strip().upper()[0]
        if 'N' in r:
            break
print(f'A lista completa é {todos}')
print(f'Os impares são: {impares}')
print(f'Os pares são {pares}')
