temp = []
princ = []
maior = 0
menor = 0
while True:
    temp.append(str(input('digite seu nome: ')))
    temp.append(int(input('digite seu peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input(' deseja continuar? S/N')).upper()
    if r == 'N':
        break
print(f'você cadastrou {len(princ)}, pessoas')
print(f'a pessoa mais pesada tem {maior} kg')
print(f'o mais leve tem {menor}')