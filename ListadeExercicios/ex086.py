jogadores = dict()
gols = list()
time = list()
while True:
    jogadores.clear()
    jogadores["Nome"] = str(input("Nome do jogador: ")).strip().capitalize()
    jogadores["Partidas"] = int(input(f"Quantas partidas {jogadores["Nome"]} jogou? "))
    for g in range(0, jogadores["Partidas"]):
        gols.append(int(input(f'Quantos gols {jogadores["Nome"]} fez na {g + 1}° partida ')))
    jogadores["Gols"] = gols[:]
    jogadores["Total"] = sum(gols)
    time.append(jogadores.copy())
    gols.clear()
    while True:
        cond = str(input("Quer continuar? ")).strip().upper()[0]
        if cond in 'SN':
            break
        print("ERRO! Digite apenas Sim ou Não")
    if cond == 'N':
        break
for k, v in enumerate(time):  # Está pegando as chaves e valores da lista time e enumerando
    print(f"{k:>3} ", end="")  # aqui ele imprime os índices das chaves
    for p in v.values():  # aqui ele nomeia como "p" a variável que vai abrigar os valores das chaves, fazendo isso pra
        # todos os itens da lista time de um por um.
        print(f"{str(p):<8}", end="")  # aqui ele imprime os valores de um por um, eu preciso transformar todos eles
        # em string pois alguns são int e dá conflito
    print()
while True:
    busca = int(input("Para encerrar digite -1\n"
                      "Qual jogador você quer ver estáticas: "))  # número do índice do jogador
    if busca == -1:  # condição de encerramento do programa (Gambiarra)
        break
    if busca >= len(time):
        print("ERRO! Não existe jogador com este código")
    else:
        print(f"Levantamento do jogador {time[busca]["Nome"]}")  # imprime o nome do jogador buscando na lista time pelo
        # índice que foi escolhido na variável "busca"
        for i, g in enumerate(time[busca]["Gols"]):  # Vai acessar a lista time e nela o dicionário que foi escolhido na
            # variável "busca" e vai iterar os valores de "gols" um por um colocando o índice
            print(f"Na partida {i + 1} fez {g} gols")  # imprimindo os valores da iteração um por vez
    print("-" * 40)
print("Volte Sempre!!")
