from time import sleep
ado = menor = maior = num = int(input('digite um número: '))
cond = str(input('Quer continuar? ')).upper().strip()
div = 1
med = 0
if 'S' in cond:
    while 'S' in cond:
        num = int(input('digite um número: '))
        div += 1
        ado += num
        cond = str(input('Quer continuar? ')).upper().strip()
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        if 'N' in cond:
            print('Encerrando e calculando...')
            sleep(1)
elif 'N' in cond:
    print('Encerrando e calculando...')
    sleep(1)
med = ado/div
print('Você digitou {} números e a média foi de {}'
      '\nO maior valor foi de {} e o menor foi de {}'
      ''.format(div, med, maior, menor))
