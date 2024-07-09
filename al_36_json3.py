# Aula 36 - Json 3
# Agenda
# O que é o formato Json?
# Manipular dados no formato Json
# Via API
# Via arquivos
# Realizar análise de dados no formato Json (*)
# Analisando dados no formato Json
# Exercício 1:
# Considere os dados no formato JSON abaixo provenientes da API de nomes do IBGE para mostrar a série histórica de frequência de uso do nome 'ANA'.

#https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana

[
    {
        "nome": "ANA",
        "sexo": null,
        "localidade": "BR",
        "res": [
            {"periodo": "1930[", "frequencia": 33395},
            {"periodo": "[1930,1940[", "frequencia": 56160},
            {"periodo": "[1940,1950[", "frequencia": 101259},
            {"periodo": "[1950,1960[", "frequencia": 183941},
            {"periodo": "[1960,1970[", "frequencia": 292835},
            {"periodo": "[1970,1980[", "frequencia": 421531},
            {"periodo": "[1980,1990[", "frequencia": 529266},
            {"periodo": "[1990,2000[", "frequencia": 536302},
            {"periodo": "[2000,2010[", "frequencia": 935169}
        ]
    }
]
# Desenvolva um programa Python que calcula a frequência média. Utilize a instrução for no algoritmo para varrer a estrutura de dados. Imprima a saída no formato abaixo:

# Nome: ANA, Frequência Média: xxx

import requests

# URL da API do IBGE para o nome "ANA"
url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana"

# Fazer a requisição para a API
response = requests.get(url)

dados_json = response.json()

# Cálculo da frequência média
total_frequencia = 0
contador = 0

# Varrendo os dados para calcular a soma das frequências e contar os períodos
for registro in dados_json[0]['res']:
      total_frequencia += registro["frequencia"]
      contador += 1

# Calculando a média
frequencia_media = total_frequencia / contador

# Formatar a saída conforme solicitado
print(f"Nome: {dados_json[0]['nome']}, Frequência Média: {frequencia_media}")


# Exercício 2:
# Agora, ainda utizando a API de nomes do exercício anterior, desenvolva um programa Python que calcule qual a maior frequência.

# Utilize a instrução for no algoritmo para varrer a estrutura de dados. Suponha que não necessariamente os dados estejam ordenados pela frequência. Imprima a saída no formato abaixo:

# Nome: ANA, Frequência maior : 935169 Período: [2000,2010[

import requests

# URL da API que contém os dados JSON
url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana"

# Fazendo a solicitação para a API e convertendo a resposta para JSON
response = requests.get(url)
dados = response.json()

# Inicializando variáveis para armazenar o período com a maior frequência
max_frequencia = 0
periodo_max = ''

# Iterando sobre os registros de frequência
for registro in dados[0]['res']:
    if registro['frequencia'] > max_frequencia:
        max_frequencia = registro['frequencia']
        periodo_max = registro['periodo']

# Imprimindo o resultado
print(f"Nome: ANA, Frequência maior : {max_frequencia} Período: {periodo_max}")

# (Agora é a sua vez...) Exercício: Analisando dados no formato JSON
# Considere os dados da API de Cotação de Moedas.

#https://economia.awesomeapi.com.br/json/daily/USD-BRL/15

# [
#     {
#         "code": "USD",
#         "codein": "BRL",
#         "name": "Dólar Americano/Real Brasileiro",
#         "high": "5.3886",
#         "low": "5.3152",
#         "varBid": "0.011",
#         "pctChange": "0.2",
#         "bid": "5.3555",
#         "ask": "5.356",
#         "timestamp": "1718046965",
#         "create_date": "2024-06-10 16:16:05"
#     },
#     {
#         "high": "5.354",
#         "low": "5.2416",
#         "varBid": "0.0092",
#         "pctChange": "0.17",
#         "bid": "5.353",
#         "ask": "5.355",
#         "timestamp": "1717957808"
#     },
#     {
#         "high": "5.3483",
#         "low": "5.2416",
#         "varBid": "0.0888",
#         "pctChange": "1.69",
#         "bid": "5.3436",
#         "ask": "5.3461",
#         "timestamp": "1717793996"
#     },
#     {
#         "high": "5.3483",
#         "low": "5.2416",
#         "varBid": "0.0881",
#         "pctChange": "1.68",
#         "bid": "5.3436",
#         "ask": "5.3446",
#         "timestamp": "1717793976"
#     },
#     {
#         "high": "5.2614",
#         "low": "5.255",
#         "varBid": "0.003",
#         "pctChange": "0.06",
#         "bid": "5.2585",
#         "ask": "5.2594",
#         "timestamp": "1717710765"
#     },
#     ... (continua)
# Elabore um programa python que acesse os dados da API e calcule qual foi o maior valor de bid. Utilize a estrutura de controle forpara varrer a estrutura de dados.

# bid: O preço pelo qual a moeda é comprada (o quanto se paga em reais para comprar um dólar).

# Imprima a saída no formato abaixo:

# O maior valor de bid é: 5.3545

url = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/15'
req = requests.get(url)
dados = req.json()

maior = float('-inf')

for info in dados:
  bid_atual = float(info['bid'])
  if bid_atual > maior:
    maior = bid_atual

print(f'O maior valor de bid é: {maior}')
