tot = totmil = cont = menor = 0
barato = ''
while True:
    name = str(input('Nome do produto: ')).capitalize().strip()
    price = int(input('Preço: R$'))
    cont += 1
    tot += price
    if price > 1000:
        totmil += 1
    if cont == 1:
        menor = price
        barato = name
    else:
        if price < menor:
            menor = price
            barato = name
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if cond in 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${tot:.2f}')
print(f'Temos {totmil} produtos acima de R$1000.00')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}')
