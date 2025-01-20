from math import hypot
print('Triângulos Retângulos')
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjascente? '))
'''ig = pow(co, 2)+pow(ca, 2)
h = math.sqrt(ig)
print('A hipotenusa vai medir {:.2f}'.format(h))'''
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
