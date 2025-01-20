print('Medidor de parede')
lar = float(input('Qual a largura da sua parede? '))
alt = float(input('Qual a altura de sua parede? '))
dim = lar*alt
print('Sua parede tem dimensão de {}x{} e sua área é de {}m²'.format(lar, alt, lar*alt))
print('Para pintar ela precisamos de {:.2f}L de tinta'.format((lar*alt)/2))
