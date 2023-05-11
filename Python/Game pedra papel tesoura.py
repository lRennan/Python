from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print(''' Suas opçoes:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('computador jogou  {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador VENCEU')
    elif jogador == 2:
        print('computador VENCEU')
    else:
        print('jogada invalida')

elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogada invalida')

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('jogada invalida')