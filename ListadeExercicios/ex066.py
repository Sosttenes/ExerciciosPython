print('=' * 25)
print('{:^25}'.format('Bank ES'))
print('=' * 25)
value = int(input('What amount do you want to withdraw? U$'))
total = value
bigced = 50
counter = 0
while True:
    if total >= bigced:
        total -= bigced
        counter += 1
    else:
        if counter > 0:
            print(f'Total of {counter} bill of U${bigced}')
        if bigced == 50:
            bigced = 20
        elif bigced == 20:
            bigced = 10
        elif bigced == 10:
            bigced = 1
        counter = 0
        if total == 0:
            break
