pt = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
termo = pt
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += rz
    cont += 1
    if cont == 11:
        print('FIM!')
