#Aula 26 - Lista de Dicionários

#Tarefa Imprimir
#Considere a lista de dicionários abaixo contendo dados de notas dos alunos e idades.

alunos = [
    {"nome": "Ana", "idade": 18, "nota_mat": 85, "nota_port": 90},
    {"nome": "Beto", "idade": 22, "nota_mat": 78, "nota_port": 88},
    {"nome": "Carlos", "idade": 21, "nota_mat": 92, "nota_port": 81},
    {"nome": "Daniela", "idade": 19, "nota_mat": 74, "nota_port": 94}
]

#Imprima as notas de matemática apenas dos alunos com idade superior a 20 anos, conforme formato abaixo.

#Relatório de notas de matemática dos alunos com mais de 20 anos
#--------------------------------------------------
#Nome: xxxx, Idade: xx, Nota de matemática: xxx

print('Relatório de notas de matemática dos alunos com mais de 20 anos')
print('---------------------------------------------------------------')

nome= ''
age = 0
nota = 0
for idade in alunos:
    if idade['idade'] > 20:
        nome = idade['nome']
        age = idade['idade']
        nota = idade['nota_mat']
        print(f'Nome: {nome}, Idade: {age}, Nota de matemática: {nota}')

#Tarefa Contar elementos
#Considere a lista de dicionários abaixo contendo dados de notas dos alunos e idades.

alunos = [
    {"nome": "Ana", "idade": 18, "nota_mat": 85, "nota_port": 90},
    {"nome": "Beto", "idade": 22, "nota_mat": 78, "nota_port": 88},
    {"nome": "Carlos", "idade": 21, "nota_mat": 92, "nota_port": 81},
    {"nome": "Daniela", "idade": 19, "nota_mat": 74, "nota_port": 94}
]
#Conte quantos alunos tem notas superiores a 85 independente da matéria. Considere o fomato abaixo para imprimir a resposta.

#Quantidade de alunos com notas superiores a 85 em matemática: yy
#Quantidade de alunos com notas superiores a 85 em português: xx

count1 = 0
count2 = 0

for info in alunos:
    if info['nota_mat'] > 85:
        count1+=1
    if info['nota_port'] > 85:
        count2+=1
print(f'Quantidade de alunos com notas superiores a 85 em matemática: {count1}')
print(f'Quantidade de alunos com notas superiores a 85 em português: {count2}')

#Tarefa Acumular elementos
#Considere a lista de dicionários abaixo contendo dados de notas dos alunos e idades.

alunos = [
    {"nome": "Ana", "idade": 18, "nota_mat": 85, "nota_port": 90},
    {"nome": "Beto", "idade": 22, "nota_mat": 78, "nota_port": 88},
    {"nome": "Carlos", "idade": 21, "nota_mat": 92, "nota_port": 81},
    {"nome": "Daniela", "idade": 19, "nota_mat": 74, "nota_port": 94}
]
#Compare o totais de pontos das notas de matemática e português e informe quais das duas disciplinas os alunos estão performando melhor. Gere a saída no formato abaixo.

#A disciplina que os alunos mais fizeram pontos é: xxxxx
#O total de pontos dessa disciplina é: yy
port = 0
mat = 0
for info in alunos:
    if info['nota_port'] > 0:
        port += info['nota_port']
    if info['nota_mat'] > 0:
        mat += info['nota_mat']
if port > mat:
    disc = 'Portugues'
else:
    disc = 'Matematica'
print(f'A disciplina que os alunos mais fizeram pontos é: {disc}')
print(f'O total de pontos dessa disciplina é: {port}')

#Tarefa Calcular a Média
#Considere a lista de dicionários abaixo contendo dados de notas dos alunos e idades.

alunos = [
    {"nome": "Ana", "idade": 18, "nota_mat": 85, "nota_port": 90},
    {"nome": "Beto", "idade": 22, "nota_mat": 78, "nota_port": 88},
    {"nome": "Carlos", "idade": 21, "nota_mat": 92, "nota_port": 81},
    {"nome": "Daniela", "idade": 19, "nota_mat": 74, "nota_port": 94}
]
#Calcule a média geral das notas de matemática e português da turma. Gerar a saída no formato a seguir:

#Média geral de Matemática: yy
#Média geral de Português: xx
media1 = 0
media2 = 0
mat = 0
count1 = 0
port = 0
count2 = 0
for notas in alunos:
    if notas['nota_mat'] > 0:
        mat += notas["nota_mat"]
        count1+=1
    if notas['nota_port'] > 0:
        port+=notas["nota_port"]
        count2+=1
media1 = mat / count1
media2 = port / count2
print(f'Média geral de Matemática: {media1}')
print(f'Média geral de Português: {media2}')

#Tarefa Selecionar Maior Elemento
#Considere a lista de dicionários abaixo contendo dados de notas dos alunos e idades.

alunos = [
    {"nome": "Ana", "idade": 18, "nota_mat": 85, "nota_port": 90},
    {"nome": "Beto", "idade": 22, "nota_mat": 78, "nota_port": 88},
    {"nome": "Carlos", "idade": 21, "nota_mat": 92, "nota_port": 81},
    {"nome": "Daniela", "idade": 19, "nota_mat": 74, "nota_port": 94}
]
#Encontre qual a maior nota independente da matéria. Gere a saída no formato abaixo.

#Nome: xxxxx disciplina: xxxx nota: yyy

alt = 0
nota=0
nome = ''
disc = ''
for maior in alunos:
    if maior['nota_mat'] > alt:
        alt = maior["nota_mat"]
        nome = maior['nome']
    if maior['nota_port'] > alt:
        alt = maior['nota_port']
        nome = maior['nome']
if alt > alt:
    disc = 'Matematica'
    nota = alt
else: 
    disc = 'Portugues'
    nota = alt
print(f'Nome: {nome} disciplina: {disc} nota: {nota}')

#Tarefa Selecionar Menor Elemento
#Considere a lista de dicionários abaixo contendo dados de notas dos alunos e idades.

alunos = [
    {"nome": "Ana", "idade": 18, "nota_mat": 85, "nota_port": 90},
    {"nome": "Beto", "idade": 22, "nota_mat": 78, "nota_port": 88},
    {"nome": "Carlos", "idade": 21, "nota_mat": 92, "nota_port": 81},
    {"nome": "Daniela", "idade": 19, "nota_mat": 74, "nota_port": 94}
]
#Qual o aluno mais novo? Gere a saída no formato abaixo.

#Nome: xxxxx
#Idade: yy
novo = 50
nome = ''
for age in alunos:
    if age['idade'] < novo:
        novo = age['idade']
        nome = age['nome']
print(f'Nome: {nome}')
print(f'Idade: {novo}')

#Exercícios adicionais
#Calcular: média, percentuais, etc

#Armazenando resultado do cálculo em variáveis temporárias para uso posterior
#Incluir elementos a partir de variáveis

#Tarefa Calcular aumento nas notas e armazenar o resultado em variável temporária
#Considere a lista de dicionários abaixo contendo dados de notas dos alunos e idades.

alunos = [
    {"nome": "Ana", "idade": 18, "nota_mat": 85, "nota_port": 90},
    {"nome": "Beto", "idade": 22, "nota_mat": 78, "nota_port": 88},
    {"nome": "Carlos", "idade": 21, "nota_mat": 92, "nota_port": 81},
    {"nome": "Daniela", "idade": 19, "nota_mat": 74, "nota_port": 94}
]
#Professor de matemática resolveu adicionar mais 0,5 nas notas de todos os alunos em função da anulação de uma questão. Armazene o resultado em um dicionário contendo o nome do aluno e sua nova nota de matemática. Gere a saída no formato abaixo a partir do dicionário gerado no passo anterior.

#Nome: xxxxx, nota matemática: xx
#Nome: yyyyy, nota matemática: zz
galinha = dict()
nova = 0
nome=''
for nota in alunos:
    if nota['nota_mat'] > 0:
        nova = nota['nota_mat'] + 0.5
        nome = nota['nome']
        galinha[nota['nome']] = nova
        print(f'Nome: {nome}, nota matematica: {nova}')

#Tarefa Incluir elementos a partir de uma variável adicional de entrada
#Considere a lista de dicionários abaixo contendo dados de notas dos alunos e idades.

alunos = [
    {"nome": "Ana", "idade": 18, "nota_mat": 85, "nota_port": 90},
    {"nome": "Beto", "idade": 22, "nota_mat": 78, "nota_port": 88},
    {"nome": "Carlos", "idade": 21, "nota_mat": 92, "nota_port": 81},
    {"nome": "Daniela", "idade": 19, "nota_mat": 74, "nota_port": 94}
]

notas_fisica = [
    {"nome": "Ana", "nota_fisica": 70},
    {"nome": "Carlos", "nota_fisica": 50},
    {"nome": "Beto", "nota_fisica": 60},
    {"nome": "Daniela", "nota_fisica": 30}
]
#Insira na lista de dicionários alunos as notas de física constante na variável notas_física. Imprima o resultado final da lista de dicionário alunos atualizada conforme abaixo.

# alunos = [
#     {"nome": "Ana", "idade": 18, "nota_mat": 85, "nota_port": 90, "nota_fisica": 70},
#     {"nome": "Beto", "idade": 22, "nota_mat": 78, "nota_port": 88, "nota_fisica": 60},
#     {"nome": "Carlos", "idade": 21, "nota_mat": 92, "nota_port": 81, "nota_fisica": 50},
#     {"nome": "Daniela", "idade": 19, "nota_mat": 74, "nota_port": 94, "nota_fisica": 30}
# ]

for nota_fisica in notas_fisica:
    nome_aluno = nota_fisica['nome']
    for aluno in alunos:
        if aluno['nome'] == nome_aluno:
            aluno['nota_fisica'] = nota_fisica['nota_fisica']
            break
print(alunos)