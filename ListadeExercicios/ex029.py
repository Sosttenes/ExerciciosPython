print('VALORES')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
maior = n1
# verificando maior
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
menor = n1
# verificando o menor
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('Seu maior valor é: {}\n'
      'Seu menor valor é: {}'.format(maior,menor))