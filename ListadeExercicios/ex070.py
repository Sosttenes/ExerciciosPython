num = (int(input("Digite um valor: ")),
       int(input("Digite um valor: ")),
       int(input("Digite um valor: ")),
       int(input("Digite um valor: ")))
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está na {num.index(3)+1}° posição')
else:
    print('Não há número 3.')
print('Os valores pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
