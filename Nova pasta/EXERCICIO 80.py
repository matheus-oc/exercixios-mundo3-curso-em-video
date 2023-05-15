lista = []
maior = 0
menor = 0

for c in range(0, 5):
    numero = (int(input('digite um valor: ')))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, numero)
                break
            pos += 1
print(f'os valores digitados são: {lista}')