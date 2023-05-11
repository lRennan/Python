num =  (int(input('Digite um numero ')),
        int(input('Digite outro numero ')),
        int(input('Digite mais um numero ')),
        int(input('Digite  0 ultimo numero ')))
print(f'vode digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes ')
if 3 in num:
        print(f'O valor 3 apareceu na {num.index(3)}ªposiçao ')
else:
        print("O valor 3 digitado  nao esta em nenhuma posiçao")
print("os valores pares digitados foram ", end='')
for n in num:
        if n % 2 == 0:
                print(n, end=' ')


