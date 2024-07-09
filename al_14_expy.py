# Aula 14 - Exercícios em Sala de Aula

# Exercícios sobre manipulação de Funções

# Exercício 1
# Criar uma função chamada total_alunos que aceita uma lista com o número de alunos em diferentes classes e retorna o número total de alunos na escola.

# Cálculo do total de alunos na escola

def total_alunos(alunos):
    total = sum(alunos)
    return total

print(total_alunos([30, 35, 40, 25]))

# Exercício 2
# Criar uma função chamada calcular_media que aceita uma lista de notas de alunos e retorna a média das notas.

# Cálculo da média de notas de alunos

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

print(calcular_media([80, 90, 100, 85, 70]))

# Exercício 3
# Criar uma função chamada aprovar_aluno que aceita uma média de notas e retorna "Aprovado" se a média for maior ou igual a 70, caso contrário retorna "Reprovado".

# Verificação de aprovação de aluno
def aprovar_aluno(nota):
    if nota >= 70:
        return "Aprovado"
    else:
        return "Reprovado"

print(aprovar_aluno(75))

# Exercício 4
# Neste exercício, crie uma função calcular_valor_total que recebe um dicionário de produtos, onde cada produto é representado por um dicionário contendo o "nome", o "preco" e a "quantidade" comprada. A função deve retornar o valor total da compra.

def calcular_valor_total(produtos):
    total = 0
    for produto in produtos:
        total = total + (produto['preco'] * produto['quantidade'])
    return total

produtos = [{'nome':'arroz', 'preco':5, 'quantidade':2}, {'nome':'feijão', 'preco':10, 'quantidade':3}]
print(calcular_valor_total(produtos))

# Exercício 5
# Neste exercício, você deve criar uma função chamada calcula_imposto que aceite uma lista de receitas e uma taxa de imposto. A função deve calcular o imposto para cada receita e retornar uma lista de impostos.

def calcula_imposto(receitas, taxa):
    impostos = []
    for receita in receitas:
        impostos.append(receita * taxa)  # Substitua os espaços em branco para calcular o imposto.
    return impostos

receitas = [1000, 2000, 3000, 4000, 5000]
taxa = 0.1  # 10%
print(calcula_imposto(receitas, taxa))

# Exercício 6
# Neste exercício, você deve criar uma função chamada calcular_imposto que receberá dois parâmetros: renda e aliquota. A função deve calcular o imposto com base na alíquota informada e retornar o valor do imposto a ser pago. Caso a aliquota seja maior que 27.5, a função deve retornar "Alíquota inválida".

def calcular_imposto(renda, aliquota):
    if aliquota > 27.5:
        return "Alíquota inválida"
    else:
        return renda * (aliquota / 100)  # Preencha aqui

print(calcular_imposto(1000, 27.5))

# Exercício 7
# Neste exercício, crie uma função chamada aumenta_investimento. A função deve receber dois argumentos: um dicionário de políticas e seus respectivos investimentos e uma porcentagem de aumento. A função deve retornar um novo dicionário com os valores atualizados.


def aumenta_investimento(dicionario_investimentos, porcentagem):
    for politica, valor in dicionario_investimentos.items():
        dicionario_investimentos[politica] = valor + (valor * porcentagem/100)
    return dicionario_investimentos

print(aumenta_investimento({"saude": 500000, "educacao": 300000, "infraestrutura": 200000}, 10))

# Exercício 8
# Neste exercício, você deve definir duas funções: verificar_elegibilidade e imprimir_elegibilidade. A primeira função checará se uma pessoa é elegível para um benefício com base em sua idade (acima de 60 anos é elegível). A segunda função irá imprimir o resultado.

def verificar_elegibilidade(idade):
    return idade >= 60

def imprimir_elegibilidade(idade):
    if verificar_elegibilidade(idade):
        print("Elegível para o benefício!")
    else:
        print("Não elegível para o benefício.")

imprimir_elegibilidade(65)

# Exercício 9
# Neste exercício, você deve criar duas funções: calcular_total_investimento e ajuste_inflacionario. A primeira função deve calcular o investimento inicial para um programa social com base no valor por beneficiário e no total de beneficiários. A segunda função deverá calcular o valor ajustado com a inflação.

def calcular_total_investimento(valor_por_beneficiario, total_beneficiarios):
    return valor_por_beneficiario * total_beneficiarios

def ajuste_inflacionario(investimento_inicial, taxa_inflacao):
    return investimento_inicial + (investimento_inicial * taxa_inflacao / 100)

investimento = calcular_total_investimento(100, 250)
print("Investimento com ajuste inflacionário:", ajuste_inflacionario(investimento, 5))

# Exercício 10
# Considere o programa abaixo que utiliza um dicionário simples como entrada, contendo o nome do produto como chave e a quantidade em estoque como valor. O objetivo será identificar quais produtos estão abaixo de uma quantidade mínima de estoque definida e gerar um dicionário como saída com o nome do produto como chave e o valor com a quantidade que falta para atingir a quantidade mínima.

# Elabore uma tabela de rastremento de variáveis do código utilizando papel ou planilha excel.

# 1 quantidade_minima = 7
# 2 estoque = {
# 3     'Caneta': 10,
# 4     'Lápis': 5,
# 5     'Borracha': 8,
# 6     'Papel': 4
# 7 }
# 8
# 9  def identificar_reposicao(estoque):
# 10    produtos_reposicao = {}
# 11    for produto, qtd in estoque.items():
# 12        if qtd < quantidade_minima:
# 13            unidades_faltantes = quantidade_minima - qtd
# 14            produtos_reposicao[produto] = unidades_faltantes
# 15    return produtos_reposicao
# 16
# 17 produtos_para_reposicao = identificar_reposicao(estoque)
# 18 print(produtos_para_reposicao)