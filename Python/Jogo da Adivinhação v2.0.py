from random import randint
computador  = randint(0,10)
print('Sou seu computador...acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador :
            print('MAIS...')
        elif jogador > computador:
            print('MENOS...')
print('Acertou com {} tentavtivas '.format(palpites))