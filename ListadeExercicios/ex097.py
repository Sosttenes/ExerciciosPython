def ajuda(com):
    help(com)


comando = ''
while True:
    comando = str(input('Função ou Biblioteca > ')).strip()
    if comando.title() == 'Fim':
        break
    else:
        ajuda(comando)
