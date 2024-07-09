# Aula 37 - Exercício manipulação de dados JSON
# Exercício:
# Neste exercício você irá praticar todos os conceitos até então vistos sobre a manipulação de dados no formato JSON.

# Você deverá selecionar dentres as APIs de dados abertos do Banco Central aquela que mais lhe interessar e deverá realizar os passos abaixo identificados para extrair e analisas dados de seu interesse.

# Depois de completar os passos abaixo identificados copie suas respostas para dentro da ferramenta Miro de compartihamento, cujo endereço está abaixo identificado:

# https://miro.com/app/board/uXjVK89Jo08=/?share_link_id=772524564188
# Passo 1: Selecionar um assunto de seu interesse
# Explore as APIs de dados abertos do Banco Central

# https://dadosabertos.bcb.gov.br/
# Selecione um assunto que lhe interessa conhecer mais dados específico dentre os assuntos da coluna de dados populares.
# informe aqui o assunto que você se interessou em extrair dados para analisar:

# Índice de Atividade Econômica do Banco Central - IBC-Br

# É um indicador mensal contemporâneo da atividade econômica nacional.


# Passo 2: Gerar/Acessar a URL do Endpoint JSON
# Gerar a URL de consulta específica no formato Json ao endpoint dos dados abertos do Banco Central.
# Insira aqui a URL:

#https://api.bcb.gov.br/dados/serie/bcdata.sgs.24363/dados?formato=json


# Passo 3:Programa para acessar o Endpoint
# Desenvolver um programa em python que vai acessar os dados da URL acima e imprimir os dados na tela
## Insira o programa aqui:

import requests
import json
import pprint

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.24363/dados?formato=json"

dados_api = requests.get(url)
dados = dados_api.json()

pprint.pprint(dados)


# Passo 4: Programa que grava em um arquivo no formato Json
# Desenvolver um programa em Python que vai gravar os dados em um arquivo no formato JSON
 ## Insira o programa aqui:
 
import requests
import json
import pprint

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.24363/dados?formato=json"

dados_api = requests.get(url)
dados = dados_api.json()

with open('ind_ativ_economica.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)
    
    
    
# Passo 5: Programa que gera um relatório dos dados
# A partir da leitura do arquivo em Json anteriormente gravado no passo anterior, desenvolver um programa em Python que vai gerar um relatório na tela dos dados acessados na API no seguinte formato abaixo:

# uma linha no relatório para cada conjunto de informações geradas.

# Relatório do assunto xyz
# -------------------
# dado_1: x1  dado_2: x2 dado_3:x3
# dado_1: y1  dado_2: y2 Dado_3:y3
# ...
## Insira o programa aqui:

import requests
import json

with open('ind_ativ_economica.json', 'r') as arquivo:
    dados = json.load(arquivo)

print("Relatório")
print("---------")

for registro in dados:
    print(f"Data: {registro['data']}  -   Valor: {registro['valor']}")
    
    
    
# Passo 6: Programa que analisa os dados
# A partir da leitura do arquivo em Json anteriormente gravado, desenvolver um programa em Python que vai gerar uma análise dos dados que você considere relevante para entender melhor a realidade revelada pelos dados acessados. Imprima na tela o resultado da análise.
# uma linha no relatório para cada conjunto de informações geradas.


import requests
import json
import pprint
import matplotlib.pyplot as plt

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.24363/dados?formato=json"

dados_api = requests.get(url)
dados = dados_api.json()
pprint.pprint (dados)
print('')

x, y = [], []
ano = dados[0]['data'][-4:]
total_ano = 0
meses_ano = 0

for registro in dados:
    if registro['data'][-4:] != ano:
        x.append(ano)
        y.append(round(total_ano / meses_ano, 2))
        ano = registro['data'][-4:]
        total_ano = 0
        meses_ano = 0
    total_ano += float(registro['valor'])
    meses_ano += 1
x.append(ano)
y.append(round(total_ano / meses_ano, 2))
print (x)
print (y)
print ('')

# Gráfico de Barras Verticais
plt.barh(x, y, align='center', height=0.6, alpha=0.5)
plt.title("Índice de Atividade Econômica", fontdict={'family': 'monospace', 'color': 'red', 'weight': 'bold', 'size': 16}, loc='left')
plt.xlabel('Valor (em bilhões de R$)')
plt.ylabel('Ano')
plt.show()