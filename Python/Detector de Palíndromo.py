frase = str(input('digite uma frase : ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
'''inverso = ''
for letra  in range (len(junto)-1, -1,-1):
    inverso += junto[letra]'''
print('o inverso de {} é {} '.format(junto, inverso))
if inverso == junto:
    print('temos um palíndromo! ')
else:
    print('A frase digitada nao é um palidromo!')