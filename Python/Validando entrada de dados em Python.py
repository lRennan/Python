def leiaInt(mgs):
    ok = False
    valo = 0
    while True:
        n = str(input(mgs))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERROR! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor

# Programa Principal
n = leiaInt('Digite um numero: ')
print(f'voce acabou de diggitar o numero: {n}')
