from time import sleep


def contador(i, f, p):
    print('OLA lita KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK SE PREPARA POIS SERA SEUS ULTIMOS MOMENTOS')
    sleep(2.0)
    print(f'contagem Regressiva de sua MORTEE {i} até 0', )

    sleep(1.0)

    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont}    ', end='')
            sleep(1.0)
            cont -= p
        print('0')
        sleep(0.2)

        print('FIM HAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!')
        sleep(0.5)
        print('BYE BYEEEE')
        sleep(0.5)
        print('TE VEJO NO INFERNO')


contador(10, 1, 1)
