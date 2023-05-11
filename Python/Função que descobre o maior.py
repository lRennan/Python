'''Exercício Python 099:Faça um programa que tenha uma função chamada
maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('analizando os valores passados....')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont} valores ao toda')
    print(f'o maior valor informado foi {maior}.')


maior(2, 9, 7, 0, 6, 3)
maior(4, 5, 677, 23, 2)
maior(2, 4, 5, 7, 85)
maior(2, 3, 45, 6, 7, 8)
maior(3, 4, 5, 2, 4)
maior(7, 8, 9)
