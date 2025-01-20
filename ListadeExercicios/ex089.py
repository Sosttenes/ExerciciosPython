from time import sleep


def contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(3)
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
            sleep(0.3)
    if i > f:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
            sleep(0.3)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input("Inicio:   "))
fim = int(input("Fim:      "))
pas = abs(int(input("Passo:    ")))
contador(ini, fim, pas)
