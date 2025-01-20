# importações
from datetime import date
# Entradas dos dados
data = date.today().year
ano = int(input('Qual seu ano de Nascimento? '))
idade = data-ano
if idade > 18:
    alis = ano + 18
    prazo = idade-18
    print('Você se alistou há {} anos'.format(prazo))
    print('Seu alistamento foi em {}'.format(alis))
elif idade < 18:
    alis = ano + 18
    prazo = 18-idade
    print('Seu alistamento será em {}'.format(alis))
    print('Você deverá se alistar em {} anos'.format(prazo))
elif idade == 18:
    print('Você devera se alistar este ano')
