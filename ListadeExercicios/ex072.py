lista = []
while True:
    n = lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? ')).strip().upper()[0]
    if r in 'SN':
        if 'N' in r:
            break
    if r not in 'NS':
        print('Não entendi, tente outra vez.')
        r = str(input('Quer continuar? ')).strip().upper()[0]
        if 'N' in r:
            break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
print('O valor 5 não foi encontrado!' if 5 not in lista else 'O valor 5 faz parte da lista!')
