#Aula 6 - Exercícios em Sala de Aula

#Exercícios sobre estrutura de dados tipo Dicionário

#Exercício 1
#Neste exercício, você deve criar um dicionário chamado banco com chaves para nome, fundacao e total_de_agencias. O banco será o "Banco do Brasil", fundado em 1808, com um total de 5000 agências.

# Crie um dicionário chamado 'banco' com as informações do Banco do Brasil
banco = {"nome": "Banco do Brasil", "fundacao": 1808, "total_de_agencias": 5000}
print(banco)

#Exercício 2
#Neste exercício, você deve adicionar uma chave regulador ao dicionário banco criado anteriormente e atribuir o valor "Banco Central do Brasil".

# Adicione a chave 'regulador' com o valor "Banco Central do Brasil" ao dicionário 'banco'
banco['regulador'] = 'Banco do Brasil'
print(banco)

#Exercício 3
#Uma ONG que trabalha com reflorestamento registra o número de árvores plantadas por voluntários em diferentes locais. Utilize um dicionário para armazenar o nome do local como chave e o número de árvores plantadas como valor. Escreva um código para adicionar três locais com seus respectivos números de árvores plantadas e, em seguida, calcule o total de árvores plantadas.

reflorestamento = {
    "Parque da Cidade": 3020,
    "Margens do Rio": 1500,
    "Área Urbana": 2000
}

total_arvores = 0
for arvores in reflorestamento.values():
    total_arvores = total_arvores + arvores

print(f"Total de árvores plantadas: {total_arvores}")

#Exercício 4
#Uma ONG dedicada à conservação ambiental quer identificar as áreas onde o número de árvores plantadas é inferior a 500 para priorizar novas campanhas de reflorestamento. Escreva um código que liste essas áreas prioritárias.

arvores_plantadas = {
    "Área 1": 450,
    "Área 2": 600,
    "Área 3": 300,
    "Área 4": 700
}

areas_prioritarias = []
for area, arvores in arvores_plantadas.items():
   if arvores < 500:
    areas_prioritarias = area

    #areas_prioritarias.append(area)
    #poe o print fora do laço for

    print("Áreas prioritárias para reflorestamento:", areas_prioritarias)

#Exercício 5
#Neste exercício, você deve atualizar o valor da chave total_de_agencias para 5100.

# Atualize o valor da chave 'total_de_agencias' para 5100
banco['total_de_agencias'] = 5100
print(banco)

#Exercício 6
#Retorne um dicionário apenas com as ONGs que estão em países lusófonos do seguinte dicionário {"ONG1":"Brazil", "ONG2":"USA", "ONG3":"Portugal", "ONG4":"Spain", "ONG5":"Mozambique"}

dicionarioONGPais = {"ONG1":"Brazil", "ONG2":"USA", "ONG3":"Portugal", "ONG4":"Spain", "ONG5":"Mozambique"}
lusofonos = ["Brazil", "Portugal", "Mozambique", "Angola", "Cape Verde", "Guinea Bissau", "East Timor", "Equatorial Guinea", "Macau"]
dic_lusofona = {}

for key, value in dicionarioONGPais.items():
  if value in lusofonos:
    dic_lusofona[key] = value
print(f"ONG's lusofonas {dic_lusofona}")

#Exercício 7
#Neste exercício, você deve remover a chave fundacao do dicionário banco.

# Remova a chave 'fundacao' do dicionário 'banco'
del (banco['fundacao'])
print(banco)

#Exercício 8
#Uma ONG de direitos dos animais quer rastrear o número de leis aprovadas em favor da proteção animal por ano. Escreva um código que adicione o número de leis aprovadas em um ano específico e depois calcule a média anual de leis aprovadas com base nos dados disponíveis.

leis_protecao_animal = {
    2018: 3,
    2019: 5,
    2020: 4
}

# Adicionando novas leis
leis_protecao_animal[2021] = 1

# Calculando média de leis aprovadas
media_leis = (sum(leis_protecao_animal.values())) / len(leis_protecao_animal)

print(f"Média anual de leis aprovadas: {media_leis:.2f}")

#Exercício 9
#Uma ONG de apoio a pequenos empreendedores mantém um registro de doações recebidas por mês. Se um mês alcança doações acima de R$10.000, ele é considerado um mês de grande sucesso. Escreva um código que determine quantos meses tiveram grande sucesso.

doacoes = {
    "Janeiro": 9500,
    "Fevereiro": 10500,
    "Março": 12000,
    "Abril": 8500
}

meses_sucesso = 0

for mes, valores in doacoes.items():
    if valores > 10000:
        meses_sucesso += 1

print(f"Número de meses de grande sucesso: {meses_sucesso}")

#Exercício 10
#Neste exercício, você deve verificar se a chave nome está presente no dicionário banco.

banco = {"nome": "Banco do Brasil", "fundacao": 1808, "total_de_agencias": 5000}
existe = 'nome' in banco
print(existe)

#Exercício 11
#Neste exercício, você deve criar um dicionário chamado regulatorio que guarda informações sobre os bancos e suas obrigações regulatórias. O dicionário deve ter chaves para banco, obrigacoes, e multas. Para o banco, use "Itaú". obrigacoes será uma lista contendo "Basiléia III" e "IFRS 9". multas será um valor inteiro, digamos 5.

# Crie um dicionário chamado 'regulatorio' com as informações solicitadas
regulatorio = {"banco": "Itaú", "obrigacoes": ["Basiléia III", "IFRS 9"], "multas": 5}
print(regulatorio)

#Exercício 12
#Neste exercício, condiderando o dicionário regulatorio acesse o segundo item da chave obrigacoes.

obrigacao_valor = regulatorio ["obrigacoes"][1]
print(obrigacao_valor)

#Exercício 13
#Neste exercício, crie um dicionário chamado taxas que armazene as taxas de juros dos empréstimos para diferentes tipos de contas. Utilize "Pessoa Física" com uma taxa de 5.2% e "Pessoa Jurídica" com uma taxa de 7.5%.

# Crie um dicionário chamado 'taxas' com as informações solicitadas
taxas = {"Pessoa Física": 5.2/100, "Pessoa Jurídica": 7.5/100}
print(taxas)

#Exercício 14
#Neste exercício, atualize o dicionário taxas para incluir uma nova chave "MEI" (Microempreendedor Individual) com uma taxa de 4.8%.

# Atualize o dicionário 'taxas' para incluir a chave 'MEI' com uma taxa de 4.8%
taxas["MEI"] = 4.8/100
print(taxas)

#Exercício 15
#Dicionários no Python funcionam em chave-valor. Dadas duas listas ONGs = [NGO1, NGO2, NGO3, NGO4, NGO5] e Pais = [Brazil, Portugal, Equador, Angola, Mozambique], faça um dicionário relacionando o nome da ONG com o pais.

ONGs = ['NGO1', 'NGO2', 'NGO3', 'NGO4', 'NGO5']
Pais = ['Brazil', 'Portugal', 'Equador', 'Angola', 'Mozambique']
dicionarioONGPais = {}

for i in range(len(ONGs)):
    dicionarioONGPais[ONGs[i]] = Pais[i]

print(f"Dicionário de ONGs e País: {dicionarioONGPais}")

#ou
# for ong, pais in zip(ONGs, Pais):
#     dicionarioONGPais[ong] = pais
# print(f"Dicionário de ONGs e País: {dicionarioONGPais}")