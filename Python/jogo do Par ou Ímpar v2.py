from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor? '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {computador}. Total e {total}', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce VENCEU!')
            v += 1
        else:
            print('voce PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce  VENCEU!')
            v += 1
        else:
            print('Voce PERDDEU!')
            break
    print('Vamos jogar novamente... ')
print(f'GAMER OVEER ! Voce venceu {v} vezes')