'''Exercício Python 082: Crie um programa que vai ler vários
números e colocar em uma lista. Depois disso,
crie duas listas extras que vão conter apenas os valores
pares e os valores  ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar [s/n] '))
    if resp in 'nN':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f' a lista completa é {num}')
print(f' a lista de pares é {pares}')
print(f' a lista de impares é {impares}')