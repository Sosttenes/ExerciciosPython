import colorama
aluno = dict()
aluno["Nome"] = str(input("Nome do aluno: ")).capitalize().strip()
aluno['Média'] = float(input(f"A média de {aluno['Nome']} foi de: "))
aluno["Situação"] = " "
if aluno['Média'] >= 7:
    aluno["Situação"] = (colorama.Fore.GREEN + "Aprovado")
elif 5 <= aluno["Média"] < 7:
    aluno["Situação"] = (colorama.Fore.YELLOW + "Recuperação")
else:
    aluno["Situação"] = (colorama.Fore.RED + "Reprovado")
for k, v in aluno.items():
    print(f'{k}: {v}')