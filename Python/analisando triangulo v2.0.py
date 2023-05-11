r1 =  float(input('Primerio Segmento: '))
r2 =  float(input('Segundo Segmento:  '))
r3 =  float(input('Terceiro Segmento: '))
if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segemntos acima PODEM FORMAR um TRIANGULO!!',end='')
    if r1 == r2 == r3:
        print('EQUILATERO!!')
    elif r1 != r2 == r3:
        print('ESCALENO!')
    else:
        print('ISOCELES')
else:
    print('OS segmentos acima NAO PODEM FORMA tringulo')