a = int(input('Primeiro valor: '))
b = int(input('Segundo valor:  '))
c = int(input('Teceiro Valor:  '))
# verificando quem é menor

menor = a
if b < a and b < c:
    menor = b
if c < a and  c < b:
    menor = c
# verificando quem é o maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {} \nO maior valor Digitado {}'.format(menor, maior))