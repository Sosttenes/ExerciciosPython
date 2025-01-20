# introdução de valores
n1 = float(input('DIGITE UM NÚMERO:'))
n2 = float(input('DIGITE OUTRO VALOR:'))
# condicionais
if n1 > n2:
    print('{} é o maior número'.format(n1))
elif n1 == n2:
    print('{} e {} são iguais'.format(n1, n2))
else:
    print('{} é o maior número'.format(n2))
