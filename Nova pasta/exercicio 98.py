def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')

    print('-' * 25)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print('fim')
        print('-' * 25)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
        print('fim')
        print('-' * 25)


# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('digite o começo: '))
fim = int(input('digite o fim: '))
passo = int(input('digite de quanto em quando é para contar: '))
contador(inicio, fim, passo)
