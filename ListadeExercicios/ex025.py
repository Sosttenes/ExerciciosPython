from random import randint
from time import sleep
print('Vou pensar em número entre 0 e 5\n'
      'tente advinhar')
lisnum = randint(0, 5)  # resposta do computador
res = int(input('Em que número eu pensei? '))  # resposta do jogador
print('Processando...')
sleep(1)
if lisnum == res:
    print('Parabéns, eu pensei no número {} você me ganhou'.format(res))
else:
    print('GANHEI, eu pensei no número {} e não no {}'.format(lisnum, res))
