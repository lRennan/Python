'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione
com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
'''
time = list()
jogador = dict()
partidas = list()


while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        print('erro! responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('code ', end='')
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
print()
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}! ')
    else:
        print(f' ------- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'      no jogo {i+1} fez {g} gols')
    print('-=' * 30)
print('<<<<<< VOLTE SEMPRE >>>>>>>')


