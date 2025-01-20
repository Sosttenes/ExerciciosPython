from random import randint
num = randint(0, 10)
cont = 0
print('Olá, sou seu computador e acabei de pensar em número'
      'entre 0 e 10.\n'
      'Será que você consegue advinhar?')
res = int(input('Qual seu palpite? '))
while res != num:
    if res < num:
        print('Tente outra vez, pensei em um número maior')
        res = int(input('Qual seu palpite? '))
    elif res > num:
        print('Tente outra vez, pensei em um número menor')
        res = int(input('Qual seu palpite? '))
    cont += 1
if num == res:
    print('Parabéns você acertou com {} tentativas.'.format(cont))
