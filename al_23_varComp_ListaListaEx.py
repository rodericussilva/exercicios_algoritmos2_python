#Aula 23 - Variáveis compostas Exercícios ( Lista de Listas)
#Exercício 1: Aumentar a Receita de Todas as Lojas em 10%
#Considere a lista de listas abaixo contendo informações de lojas, localizações e receitas. Os comerciantes desejam aumentar as receitas de suas lojas em 10%. Imprima os resultados conforme saída posteriomente mostrada.

lojas = [
    ["Loja A", "Nova York", 1200000],
    ["Loja B", "Los Angeles", 950000],
    ["Loja C", "Chicago", 850000]
]
# Saída
#Loja Loja A em Nova York agora tem uma receita estimada de R$1320000.
#Loja Loja B em Los Angeles agora tem uma receita estimada de R$1045000.
#Loja Loja C em Chicago agora tem uma receita estimada de R$935000.

nomeLoja = ''
local = ''
receita = 0

for loja in lojas:
    nomeLoja = loja[0]
    local = loja[1]
    receita = int(loja[2] * 1.10)
    print(f'Loja {nomeLoja} em {local} agora tem uma receita estimada de R$ {receita}')

#Exercício 2: Listar Lojas em Uma Cidade Específica
#Listar todas as lojas e receitas numa cidade específica. A cidade deverá ser informada em uma variável no ínicio do programa e pode variar. Considere a lista de listas abaixo como a variável de entrada.

lojas = [
    ["Loja A", "Nova York", 1200000],
    ["Loja B", "Los Angeles", 950000],
    ["Loja C", "Chicago", 850000],
    ["Loja d", "Los Angeles", 850000]
]

# Cidade desejada
cidade_desejada = "Los Angeles"
# saída esperada para a cidade de Los Angeles
#Lojas em Los Angeles:
#Loja B com receita de R$950000.
#Loja d com receita de R$850000.

print(f'Lojas em {cidade_desejada}')
for loja in lojas:
    if loja[1] == cidade_desejada:
        print(f'{loja[0]} com receita de {loja[2]}')

#Exercício 3: Contar quantas vezes um país ganhou medalha de ouro
#Considere a lista de listas abaixo que descreve informações sobre diferentes eventos olímpicos, suas localizações, ano em que ocorreram e medalhas de ouro ganhas por um país específico.

#Determinar quantas vezes os Estados Unidos ganharam medalhas de ouro.

olimpiadas = [
    ["Natação", "Tóquio", 2021, "Estados Unidos"],
    ["Atletismo", "Rio de Janeiro", 2016, "Jamaica"],
    ["Ginástica Artística", "Londres", 2012, "Estados Unidos"],
    ["Judo", "Pequim", 2008, "Japão"],
    ["Vôlei", "Atenas", 2004, "Brasil"],
    ["Basquete", "Sydney", 2000, "Estados Unidos"],
    ["Futebol", "Atlanta", 1996, "Nigéria"]
]
count = 0
for pais in olimpiadas:
    if pais[3] == 'Estados Unidos':
        count+=1
print(f'O referido pais ganhou ouro {count} vezes')

#Exercício 4: Encontrar o evento olímpico mais antigo na lista
#Considere a lista de listas abaixo que descreve informações sobre diferentes eventos olímpicos, suas localizações, ano em que ocorreram e medalhas de ouro ganhas por um país específico.

#Identificar qual é o evento olímpico mais antigo registrado na lista.

olimpiadas = [
    ["Natação", "Tóquio", 2021, "Estados Unidos"],
    ["Atletismo", "Rio de Janeiro", 2016, "Jamaica"],
    ["Ginástica Artística", "Londres", 2012, "Estados Unidos"],
    ["Judo", "Pequim", 2008, "Japão"],
    ["Vôlei", "Atenas", 2004, "Brasil"],
    ["Basquete", "Sydney", 2000, "Estados Unidos"],
    ["Futebol", "Atlanta", 1996, "Nigéria"]
]
ancien = 0
pay = ''
for ano in olimpiadas:
    if ano[2] < 2000:
        ancien = ano[2]
        pay = ano[1]
print(f'O mais antigo foi em {pay} no ano de {ancien}')

#Exercício 5: Listar todos os eventos que ocorreram em um país específico
#Considere a lista de listas abaixo que descreve informações sobre diferentes eventos olímpicos, suas localizações, ano em que ocorreram e medalhas de ouro ganhas por um país específico.

#Listar todos os eventos olímpicos que ocorreram em Sydney.

olimpiadas = [
    ["Natação", "Tóquio", 2021, "Estados Unidos"],
    ["Atletismo", "Rio de Janeiro", 2016, "Jamaica"],
    ["Ginástica Artística", "Londres", 2012, "Estados Unidos"],
    ["Judo", "Pequim", 2008, "Japão"],
    ["Vôlei", "Atenas", 2004, "Brasil"],
    ["Basquete", "Sydney", 2000, "Estados Unidos"],
    ["Futebol", "Atlanta", 1996, "Nigéria"]
]
pay = 'Sydney'
count = 0
for event in olimpiadas:
    if event[1] == pay:
        count+=1
print(f'houveram {count} em {pay}')