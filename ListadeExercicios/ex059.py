soma = con = num = 0
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
    con += 1
print('Você digitou {} números e a soma entre eles é {}'.format((con - 1), (soma - 999)))
