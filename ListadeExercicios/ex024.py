nome = str(input('Digite seu nome completo: ')).strip().title()
ana = nome.find(' ')
pn = nome[0:ana]
an = nome.rfind(' ')
un = nome[an:]
print('Olá, seja bem vindo {} \n'
      'Seu primeiro nome é: {}\n'
      'E seu último nome é:{}'.format(nome, pn, un))
