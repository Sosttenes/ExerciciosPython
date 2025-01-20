# Criação das listas
dados = []
bancodeDados = []
# Analise
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(float(input('Peso: ')))
    if len(bancodeDados) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    bancodeDados.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar? ')).strip().upper()[0]
    if r not in 'SN':
        r = str(input('Não entendi, responda outra vez,'
                      ' quer continuar? ')).strip().upper()[0]
        if r in 'S' or 'N':
            if r in 'N':
                break
    else:
        if r in 'N':
            break
print(f'Você cadastrou {len(bancodeDados)} pessoas, ', end='')
print(f'o maior peso foi de {maior}kg', end=' ')
for p in bancodeDados:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'e o menor peso foi de {menor}kg', end=' ')
for p in bancodeDados:
    if p[1] == menor:
        print(f'{p[0]}')
