# Aula 35 - Json 2
# Agenda
# O que é o formato Json?
# Manipular dados no formato Json
# Via API
# Via arquivos (*)
# Realizar análise de dados no formato Json
# Manipulando arquivos no formato Json em Python
# Função Open nativa do Python
# Em Python, você pode abrir, escrever (ou gravar), e fechar arquivos usando função open() para ler, gravar e alterar aquivos com python nos formatos txt, csv, json, binário, json, etc.

# Sintaxe da função open():

# file_object = open(file_name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# Modos de abertura do arquivo (há outros)

# https://docs.python.org/3/library/functions.html#open

# 'r': Modo de leitura (o padrão se o modo não for especificado).

# 'w': Modo de escrita (cria um novo arquivo ou sobrescreve um existente).

# 'a': Modo de acréscimo (escreve dados no final do arquivo sem apagar o conteúdo existente).

# Biblioteca JSON
# Além da biblioteca requests que vimos anteriormente, a biblioteca jsontambém manipula dados no formato JSON.

# Principais Funcionalidades da Biblioteca json
# Serialização (Encoding): Converte objetos Python em uma string JSON.
# Deserialização (Decoding): Converte uma string JSON de volta em um objeto Python.
# json.dump
# A função json.dump é usada para serializar objetos Python para um arquivo em formato JSON. Ou seja, ela escreve o JSON diretamente em um arquivo.

# Sintaxe
# json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False)
# json.load
# A função json.load é usada para deserializar um arquivo contendo dados no formato JSON para um objeto Python.

# Sintaxe
# json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
# Inserindo dados no formato JSON em arquivos
# Utilize o parâmetro w da função open() para habilitar o modo de escrita (cria um novo arquivo ou sobrescreve um existente de mesmo nome)

# Lendo a API da web e gravando arquivo

import requests
import json

# URL da API
#link = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana"
link = "https://viacep.com.br/ws/CE/fortaleza/pontes+vieira/json"


# Realizando a solicitação GET à API
requisicao = requests.get(link)
dados_nome = requisicao.json()
type(dados_nome)
# Gravando a variável diretamente no arquivo
with open('dados_api.json', 'w') as arquivo:
    json.dump(dados_nome, arquivo, indent=4)

print("Os dados da API foram salvos com sucesso no arquivo ")

type(dados_nome)


# Gravando variável da memória para um arquivo json

import json

# Suponha que esta seja a variável que você deseja gravar em um arquivo JSON
dados = {
    'nome': 'Alice',
    'idade': None,
    'cidade': 'São "Paulo"',
    'hobbies': ['leitura', 'caminhada', 'música']
}


# Abrindo o arquivo para escrita
with open('dados2.json', 'w') as arquivo:
    # Usando json.dump para converter o dicionário em JSON e gravar no arquivo
    # ensure_ascii=False permite que caracteres Unicode sejam escritos diretamente
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Os dados foram salvos com sucesso no arquivo")

# (Agora é a sua vez...) Inserindo dados no formato JSON em arquivos
# Considere o endereço internet de API de cotação de moeda.

#https://economia.awesomeapi.com.br/json/daily/USD-BRL/15

# [
#     {
#         varBid: "-0.0143",
#         code: "USD",
#         codein: "BRL",
#         name: "Dólar Americano/Real Brasileiro",
#         high: "3.8906",
#         low: "3.8596",
#         pctChange: "-0.37",
#         bid: "3.8659",
#         ask: "3.8671",
#         timestamp: "1555360543",
#         create_date: "2019-04-15 17:35:43"
#     },
#     {
#         varBid: "0.0006",
#         high: "3.9076",
#         low: "3.8571",
#         pctChange: "0.02",
#         bid: "3.8808",
#         ask: "3.8829",
#         timestamp: "1555275600"
#     },
#     {
#         varBid: "0.0248",
#         high: "3.9076",
#         low: "3.8571",
#         pctChange: "0.64",
#         bid: "3.8813",
#         ask: "3.8823",
#         timestamp: "1555102794"
#     }
# Elabore um programa python que acesse os dados em json acima provenientes da internet, converta-o para variável no formato python tipo lista ou string. Finalmente, grave o arquivo no formato JSON chamado dados_moeda_api.json.

# Vamos usar este arquivo no exrcício seguinte.

import requests
import json

url = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/15'
req = requests.get(url)
dados = req.json()

with open('dados_api.json', 'w') as arquivo:
  json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print("Dados gravados")


# Lendo Arquivos no formato JSON
# Utilize o parâmetro r da função open() para habilitar o modo de leitura.

# Use a função read() para ler todas as linhas de uma só vez e as inserir na memória. Imprima o conteudo do arquivo lido.

# Ler json do arquivo e transforma e variável do python na memória

import json
import pprint

# Lendo os dados do arquivo
with open('dados_api.json', 'r') as arquivo:
    dados = json.load(arquivo)

print (type (dados))
pprint.pprint (dados)

# (Agora é a sua vez...) Lendo dados no formato JSON em arquivos
# Considere os dados da API de Cotação de Moedas. No exercício anterior foi gravado o arquivo dados_moeda_api.json a partir do acesso da API.

# obs:Vamos posteriormente usar este aquivo no exercício seguinte.

# Elabore um programa python que acesse os dados do arquivo json 'dados_moeda_api.json' e imprima o seu conteúdo na tela.

import json
import pprint

with open('dados_api.json', 'r') as arquivo:
  dados = json.load(arquivo)

pprint.pprint(dados)


# Modificar e Salvar arquivos no formato JSON
# Objetivo: Familiarizar-se com a leitura, alteração e escrita de arquivos JSON, mostrando como modificar dados e salvá-los de volta em um arquivo.

# Descrição:

# Passo 1: gravar um arquivo de configurações chamdo config.json. Utilize o dicionário python abaixo para gerar o aquivo de configurações.
# Passo 2: ler o arquivo de configurações gerado no passo anterior e alterar a informação de tamanho de 70 para 50.
# Passo 3: gravar novamente o arquivo com os valores alterados.
# Conteúdo do Arquivo config.json:

{
    "resolucao": "1920x1080",
    "tamanho": 70,
    "notificacoes": True
}
#Passo 1: Gravar o arquivo de configurações config.json

import json

# Dados de configuração inicial
configuracoes = {
    "resolucao": "1920x1080",
    "tamanho": 70,
    "notificacoes": True
}

# Gravando os dados no arquivo config.json
with open('config.json', 'w') as arquivo:
    json.dump(configuracoes, arquivo, indent=4)

print("Arquivo config.json criado com sucesso.")

#Passo 2: Ler o arquivo config.json e alterar a informação de tamanho

# Lendo o arquivo de configurações
with open('config.json', 'r') as arquivo:
    configuracoes = json.load(arquivo)

# Alterando o tamanho de 70 para 50
configuracoes['tamanho'] = 50

print("Configuração de tamanho alterada para 50.")
#Passo 3: Gravar novamente o arquivo config.json com os valores alterados

# Gravando as configurações atualizadas no arquivo config.json
with open('config.json', 'w') as arquivo:
    json.dump(configuracoes, arquivo, indent=4)

print("As configurações atualizadas foram gravadas com sucesso em config.json.")

# Explicação Completa do Processo
# Criação do Arquivo: No primeiro bloco, criamos o arquivo config.json com as configurações iniciais, usando json.dump() para converter o dicionário Python em uma string JSON formatada.

# Leitura e Modificação: No segundo bloco, lemos o arquivo usando json.load(), que converte a string JSON de volta para um dicionário Python. Então, modificamos o valor da chave tamanho de 70 para 50.

# Regravação do Arquivo: No terceiro bloco, gravamos o dicionário modificado de volta no mesmo arquivo, atualizando-o com as novas configurações.

# Este processo garante que o arquivo config.json seja criado, modificado e atualizado de forma simples e eficiente, demonstrando uma maneira prática de manipular arquivos de configurações em JSON com Python.