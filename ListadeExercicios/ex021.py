city = str(input('Em que cidade você nasceu? ')).lower().strip()
pri = city[:6]
pn = pri in 'santo '
print(pn)
