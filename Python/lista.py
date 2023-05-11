'''num = [2, 5, 9, 11]
num [2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Nao achei o numero 5')
print(num)
print(f'fessa lista tem {len(num)} elementos')
'''

valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor:')))

#valores.append(5)
#valores.append(9)
#valores.append(4)

for c, v in  enumerate(valores):
    '''print(f'{v}...', end='')'''
    print(f'na posiçao {c} encontrei o valor {v}!')
print('cheguei ao final da lista')

# b = a[:]  '''copia '''
