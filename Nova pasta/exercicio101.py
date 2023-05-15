from datetime import date


def voto(nasc):
    atual = date.today().year
    idade = atual - nasc
    if idade >= 18:
        print(f'sua idade é de {idade} portanto o seu voto é obrigatorio')
    elif 18 > idade >= 16:
        if idade > 65:
            print('seu voto é opicional')
    else:
        return print(f'você ainda nao pode votar')


# programa principal
voto(int(input('digite o ano em que nasceu: ')))
