# importações
import time
from datetime import date
# Entrada de dados
atual = date.today().year
nasc = int(input('Qual ano você nasceu? '))
# cálculo
idade = atual-nasc
# verificação
print('ANALISANDO...')
time.sleep(2)
# condicionais
if idade <= 9:
    print('Sua idade é {}\n'
          'Atleta: Mirim'.format(idade))
elif 10<=idade<=14:
    print('Sua idade é {}\n'
          'Atelta: Infantil'.format(idade))
elif 15<=idade<=19:
    print('Sua idade é {}\n'
          'Atleta: Junior'.format(idade))
elif 20<=idade<=25:
    print('Sua idade é {}\n'
          'Atleta: Sênior'.format(idade))
else:
    print('Sua idade é {}\n'
          'Atleta: Master'.format(idade))
