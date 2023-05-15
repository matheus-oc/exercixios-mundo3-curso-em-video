from time import sleep


def maior(*num):
    cont = maior = 0
    print('-' * 30)
    print('\nanalisando os valores passados')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram informados {cont} valares ao todo')
    print(f'o maior valor informado foi {maior}')


# programa principal:
maior(2, 9, 5, 7, 13)
maior(3, 4, 6, 7, 17)
maior(3, 5, 1)
