fra = str(input('Digite uma frase: ')).strip().upper()
pal = fra.split()
tju = ''.join(pal)
inv = ''
for letra in range(len(tju) -1, -1, -1):
    inv += tju[letra]
if inv == tju:
    print(' É palíndromo')
else:
    print(' Não é palíndromo')
