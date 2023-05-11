from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('quem nasceu em {} tem {} ano(s) em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce precisa se ALISTAR IMEDIATAMENTE!!!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos pra o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} ano()'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))