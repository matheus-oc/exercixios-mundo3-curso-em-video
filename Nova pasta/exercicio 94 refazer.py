mulheres = []
cont = 0
media = idades = 0
acima = []
while True:
    pessoas = dict()
    pessoas['nome'] = str(input('digite seu nome: '))
    pessoas['sexo'] = str(input('digite seu sexo [M/F]: ')).upper()
    pessoas['idade'] = int(input('digite sua idade: '))
    idades += pessoas['idade']
    cont += 1
    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
    if pessoas['idade'] > media:
        acima.append(pessoas['nome'])
    r = str(input('você deseja continuar?S/N: ')).upper()
    if r == 'N':
        break
media = idades / cont
print(f'o numero de pessoas cadastradas foi : {cont}')
print(f' as mulhres cadastradas foram : {mulheres}')
print(f'as pessoas com idade acima da media são: {acima}')