from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 100)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('pronto!')


def somarPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares de {lista}, temos {soma}')

numero = list()
sorteia(numero)
somarPar(numero)