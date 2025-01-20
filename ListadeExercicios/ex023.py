fr = str(input('Digite uma frase:')).upper().strip()
num = fr.count('A')
posa = fr.find('A')+1
posb = fr.rfind('A')+1
print('A letra A aparece {}\n'
      'A primeira letra A apareceu na posição {}\n'
      'a última letra A aparece na posição {}'.format(num, posa, posb))
