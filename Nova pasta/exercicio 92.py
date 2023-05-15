from datetime import datetime
dados = dict()
dados['nome'] = str(input('digite seu nome: '))
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteiara de trabalho(0 não tem): '))
if dados['ctps'] != 0:
    dados['ddc'] = int(input('digite o ano que foi contratado: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['ddc'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
