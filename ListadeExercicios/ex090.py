from time import sleep


def maior(* num):
    mav = cont = 0
    print('Analisando valores...', end=' ')
    sleep(0.5)
    if len(num) > 0:
        for v in num:
            print(f'({v})', end=' ')
            sleep(0.5)
            if cont == 0:
                mav = v
            else:
                if v > mav:
                    mav = v
            cont += 1
        print(f'\nO maior número foi {mav}')
        sleep(0.5)
        print(f'A quantidade de números informados foi {cont}')
        sleep(0.5)
    else:
        print('A quantidade de números informados foi 0')
        sleep(0.5)
        print('Não existe número maior')


maior(1, 4, 2)
maior(6)
maior()
