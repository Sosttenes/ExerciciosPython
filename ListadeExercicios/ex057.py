import time
pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
cont = 1
termo = pt
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += rz
        cont += 1
        time.sleep(0.5)
    print('PAUSA')
    mais = int(input('Quantos termos a mais devo '
                     'mostrar?'))
print('Progressão finalizada com {} termos'.format(total))