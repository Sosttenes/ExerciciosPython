wmu = man= ola = 0
while True:
    print('CADASTRE UMA PESSOA')
    age = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: '))[0].upper().strip()
    if age >= 18:
        ola +=1
    if sexo in 'M':
        man += 1
    if age < 20:
        if sexo in 'F':
            wmu +=1
    con = ' '
    while con not in 'SN':
        con = str(input('Quer continuar? '))[0].upper().strip()
    if con == 'N':
        break
print(f'Total de Pessoas com mais de 18 anos: {ola}\n'
      f'Ao todo temos {man} homens cadastrados\n'
      f'E temos {wmu} Mulheres com menos de 20 anos')
