nome = str(input('Quaal é o seu nome?' ))

if nome == 'Gustavo':
    print('Que nome bonito! ')
elif nome =='Pedro' or nome =='Maria' or nome =='Paulo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um otimo dia ,{}'.format(nome))
