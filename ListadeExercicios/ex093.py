# Cálculo de fatorial
def fatorial(num, show=False):
    """
    --> Calcula o valor fatorial de um número
    :param num: Número que deseja realizar a operação de fatorial
    :param show: (Opcional) Caso queira ver a conta pra chegar em tal valor
    :return: Retorna o valor do fatorial de um número n
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f


n = int(input('Número!: '))
print(fatorial(n, show=True))
help(fatorial)
