def fatorial(numero, show=False):
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(int(input('digite um numero: ')), show=True))
