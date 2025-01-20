from random import randint
import time
v = 0
while True:
    print('Vamos jogar par ou ímpar')
    com = randint(0, 20)
    value = int(input('Digite um valor: '))
    total = com+value
    ip = ' '
    while ip not in 'IPÌÍ':
        ip = str(input('Par ou ímpar?')).strip().upper()[0]
        time.sleep(1)
        print(f'Você jogou {value} e o computador {com}. O total foi de {total}')
        time.sleep(2)
    if ip == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Eu ganhei!')
            break
    elif ip in 'ÍIÌ':
        if total % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            print('Eu ganhei!')
            break
    print('Vamos jogar novamente...')
time.sleep(2)
print(f'GAMEOVER, você venceu {v} vezes.')