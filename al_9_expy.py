# Exercício
# Neste exercício, você deve criar um loop for com range para somar o número de dias de férias de cinco funcionários. Suponha que cada funcionário tem 10 dias de férias. Complete o código para somar os dias de férias e imprimir o total.

soma = 0
for funcionario in range(10):
    soma = soma + 1
print(soma)

# Exercício
# Realizar um loop for para calcular a soma de todos os salários constantes em uma varável tipo lista chamada salarios. O resultado deve ser armazenado em uma variável chamada soma_salarios.

# Utilize um loop `for` para calcular a soma de todos os salários em uma lista chamada 'salarios'

salarios = [2000, 3000, 4000, 5000]
soma_salarios = 0
for i in salarios:
  soma_salarios = soma_salarios + i
print(soma_salarios)

# Exercício
# Suponha que você inicie com um salário anual e receba um aumento fixo anual. Usando uma estrutura de repetição while, calcule quantos anos levará para seu salário dobrar.

# Variáveis de entrada
salario_inicial = float(input("Digite seu salário anual inicial: "))
taxa_aumento = float(input("Digite a taxa de aumento anual (exemplo: 0.03 para 3%): "))

# Inicializações
salario_atual = salario_inicial
anos = 0

# Loop

while salario_atual < salario_inicial * 2:
    salario_atual *= (1 + taxa_aumento)
    anos += 1

# imprimindo resultado final
print(f"Levará {anos} anos para seu salário dobrar.")

# Exercício
# Realizar um loop for para imprimir o nome e a idade de aposentadoria de cada pessoa constantes em uma variável tipo dicionário chamado aposentadoria.

# Utilize um loop `for` para imprimir o nome e a idade de aposentadoria de cada pessoa em um dicionário chamado 'aposentadoria'
aposentadoria = {'Alice': 65, 'Bob': 67, 'Clara': 63}
for pessoa, idade in aposentadoria.items():
    print(f"{pessoa} se aposentará aos {idade} anos")

# Exercício
# Realizar um loop for para calcular o número total de dias de férias acumuladas por um empregado em uma variável tipo lista chamada ferias_por_ano.

# Utilize um loop `for` para calcular o número total de dias de férias acumuladas por um empregado em uma lista chamada 'ferias_por_ano'

ferias_por_ano = [10, 12, 15]
total_ferias = 0
for total_ferias in ferias_por_ano:
    total_ferias += 1
print(f"total de {total_ferias} dias")

# Exercício
# Realizar um loop for para calcular o total de contribuições mensais feitas por um trabalhador cujos valores estão registrados em uma variável tipo lista chamada contribuicoes.

# Utilize um loop `for` para calcular o total de contribuições mensais feitas por um trabalhador em uma lista chamada 'contribuicoes'

contribuicoes = [100, 150, 200]
for total in contribuicoes:
    total += 1
print(f"Total de {total}")

# Exercício
# Realizar um loop for para listar todos os anos em que um funcionário deve contribuir para a previdência. Os anos vão de 2020 a 2040.

# Utilize um loop `for` para listar todos os anos em que um funcionário deve contribuir para a previdência
for ano in range(2020, 2040):
    print(ano)

# Exercício
# Você quer se aposentar em uma certa idade e, para isso, precisa economizar uma quantia específica de dinheiro. Com um salário mensal fixo, quanto tempo levará para você atingir sua meta de economia, considerando que você consegue economizar uma porcentagem fixa do seu salário todo mês?

# Variáveis de entrada
salario_mensal = float(input("Digite seu salário mensal: "))
porcentagem_economia = float(input("Digite a porcentagem do salário a ser economizada (exemplo: 20 para 20%): ")) / 100
meta_economia = float(input("Digite sua meta de economia para aposentadoria: "))

economia = salario_mensal * porcentagem_economia
tempo = meta_economia / economia
anos = tempo * 12
print(f"Você levará {anos:.0f} anos para juntar {meta_economia}")

# Exercício
# Neste exercício, você deve criar um programa que utilize a estrutura de controle for para percorrer uma lista de estados da região Nordeste do Brasil. Para cada estado, você deve verificar se ele está na lista de estados com políticas de desenvolvimento e, em seguida, imprimir o nome do estado e se ele tem ou não políticas de desenvolvimento.

# Crie um programa que percorra a lista de estados da região Nordeste e imprima se eles têm ou não políticas de desenvolvimento.
estados_nordeste = ['Bahia', 'Sergipe', 'Alagoas', 'Pernambuco', 'Paraíba', 'Rio Grande do Norte', 'Ceará', 'Piauí', 'Maranhão']
politicas_desenvolvimento = ['Bahia', 'Ceará', 'Pernambuco']

for estado in estados_nordeste:
    if estado in politicas_desenvolvimento:
        print(estado, "Tem politica de desenvolvimento.")
    else:
        print(estado, "Não tem política de desenvolvimento.")
        
# Exercício
# Neste exercício, você deve criar um programa que utilize a estrutura de controle for para percorrer uma lista de cidades da região Nordeste. Para cada cidade, você deve verificar se ela está na lista de cidades com projetos de sustentabilidade e, em seguida, imprimir o nome da cidade e se ela tem ou não projetos de sustentabilidade.

# Crie um programa que percorra a lista de cidades da região Nordeste e imprima se elas têm ou não projetos de sustentabilidade.
cidades_nordeste = ['Recife', 'Salvador', 'Fortaleza', 'São Luís', 'Maceió']
cidades_sustentaveis = ['Recife', 'São Luís', 'Maceió']

for cidade in cidades_nordeste:
    if cidade in cidades_sustentaveis:
        print(f"{cidade}  tem projetos sustentáveis")
    else:
        print(f"{cidade} não tem projetos de sustentabilidade")

# Exercício
# Neste exercício, você deve criar um dicionário chamado politicaspb contendo políticas de desenvolvimento para o estado da Paraíba. Para cada política no dicionário, imprima o nome da política e sua descrição usando um loop for.

politicaspb = {'Educação': 'Investimento em educação básica', 'Saúde': 'Ampliação de hospitais'}
for politica, descricao in politicaspb.items():
    print(politica, ':', descricao)
    
#Exercício
#Neste exercício, você deve criar uma lista chamada investimentos contendo valores de investimentos em milhões de reais para a região Nordeste. Utilizando uma estrutura de controle for, calcule e imprima o total dos investimentos.

# Crie uma lista chamada 'investimentos' e calcule e imprima o total dos investimentos usando uma estrutura de controle 'for'.

investimentos = [100, 200, 150]
total = 0
for valor in investimentos:
    total = total + valor
print(total)

# Exercício
# Crie uma lista projetos contendo nomes de projetos de desenvolvimento para a região Amazônica. Use um loop for para imprimir o nome de cada projeto acrescido da frase ": Projeto Importante".

# Crie uma lista chamada 'projetos' e imprima o nome de cada projeto acrescido da frase ": Projeto Importante".

projetos = ['Saneamento Básico', 'Preservação Ambiental', 'Apoio aos Ribeirinhos']
for proj in projetos:
    print(f"{proj}, projeto importante")
    
# Exercício
# Neste exercício, crie uma lista estados_ne contendo nomes de alguns estados do Nordeste. Utilize uma estrutura de controle for para imprimir cada estado e informar que ele pertence à região Nordeste.

estados_ne = ['Bahia', 'Ceará']
for estado in estados_ne:
    print(estado, "pertence à região Nordeste")