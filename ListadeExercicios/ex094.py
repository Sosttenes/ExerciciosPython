# Programa secundário
def ficha(nome='<desconhecido>', gols=''):
    print(f'O {nome} fez {gols} gol(s)')


# Programa principal
nome = str(input('Nome do jogador: ')).strip().title()
g = str(input(f'Quantos gols {nome} fez? '))
if g.isnumeric():
    gols = int(g)
else:
    gols = 0
if nome == '':
    ficha(gols=g)
else:
    ficha(nome, g)
