lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Este número já está na lista')
    r = str(input('Quer continuar? ')).strip().upper()[0]
    if 'S' or 'N' in r:
        if 'N' in r:
            break
    if r not in 'SN':
        print('Não entendi, tente outra vez')
        r = str(input('Quer continuar? ')).strip().upper()[0]
        if 'N' in r:
            break
print(f'Os valores digitados foram: {lista}')
lista.sort()
print(f'Em ordem crescente são {lista}')
