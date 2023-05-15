def leiaint(msg):
    try:
        n = int(input('digite um numero inteiro: '))
    except:
        print('esse valor não é inteiro digite outro valor!!')

    else:
        print('muito bem')
    return msg


def leiafloat(msg):
    try:
        n2 = float(input('digite um numero racional: '))
    except:
        print('valor invalido digite um valor iracional!! ')
    return msg


print(leiafloat('fim do programa'))
print(leiaint('fim do programa'))
