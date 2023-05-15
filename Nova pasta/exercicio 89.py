ficha = []
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota 1'))
    nota2 = float(input('nota2 '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('quer continuar? ')).upper()
    if r == 'N':
        break
print(ficha)
