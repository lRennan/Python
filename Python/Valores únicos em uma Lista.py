numero = list()
while True:
    n = int(input('Digite um valor:  '))
    if n not in numero:
        numero.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!  nao vou adicionar...')
    r=str(input('Quer continuar? [S/N] '))
    if r in 'Nn' :
        break
print('-=' *30 )
numero.sort()
print(f'voce digitou os valores {numero}')