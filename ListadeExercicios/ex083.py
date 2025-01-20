from datetime import datetime
date = dict()
date['nome'] = str(input("Qual seu nome? ")).capitalize().strip()
born = int(input("Em que ano você nasceu? "))
date['idade'] = datetime.now().year - born
date['número da carteira'] = int(input('Número da carteira/0 se não tiver: '))
if date['número da carteira'] != 0:
    date['Contratação'] = int(input("Ano de contratação: "))
    date['Salário'] = float(input('Salário: R$'))
    date['Aposentadoria'] = date['idade'] + (date['Contratação']+35) - datetime.now().year
for k, v in date.items():
    print(f'{k}: {v}')
    