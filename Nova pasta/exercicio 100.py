from random import randint
lista = []


def sorteia(lista):
    print('sorteando valores da lista:')
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print(lista)


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'soma dos valores pares  são: {soma}')


sorteia(lista)
somaPar(lista)