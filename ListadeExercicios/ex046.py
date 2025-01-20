print('='*21)
print('PROGRESSÃO ARITMÉTICA')
print('='*21)
pt = int(input('PRIMEIRO TERMO: '))
rz = int(input('RAZÃO: '))
tm = pt + (10 - 1) * rz
for m in range(pt, tm + rz, rz):
    print(m, end=' -> ')
print('ACABOU')
