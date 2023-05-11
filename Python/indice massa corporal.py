peso = float(input('Qual é os eu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura **2)
print('0 IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('PARABENS, voce está abaixo  do peso normal')
elif 18.5 <=imc < 25:
    print('PARABENS, voce esta na faixa de peso normal ')
elif 25 <= imc <30:
    print('voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE')
elif imc >= 40:
    print('Voce esta em OBESIDADE MORBIDA . cuidado')