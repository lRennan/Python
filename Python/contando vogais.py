palavras  = ('aprender', 'programar', 'linguagem', 'python'
            'curso', 'gratis','estudar','praticar','trabalhar',
             'mercado','programador','futuro')
for p in palavras:
    print(f'\n na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'a e i o u':
            print(letra, end=' ')
