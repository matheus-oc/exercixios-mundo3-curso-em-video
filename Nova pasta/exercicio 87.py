matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('digite um numero: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
    print()
print(f'A soma dos valores pares é {par}')
for l in range(0, 3):
    coluna += matriz[l][2]
print(f'A soma da terceira coluna é {coluna}')
for c in range(0, 3):
    if c ==0:
        mai = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'o maior valor da segunda linha é {maior}')