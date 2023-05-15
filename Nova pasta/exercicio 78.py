listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'o menor valor que voçê digitou foi {menor} nas posiçoes ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'o maior valor que você digitou foi {maior} nas posiçoes ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()
# REVISAR!!