from datetime import date
data = date.today().year
print(data)
cont = 0
velho = 0
novo = 0
for c in range(0, 3):
    cont += 1
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(cont)))
    old = data - ano
    if old >= 18:
        velho += 1
    else:
        novo += 1
print('Ao todo temos {} pessoas maiores de idade\nE também {} pessoas menores de idade'.format(velho, novo))
