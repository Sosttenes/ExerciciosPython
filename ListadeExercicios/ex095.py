def leiaInt(txt):
    n = input(txt)
    if n.isnumeric():
        return int(n)
    else:
        print(f'\033[0;31mErro! {n} não é um número.\033[m')
        while True:
            n = str(input('Digite novamente: ')).strip()
            if n.isnumeric():
                return int(n)
            else:
                print(f'\033[0;31mErro! {n} não é um número.\033[m')


# Programa principal
n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')
