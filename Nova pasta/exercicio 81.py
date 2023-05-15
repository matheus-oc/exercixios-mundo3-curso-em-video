lista = []
numeros = 0
while True:
    n = int(input('digite um valor: '))
    r = str(input('quer continuar?S/N ')).upper()
    lista.append(n)
    if r == 'N':
        break
    numeros += 1
if 5 not in lista:
    print(' o numero 5 não esta na lista.')
else:
    print('o numero 5 esta na lista')
lista.sort(reverse=True)
print(lista)
print(f'foram digitados {numeros} numeros')
