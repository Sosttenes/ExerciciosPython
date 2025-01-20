from time import sleep
maior = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('1 - Somar\n'
          '2 - Multiplicar\n'
          '3 - Maior\n'
          '4 - Novos números\n'
          '5 - Sair do programa')
    opcao = int(input('Qual opção? '))
    if opcao == 1:
        print('Calculando...')
        sleep(2)
        print('A soma é {}'.format(n1 + n2))
    elif opcao == 2:
        print('Calculando...')
        sleep(2)
        print('A multiplicação é'
              ' {}'.format(n1 * n2))
    elif opcao == 3:
        print('Calculando...')
        sleep(2)
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor é {}'.format(maior))
    elif opcao == 4:
        print('Digite novos valores...')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        sleep(2)
        print('Opção inválida. Tente novamente')
print('FIM!!')