print('-='*13)
print('Analizador de Triangulos')
print('-='*13)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo  segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR tringulo!')
else:
    print('Os segmentos acima NAO PODEM FORMAR triângulo')