listanum=[]
maior = 0
menor = 0
for c in range (0 , 5):
    listanum.append(int(input(f"digite um valor para posiçao {c}: ")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=' * 30)
print(f'voce digitou os valores {listanum}')
print(f'o maior valor digitado foi {maior} na posiçao ', end='')
for i ,v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'o menor valor digitado foi {menor} na posiçao ', end='')
for i , v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()
