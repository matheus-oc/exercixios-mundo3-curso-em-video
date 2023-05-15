aluno = dict()
aluno['nome'] = str(input('digite seu nome: '))
aluno['media'] = float(input('digite sua media: '))
print('-'*40)
if aluno['media'] >= 7.0:
    print(f'o aluno {aluno["nome"]} de media {aluno["media"]} esta aprovado!')
else:
    print(f'o aluno {aluno["nome"]} de media {aluno["media"]} esta reprovado')
print('-'*40)