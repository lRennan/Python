'''
Exercício Python 101: Crie um programa que tenha uma função chamada
voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com { idade } anos: NAO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com { idade } anos: VOTO OPCIONAL.'
    else:
        return f'com { idade } anos: VOTO OBRIGATORIO.'
nas = int(input( 'em que ano voce nasceu? '
                 ''))
print(voto(1990))
