'''
Faça um programa que recebendo um valor inteiro,
informe se o número é positivo, negativo ou neutro.
'''

print('\t ---- A dança dos numeros ----')
x = int(input('Informe um numero para brincar:'))
if x < 0:

        print('é um numero negativo ')
elif x == 0:

        print('E um numero neutro')
elif x > 0:

        print('E um numero positivo')



'''
Crie um algoritmo que receba um número, 
conte o número total de dígitos e mostre o resultado.
Por exemplo, se o número é 2021 , então a saída deve ser 4'''

print('\t ---- Contagem dos Digitos ----')
digitos = int(input("Diggite um numero para contar seus digitos : "))
contador = 0
while digitos != 0:
    digitos //= 10
    contador += 1
print("Total de digitos = ", contador)