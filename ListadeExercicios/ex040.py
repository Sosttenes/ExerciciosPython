from random import randint
import time

itens = ('pedra', 'papel', 'tesoura')
com = randint(0, 2)
print('''Suas opções são:
0 - PEDRA
1 - PAPEL
2 - TESOURA''')
jog = int(input('O que você escolhe?'))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO')
time.sleep(0.5)
print('Eu escolho {}'.format(itens[com]))
print('Você escolhe {}'.format(itens[jog]))
if com == 0 and jog == 1:
    print('Você ganhou')
elif com == 0 and jog == 2:
    print('Eu ganhei')
elif com == jog:
    print('Empate')
elif com == 1 and jog == 0:
    print('Eu ganhei')
elif com == 1 and jog == 2:
    print('Você ganhou')
elif com == 2 and jog == 0:
    print('Você ganhou')
elif com == 2 and jog == 1:
    print('Eu ganhei')
