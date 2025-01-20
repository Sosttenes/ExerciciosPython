from colorama import Fore, Back, Style, init
init()
print('Velocimetro')
vel = float(input(Fore.BLUE + 'Qual a velocidade do carro? '))
if vel<=80:
    print(Fore.GREEN + 'Parabéns, sem problemas por hoje!')
else:
    mul = (vel-80)*7.00
    print(Fore.RED + 'Sua multa é de: R${:.2f} por exceder o limite de 80 km/h'.format(mul))
print(Fore.YELLOW + 'Tenha um bom dia! Dirija com segurança!')
