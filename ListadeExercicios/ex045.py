# repetição de inputs
soma = 0
con = 0
for m in range(0, 6):
    num = int(input('Digite o {}° número: \n'
                    ''.format(m+1)))
    if num % 2 == 0:
        con = con + 1
        soma = soma + num
print('A soma dos {} termos pares é ={}\n'
      ''.format(con, soma))
