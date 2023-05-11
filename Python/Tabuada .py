'''print('\t ----Tabuada----')
numero = int(input('Informe o numero para ver a tabuada: '))
print('\n Tabuada de ', numero, ':')

for i in range(1,11):
    print(numero, 'x', i, '=', (numero * i))
'''

num = int(input('Digite um numero para ver sua tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(num, c,num*c))