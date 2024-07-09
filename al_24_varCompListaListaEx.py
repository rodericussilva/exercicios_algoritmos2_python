#Aula 24: Técnicas de programação básicas em Lista de Listas: resolução de problemas práticos
#Agenda:

#Exercitar construçao de algoritmos para a resolução de problemas que envolvem lista de listas na sua entrada utilizando as técnicas de programação básicas.
#Técnicas de programação básica
#As técnicas de programação básicas são habilidades essenciais para qualquer programador, pois envolvem manipulação básica de dados para resolver problemas abaixo designados, dentre outros:

#Imprimir dados
#Selecionar dados específicos
#Contar elementos
#Acumular elementos
#Calcular: média, percentuais, etc
#Usando apenas uma variável de entrada
#Usando mais de uma variável de entrada relacionadas
#Armazenando resultado do cálculo em variáveis temporárias para uso posterior
#Selecionar maior elemento
#Selecionar menor elemento
#(*) Ordenar
#Incluir, Excluir, Alterar e Deletar elementos
#etc
#Cada uma dessas técnicas é um bloco de construção básico no desenvolvimento de software e é aplicável em uma variedade de cenários de programação, e que se podem combinar desde scripts simples até sistemas complexos. Elas formam a base sobre a qual habilidades mais avançadas são construídas, como manipulação de arquivos, interações de banco de dados, desenvolvimento de sistemas e desenvolvimento de interfaces gráficas, etc.

#(*) não será vista nesse momento

#Aplicação das Técnicas de programação básicas
#A seguir estudaremos de forma sistematizada a resolução de problemas por meio da construção de algoritmos utilizando as técnicas fundamentais de programação envolvendo a variável de entrada tipo lista de Listas.

#Observação: em todos os algoritmos desenvolvidos necessariamente necessariamente devem ser utilizada(s) seguinte(s) estrutura(s) de controle para realizar o loop de leitura nos dados de entrada: for, while, list comprehension ou dictionary comprehension.

#Utilizaremos o seguinte serviço web para melhor compreender e visualizar os algoritmos estudados.

#https://pythontutor.com/

#Tarefa Imprimir
#Considere a lista de listas abaixo contendo nome, idade e salário dos funcionários.

dados = [
    ["João", 30, 3000],
    ["Maria", 25, 3500],
    ["Pedro", 40, 2800],
    ["Ana", 35, 4000],
    ["Carlos", 28, 3200]
]
#Imprima a as informações dos funcionários com mais de 30 anos conforme formato abaixo.

#Relatório funcionários com mais de 30 anos
#--------------------------------------------------
#Nome: Pedro, Idade: 40, Salário: R$ 2800
#Nome: Ana, Idade: 35, Salário: R$ 4000

print('Relatório DE funcionários com mais de 30 anos')
print('-----------------------------------------------')

for peao in dados:
    if peao[1] > 30:
        print(f'Nome: {peao[0]}, Idade: {peao[1]}, salário: R$ {peao[2]}')
        

#Tarefa Contar elementos
#Considere a lista de listas abaixo contendo nome, idade e salário dos funcionários de uma empresa.

dados = [
    ["João", 30, 3000],
    ["Maria", 25, 3500],
    ["Pedro", 40, 2800],
    ["Ana", 35, 4000],
    ["Carlos", 28, 3200]
]
#Conte quantos funcionários ganham mais de 3000 e gere a saída conforme modelo abaixo.

#Quantidade de funcinários com salários acima de 3000: xx
count = 0
for salario in dados:
    if salario[2] > 3000:
        count+=1
print(f'Quantidade de funcinários com salários acima de 3000: {count}')

#Tarefa Acumular elementos
#Considere a lista de listas abaixo contendo nome, idade e salário dos funcionários de uma empresa.

dados = [
    ["João", 30, 3000],
    ["Maria", 25, 3500],
    ["Pedro", 40, 2800],
    ["Ana", 35, 4000],
    ["Carlos", 28, 3200]
]
#Calcule o total dos salários dos funcionários com mais de 30 anos.

#O total dos salários de funcionários com mais de 30 anos é: xx
total = 0
for idade in dados:
    if idade[1] > 30:
        total += idade[2]
print(f'Quantidade de funcinários com salários acima de 3000: {total}')

#Tarefa Calcular a Média
#Considere a lista de listas abaixo contendo nome, idade e salário dos funcionários de uma empresa.

dados = [
    ["João", 30, 3000],
    ["Maria", 25, 3500],
    ["Pedro", 40, 2800],
    ["Ana", 35, 4000],
    ["Carlos", 28, 3200]
]
#Calcule a média salarial os funcionários com mais de 4 letras no nome.

#A média salarial dos funcionários é: R$ xx
soma = 0
count = 0
for nome in dados:
    if len(nome[0]) > 4:
        count+=1
        soma += nome[2]
media = soma / count
print(f'A média salarial dos funcionários é: R$ {media}')

#Tarefa Selecionar Maior Elemento
#Considere a lista de listas abaixo contendo nome, idade e salário dos funcionários de uma empresa.

dados = [
    ["João", 30, 3000],
    ["Maria", 25, 3500],
    ["Pedro", 40, 2800],
    ["Ana", 35, 4000],
    ["Carlos", 28, 3200]
]
#Encontre qual o nome do funcionário com maior salário.

#Nome: xxxxx
#Salário: R$ yy

maior = 0
for salario in dados:
    if salario[2] > maior:
        maior = salario[2]
        nome = salario[0]
print(f'Nome: {nome}')
print(f'Salário: {maior}')

#Tarefa Selecionar Menor Elemento
#Considere a lista de listas abaixo contendo nome, idade e salário dos funcionários de uma empresa.

dados = [
    ["João", 30, 3000],
    ["Maria", 25, 3500],
    ["Pedro", 40, 2800],
    ["Ana", 35, 4000],
    ["Carlos", 28, 3200]
]
#Encontre qual o nome do funcionário com menor idade considerando apenas aqueles que ganham menos de R$ 3700.

#Nome: xxxxx
#Idade: yy
menor = 6000
idade = 0
nome = ''
for salario in dados:
    if salario[2] < menor:
        menor = salario[2]
        nome = salario[0]
        idade = salario[1]
        
print(f'Nome: {nome}')
print(f'Idade: {idade}')

#Exercícios adicionais
#Calcular: média, percentuais, etc
#Armazenando resultado do cálculo em variáveis temporárias para uso posterior
#Considere a lista de listas abaixo contendo nome, idade e salário dos funcionários de uma empresa.

# Dados de nome, idade e salário-base dos funcionários de uma empresa
dados = [
    ["João", 30, 3000],
    ["Maria", 25, 3500],
    ["Pedro", 40, 2800],
    ["Ana", 35, 4000],
    ["Carlos", 28, 3200]
]
#Calcule o bônus no valor de 10% do salário para apenas os funcionários com mais de 30 anos de idade. Armazene o resultado do cálculo em uma lista de listas contendo para cada funcionário: nome e valor do bônus. Imprima a saída do programa conforme abaixo utilizando os dados contidos na lista de lista de bônus gerada.

#Bônus a serem concedidos:
#Nome: Maria, Bônus: R$ 350.00
#Nome: Carlos, Bônus: R$ 320.00

bonus = 10/100
result = list()
nome = ''
valor = 0
print('Bônus a serem concedidos:')
for salario in dados:
    if salario[1] > 30:
        valor = salario[2] * bonus
        nome = salario[0]
        result.append(nome)
        result.append(valor)
        print(f'Nome: {result[0]}, Bonus: {result[1]}')

#Tarefa Calcular horas-extras com mais de uma variável de entrada relacionadas
#Considere as varáveis abaixo contendo dados sobre nome, idade, salário, horas-extras e valor da hora-extra.

# Dados de nome, idade e salário-base dos funcionários de uma empresa
dados = [
    ["João", 30, 3000],
    ["Maria", 25, 3500],
    ["Pedro", 40, 2800],
    ["Ana", 35, 4000],
    ["Carlos", 28, 3200]
]

# Lista com a quantidade de horas extras de cada funcionário
horas_extras = [2, 3, 1, 4, 2]

# Valor pago por hora extra
valor_hora_extra = 100
#Calcule o salário de cada funcionário sabendo que as horas-extras devem ser calculadas e somadas ao salário base. Gere a saída do programa conforme abaixo.

#Nome: João, Salário Total: R$ 3200
#Nome: Maria, Salário Total: R$ 3800
#Nome: Pedro, Salário Total: R$ 2900
#Nome: Ana, Salário Total: R$ 4400
#Nome: Carlos, Salário Total: R$ 3400

for extra in range(len(dados)):
    nome, idade, salario = dados[extra]
    total_horas = horas_extras[extra] * valor_hora_extra
    salario_total = salario + total_horas
    print(f'Nome: {nome}, salário total: {salario_total}')