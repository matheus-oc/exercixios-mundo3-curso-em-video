time = []
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('nome do jogador: '))
    tot = int(input(f'quantas partidadas o {jogador["nome"]}'))
    for c in range(0, tot):
        partidas.append(int(input(f'  quantos gols na partida {c}')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('quer continuar?')).upper()[0]
        if r != 'SN':
            break
        print('erro! digite novamente')
    if r == 'N':
        break
for i in jogador.keys():
    print(f'{i:<15}', end='')
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
        print()
print('-'*40)
while True:
    busca = int(input('mostrar dados de qual jogador?'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'erro! Não existe jogador com o codigo {busca}!')
    else:
        print(f'levantamento do jogador {time[busca["nome"]]} ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   no jogo{i+1} fez {g} gols')
    print('-'*40)