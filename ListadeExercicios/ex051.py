# cadastro
med = 0
maior = 0
nomeve = ''
mulher = 0
for c in range(1, 5):
    print('----- {}° PESSOA -----'.format(c))
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    med += idade
    div = med/4
    if c == 1 and sexo == 'M':
        maior = idade
        nomeve = nome
    else:
        if maior < idade and sexo == 'M':
            maior = idade
            nomeve = nome
    if sexo == 'F' and idade < 20:
            mulher += 1
print('A média de idade do grupo é: {}'.format(div))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, nomeve))
print('Ao todo temos {} mulheres com menos de 20 anos'.format(mulher))
