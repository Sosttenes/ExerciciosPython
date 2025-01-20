print('Conversor de temperaturas')
c = float(input('Informe a temperatura em C°:'))
f = c*9/5 + 32
k = c + 273
print(' A temperatura em K°{:.1f} e em F°{:.1f}'.format(k, f))
