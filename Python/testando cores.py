'''None      0
bold      1 negrito
underline 4
negative  7  inverte

branco       30  Fundo 40
vermelho     31  fundo 41
verde        32  Fundo 42
amarelo      33  Fundo 43
azul         34  Fundo 44
roxo         35  Fundo 45
verde claro  36  Fundo 46
cinza        37  Fundo 47

print('\033[1;31;43mOla Mundo!')
print('\033[1;31;43mOla Mundo!\033[m')
'''

print('\033[7;30;46mSou Fodaaaaaaaaaa Mundo!\033[m')
print('\033[4;35;47mOla Mundo!\033[m')
nome = 'Guanabara'
print('Ola! Muito prazer em tew conhecer , {}{}{}!!!!'.format('\033[1;31m', nome, '\033[m'))
