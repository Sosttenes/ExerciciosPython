expr = input('Digite uma expressão: ')
pilha = []
for l in expr:
    if l == '(':
        pilha.append('(')
    elif l == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Válida')
else:
    print('Inválida')
