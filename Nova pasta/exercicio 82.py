num = []
par = []
impar = []
while True:
    n = int(input('digite um numero '))
    num.append(n)
    r = str(input('você que continuar? [S/N] ')).upper()
    if r == 'nN':
        break
print(num)
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é : {impar}')
