def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, dividir um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033Entrada de dados interrompida pelo usario\033[m')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: por favor, digite um numero real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\03331mUSUARIO preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n
n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor digitado foi {n1} e o real foi {n2}')
