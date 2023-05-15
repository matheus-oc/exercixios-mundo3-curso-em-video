from random import randint
jogos = []
n = int(input('quantos jogos você quer fazer? '))
for c in range(0, n):
    jogo = []
    jogos.append(jogo)
    for i in range(0, 6):
        numeros = randint(0, 60)
        if numeros not in jogo and jogos:
            jogo.append(numeros)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')