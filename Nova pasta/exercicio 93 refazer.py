jogador = dict()
jogador['nome'] = str(input('digite seu nome: '))
jogador['gols por partida'] = int(input('numero de gols feitos em cada partida: '))
jogador['jogos'] = int(input('numeros de jogos que participou: '))
jogador['saldo de gols'] = jogador['gols por partida'] * jogador['jogos']
for k, v in jogador.items():
    print(f' -{k} tem o valor de {v}.')