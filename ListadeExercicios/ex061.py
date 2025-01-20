s = cont = 0
while True:
    num = int(input('digite um valor:'))
    if num == 999:
        break
    s += num
    cont += 1
print(f'A soma dos {cont} valores é {s}')
