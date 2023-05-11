'''
Exercício Python 098: Faça um programa que tenha uma função
chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
'''
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    sleep(0.5)
    print('-=' * 20)
    print(f'contagem de {i} ate {f} de {p} em {p} ')
    sleep(0.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!')
        print('-=' * 20)


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('Inicio:  '))
fim = int(input('Fim:     '))
passo = int(input('Passo: '))
contador(ini, fim, passo)

