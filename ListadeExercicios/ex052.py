sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'M F':
    print('Dados inválidos.')
    sexo = str(input('Por favor, informe seu sexo: ')).strip().upper()
if sexo in 'F':
    print('Sexo FEMININO registrado')
else:
    print('Sexo MASCULINO registrado')
