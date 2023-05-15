lista = []
for c in range(0, 1):
    n = int(input('digite um numero: '))
    if n not in lista:
        lista.append(n)
        print('valor adiconado com suacesso!')
    else:
        print('valor duplicado, não foi adicionado')
    cond = str(input('deseja continuar?S/N ')).upper()
    while True:
        if cond == 'S':
            n = int(input('digite um numero: '))
            if n not in lista:
                lista.append(n)
                print('valor adicionado com sucesso!')
            else:
                print('valor duplicado, não foi adicionado')
            cond = str(input('deseja continuar?S/N ')).upper()
        elif cond == 'N':
            break
        else:
            print('opção invalida tente novamente ')
            cond = str(input('deseja continuar?S/N ')).upper()
lista.sort()
print(f'os vaores digitados foram {lista}')
# REFAZER