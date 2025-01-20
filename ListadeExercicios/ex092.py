def votacao(numero):
    from datetime import datetime
    ano = datetime.today().year
    idade = ano - numero
    if idade < 16:
        return f'Com {idade} anos: Não vai votar!'
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: Voto facultativo!'
    if idade >= 18:
        return f'Com {idade} anos: Voto obrigatório!'


numero = int(input('Que ano você nasceu?'))
print(votacao(numero))
