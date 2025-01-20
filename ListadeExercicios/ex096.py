def notas(*n, sit=False):
    """
    Esta função calcula média de alunos com base em suas notas!
    :param n: dita o valor das notas
    :param sit: retorna a situação da média
    :return:
    """
    r = dict()
    r["Total"] = len(n)
    r["Maior"] = max(n)
    r["Menor"] = min(n)
    r["Média"] = sum(n)/len(n)
    if sit:
        if r["Média"] >= 7:
            print(f'Média {r["Média"]}: Situação boa!')
        elif r["Média"] >= 5:
            print(f'Média {r["Média"]}: Situação razoável!')
        else:
            print(f'Média {r["Média"]}: Situação ruim!')
    return r

# Programa principal
resp = notas(5.5, 2.5, 7.0, 9.5, sit=True)
print(resp)
