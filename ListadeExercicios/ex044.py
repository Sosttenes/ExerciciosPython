# tabuada v2.0
n = int(input('Digite um número para ver sua tabuada: '))
tab = 0
for m in range(1, 11):
    tab = n * m
    print('{} x {:>2} = {:>2}'.format(n, m, tab))
