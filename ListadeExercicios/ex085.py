cadastro = dict()
lista = list()
soma = media = 0
while True:
    cadastro.clear()
    cadastro["Nome"] = str(input("Nome: ")).strip().capitalize()
    while True:
        cadastro["Sexo"] = str(input("Sexo: ")).strip().upper()[0]
        if cadastro["Sexo"] in "MF":
            break
        print("ERRO! Digite apenas Masculino ou Feminino.")
    cadastro["Idade"] = int(input("Idade: "))
    soma += cadastro["Idade"]
    lista.append(cadastro.copy())
    while True:
        cond = str(input("Quer continuar? ")).upper().strip()[0]
        if cond in "SN":
            break
        print("ERRO! Digite apenas Sim ou Não")
    if cond == "N":
        break
print(f"Ao todo foram cadastradas {len(lista)} pessoas")
media = soma/len(lista)
print(f"A média das idades é {soma/len(lista):.2f} anos")
print("As mulheres cadastradas são ", end="")
for p in lista:
    if p["Sexo"] == "F":
        print(p["Nome"], end=" ")
        print()
print("Acima da média")
for d in lista:
    if d["Idade"] > media:
        for k, v in d.items():
            print(f"{k} = {v} ", end="")
        print()
print("<<<ENCERRADO>>>")
