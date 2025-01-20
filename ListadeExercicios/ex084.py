jogador = dict()
gols = list()
jogador["nome"] = str(input('Nome do jogador? ')).strip().capitalize()
jogador["partidas"] = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for p in range(0, jogador["partidas"]):
    gols.append(int(input(f'Quantos gols na {p+1}° Partida ')))
jogador["gols"] = gols[:]
jogador["total"] = sum(gols)
print("-"*40)
print(jogador)
print("-"*40)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")
print("-"*40)
print(f"{jogador["nome"]} jogou {len(jogador["gols"])} partidas")
for i, v in enumerate(gols):
    print(f"    Na primeira {i+1}° partida, fez {v} gols.")
