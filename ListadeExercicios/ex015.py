import math
print('Cossenos, senos e tangentes')
ang = float(input('Digite o ângulo que deseja: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Ângulo: {}\n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}'.format(ang, sin, cos, tan))
