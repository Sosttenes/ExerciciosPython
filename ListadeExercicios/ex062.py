cont = 1
while True:
    tab = int(input('Quer ver a tabuada de qual valor?'))
    if tab < 0:
        break
    for l in range (1, 11):
        print(f'{tab:<2} x {cont:2} = {tab*cont:2}')
        cont += 1
print('PROGRAMA ENCERRADO COM SUCESSO. Volte sempre!')
