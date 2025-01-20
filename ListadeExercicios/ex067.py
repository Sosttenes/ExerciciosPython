num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco\n'
, 'Seis', 'Sete', 'Oito', 'Nove', 'Dez\n'
, 'Onze', 'Doze', 'Treze', 'Quatorse', 'Quinze\n'
, 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
cont = ' '
while True:
    escolha = int(input('Digite um número de 0 a 20:'))
    if 0 <= escolha <= 20:
        print(f'Você digitou o número: {num[escolha]}')
        cont = str(input('Você quer continuar? ')).strip().upper()[0]
        if cont == 'N':
            break
    print('Por favor, tente novamente.', end=' ')
print('Obrigado!!')
