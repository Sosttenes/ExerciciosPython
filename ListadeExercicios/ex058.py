seq = int(input('Qual o tamanho da sequência '))
t1 = 0
t2 = 1
cont = 3
print('{} -> '.format(t1), end='')
print('{} -> '.format(t2), end='')
while cont <= seq:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM!')
