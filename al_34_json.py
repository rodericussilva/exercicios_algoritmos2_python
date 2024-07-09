# Aula 34 - Json 1
# Agenda
# O que é o formato Json?
# Manipular dados no formato Json
# Via API
# Via arquivos
# Realizar análise de dados no formato Json
# O que é uma API?
# Uma API, que significa "Interface de Programação de Aplicações" (do inglês "Application Programming Interface"), é um conjunto de regras e definições que permite que programas de software se comuniquem entre si. Ela funciona como uma interface entre diferentes softwares, possibilitando a interação deles sem a necessidade de que um conheça os detalhes internos do outro.

# Na prática teremos aceso a um 'end point' ou endereço de internet/intranet que poderemos acessar os dados ou gravar dados.

# APIs na internet:

# Google Maps API: Permite incorporar mapas em websites e aplicativos, realizar buscas de localização e até mesmo traçar rotas.
# Twitter API: Usada para acessar e interagir com tweets, contas de usuário, seguir novas contas, e postar tweets através de programas.
# Amazon S3 API: Permite armazenar e recuperar grandes quantidades de dados em servidores da Amazon de forma programática.
# APIs na intranet da organizaçao:

# Cadastro funcional de empregados
# Vendas para um cliente
# Cadastro de fornecedores
# Qual o formato dos dados Provenientes de uma API
# Existem diversos formatos para transporte de dados na internet.Seguem alguns:

# JSON (JavaScript Object Notation) é um formato de dados leve baseado em texto que é usado para a serialização de dados. É fácil de ler e escrever para humanos e simples de analisar e gerar para máquinas. JSON é derivado da notação de objeto do JavaScript, mas desde então foi adotado como um formato de troca de dados independente de linguagem, sendo suportado nativamente por muitas linguagens de programação.

# XML (eXtensible Markup Language): Antes do JSON se tornar popular, o XML era o formato predominante para a troca de dados. Ele ainda é usado em muitos sistemas, especialmente aqueles que requerem um esquema rigoroso ou que foram desenvolvidos antes do JSON se tornar popular.

# YAML (YAML Ain't Markup Language): É outro formato que é usado principalmente em arquivos de configuração devido à sua legibilidade. É menos verboso que o XML e, em muitos casos, considerado mais legível que o JSON.

# CSV (Comma-Separated Values): Embora menos comum para APIs, o CSV é usado para dados tabulares e é frequentemente utilizado para exportar e importar dados para planilhas e sistemas de banco de dados.

# Binary Data: Para transferência de imagens, arquivos de mídia ou outros tipos de dados binários, as APIs podem trafegar dados em formatos binários puros, muitas vezes como streams de bytes.

# Acessando as APIs do IBGE
# https://servicodados.ibge.gov.br/api/docs/

# API Nomes https://servicodados.ibge.gov.br/api/docs/nomes?versao=2#api-_

# Verificar a documentação da API Nomes do IBGE

# Frequência por nome
# Ranking por frequência
# Acessando as APIs do IBGE pelo navegador e pelo JSONViwer
# Use o serviço de visualização de JSON abaixo:
# https://jsonviewer.stack.hu/

# -Acesse a série histórica com frequência para o nome ANA:

# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana

# -Acesse a série histórica com frequência de nomes para o sexo masculino:

# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M

# (Agora é a sua vez...) Acessando as APIs de CEP e Conversão de moedas pelo navegador e pelo JSONViwer
# Acessando informações de CEP
# https://viacep.com.br/

# https://viacep.com.br/ws/CE/fortaleza/pontes+vieira/json

# API de Cotações de Moedas
# https://docs.awesomeapi.com.br/api-de-moedas

# https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL

# Acessando dados da API Json pelo Python
# Considere o endereço internet de API do IBGE para acessar a frequência do nome 'ANA'.

# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana

# Elabore um programa python que acesse os dados em json e os imprima na tela no formato json.

import requests

#usar json para visualizar pois retorna uma string viwer https://jsonviewer.stack.hu/

# URL da API
link = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana"

# Realizando a solicitação GET à API
response = requests.get(link)

# Acessando o conteúdo JSON puro como uma string
json_puro = response.text

# Imprimindo o JSON puro
print(json_puro)

#variavel json puro é do tipo string se for manipular pe mais dificil para extrair valores de dentro

type (json_puro)

#(Agora é a sua vez ... ) Exercício: Acesso de dados de API JSON pelo Python
#Considere o endereço internet de API do IBGE para acessar a série histórica de frequência de nomes do sexo masculino.

# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M

#Elabore um programa python que acesse os dados em json e os imprima na tela no formato json.

import requests

link = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana"
response = requests.get(link)
json_puro = response.text

print(json_puro)


# O que é JSON (JavaScript Object Notation)?
# Descrição: JSON é um formato de dados leve baseado em texto que é usado para a serialização de dados. É fácil de ler e escrever para humanos e simples de analisar e gerar para máquinas. JSON é derivado da notação de objeto do JavaScript, mas desde então foi adotado como um formato de troca de dados independente de linguagem, sendo suportado nativamente por muitas linguagens de programação.
# A documentação sobre o formato Json pode ser acessada em https://ecma-international.org/publications-and-standards/standards/ecma-404/ e https://www.json.org/json-pt.html (tem versão em português).

# Estrutura:

# JSON é composto por dois tipos de estruturas:

# Coleções de pares nome/valor (ou "objetos" em JavaScript), que no Python são representados como dicionários (dict).
# Listas ordenadas de valores (ou "arrays" em JavaScript), que são representados como listas (list) em Python.
# Os valores podem ser strings, números, objetos JSON, arrays, true, false, ou null.

# Exemplo de coleção de pares objeto/valor:

#Use visualizador Json https://jsonviewer.stack.hu/

{
 "nome": "João",
 "idade": 30,
 "professor": true,
 "cursos": ["Python", "JavaScript"]
}
#Exemplo de listas JSON:

[
 "Funcionários",
 {
   "nome": "João",
   "idade": 30
 },
 {
   "nome": "Maria",
   "idade": 25
 }
]
# Uso Comum:

# APIs web: JSON é extremamente popular em APIs RESTful e outras APIs web devido à sua fácil interoperabilidade com JavaScript e sua eficiência em termos de codificação.
# Configurações: Muitos softwares usam JSON para arquivos de configuração devido à sua clareza e simplicidade.
# Armazenamento de dados: Sistemas de banco de dados NoSQL, como MongoDB, usam JSON ou formatos semelhantes (como BSON) para armazenar dados.
# Vantagens:

# Legibilidade: JSON é muito legível e fácil de entender.
# Eficiência: Enquanto sendo baseado em texto, é relativamente compacto, o que o torna uma escolha eficiente para a troca de dados na web.
# Facilidade de Uso: Existem bibliotecas disponíveis para analisar e gerar JSON em praticamente todas as linguagens de programação modernas.
# Desvantagens:

# Limitação de Tipos de Dados: Não suporta tipos mais complexos como datas, que precisam ser convertidas para strings ou outros formatos.
# Verbosidade: Para alguns tipos de dados ou aplicações, JSON pode ser mais verboso do que outros formatos binários, como Protocol Buffers.
# Json e Python Comparação
# A comparação entre objetos JSON e estruturas de dados em Python é interessante porque, apesar de haver similaridades, há diferenças importantes que devem ser consideradas, especialmente quando se trata de conversões entre os dois formatos.

# Similaridades
# Estruturas Aninhadas: Tanto objetos JSON quanto estruturas de dados em Python suportam aninhamentos, o que permite a construção de dados complexos e hierárquicos.

# Tipos de Dados Compatíveis:

# Objetos JSON correspondem a dicionários em Python (dict), usando um conjunto de pares chave-valor.
# Arrays JSON são similares às listas em Python (list), representando uma coleção ordenada de elementos.
# Strings, números, booleanos (true/false em JSON e True/False em Python) e null (em JSON) versus None (em Python) são diretamente mapeáveis entre os dois formatos. No que se refere à strings em JSON são coleção de caractereres delimitados por aspas duplas.
# obs: Para usar aspas duplas dentro da string é preciso inserir antes o caractere de escape que é a barra invertida\.

#      {
#      "frase": "Este é um exemplo de string com \"aspas duplas\" internas"
#      }
# Diferenças
# Tipagem:

# JSON é tipado de forma mais simples e menos estrita comparado a Python. Por exemplo, JSON não faz distinção entre tipos de números (todos são considerados como números, sem diferenciação explícita entre inteiros e floats).
# Python possui uma variedade muito maior de tipos (como int, float, tuple, set etc.) que não são representados diretamente em JSON.
# Uso de Funções e Métodos:

# Objetos JSON são puramente dados; eles não incluem funções ou métodos.
# Estruturas de dados Python podem ter métodos associados (por exemplo, métodos de lista como .append(), .remove()) e podem incluir objetos mais complexos que contêm métodos.
# Converter dados da API JSON em variáves tipo lista ou dicionário em Python
# Considere os dados no formato JSON abaixo provenientes da API de nomes do IBGE que lista a série histórica de frequência de uso do nome 'ANA'.

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
# Elabore um programa python que acesse os dados em json acima provenientes da internet e converta-o para variável no formato python tipo lista ou string. Imprima o resultado final da variável convertida.
import requests
import pprint


#nome = input("Digite o nome para consultar: ")
link = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana"

#acessa os dados da API Json
requicicao = requests.get(link)

#Realiza a conversão de json para variável em python
dados_nome = requicicao.json()

print (type(dados_nome))

pprint.pprint (dados_nome)


# (Agora é a sua vez ...) Exercício: Converter dados da API JSON em variáves lista ou dicionário em Python
# Considere o endereço internet de API do IBGE para acessar a série histórica de frequência de nomes do sexo masculino.

#https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M

[
    {
        "localidade": "BR",
        "res": [
            {"frequencia": 5732508, "nome": "JOSE", "ranking": 1},
            {"frequencia": 2971935, "nome": "JOAO", "ranking": 2},
            {"frequencia": 2567494, "nome": "ANTONIO", "ranking": 3},
            {"frequencia": 1765197, "nome": "FRANCISCO", "ranking": 4},
            {"frequencia": 1483121, "nome": "CARLOS", "ranking": 5},
            {"frequencia": 1417907, "nome": "PAULO", "ranking": 6},
            {"frequencia": 1213557, "nome": "PEDRO", "ranking": 7},
            {"frequencia": 1116818, "nome": "LUCAS", "ranking": 8},
            {"frequencia": 1102927, "nome": "LUIZ", "ranking": 9},
            {"frequencia": 1101126, "nome": "MARCOS", "ranking": 10},
            {"frequencia": 931530, "nome": "LUIS", "ranking": 11},
            {"frequencia": 922744, "nome": "GABRIEL", "ranking": 12},
            {"frequencia": 814709, "nome": "RAFAEL", "ranking": 13},
            {"frequencia": 706527, "nome": "DANIEL", "ranking": 14},
            {"frequencia": 690098, "nome": "MARCELO", "ranking": 15},
            {"frequencia": 663271, "nome": "BRUNO", "ranking": 16},
            {"frequencia": 628539, "nome": "EDUARDO", "ranking": 17},
            {"frequencia": 615924, "nome": "FELIPE", "ranking": 18},
            {"frequencia": 611174, "nome": "RAIMUNDO", "ranking": 19},
            {"frequencia": 598825, "nome": "RODRIGO", "ranking": 20}
        ],
        "sexo": "M"
    }
]
# Elabore um programa python que acesse os dados em json acima na internet e converta-os para variáveis no formato python tipo lista ou string. Imprima o resultado final da variável convertida.

import requests
import pprint

url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M'
req = requests.get(url)
dados = req.json()
pprint.pprint(dados)

# Manipulando dados provenientes de API JSON.
# Considere os dados no formato JSON abaixo provenientes da API de nomes do IBGE que lista a série histórica de frequência de uso do nome 'ANA'.

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
# Elabore um programa python que acesse os dados em json acima provenientes da internet, converta-o para variável no formato python tipo lista ou string. Finalmente, calcule a média das frequências e imprima os resultados conforme abaixo.

# Nome: ANA
# Período: 1930, Frequência: 33395
# Período: 1930-1940, Frequência: 56160
# Período: 1940-1950, Frequência: 101259
# Período: 1950-1960, Frequência: 183941
# Período: 1960-1970, Frequência: 292835
# Período: 1970-1980, Frequência: 421531
# Período: 1980-1990, Frequência: 529266
# Período: 1990-2000, Frequência: 536302
# Período: 2000-2010, Frequência: 935169
# Média: 343317.56

import requests

# URL da API que contém os dados JSON
url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana"

# Fazendo a solicitação para a API e convertendo a resposta para JSON
response = requests.get(url)
dados = response.json()

# Variável para armazenar a soma das frequências e calcular a média
soma_frequencias = 0

# Imprimindo os detalhes
print(f"Nome: {dados[0]['nome']}")
for registro in dados[0]['res']:
    periodo = registro['periodo'].replace('[', '').replace(']','').replace(',','-')
    frequencia = registro['frequencia']
    print(f"Período: {periodo}, Frequência: {frequencia}")
    soma_frequencias += frequencia

# Calculando a média das frequências
media = soma_frequencias / len(dados[0]['res'])

# Imprimindo a média
print(f"Média: {media:.2f}")


# (Agora é a sua vez...) Exercício: Manipulando dados provenientes de API JSON.
# Considere o endereço internet de API do IBGE para acessar a série histórica de frequência de nomes do sexo masculino.

#https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M

[
    {
        "localidade": "BR",
        "res": [
            {"frequencia": 5732508, "nome": "JOSE", "ranking": 1},
            {"frequencia": 2971935, "nome": "JOAO", "ranking": 2},
            {"frequencia": 2567494, "nome": "ANTONIO", "ranking": 3},
            {"frequencia": 1765197, "nome": "FRANCISCO", "ranking": 4},
            {"frequencia": 1483121, "nome": "CARLOS", "ranking": 5},
            {"frequencia": 1417907, "nome": "PAULO", "ranking": 6},
            {"frequencia": 1213557, "nome": "PEDRO", "ranking": 7},
            {"frequencia": 1116818, "nome": "LUCAS", "ranking": 8},
            {"frequencia": 1102927, "nome": "LUIZ", "ranking": 9},
            {"frequencia": 1101126, "nome": "MARCOS", "ranking": 10},
            {"frequencia": 931530, "nome": "LUIS", "ranking": 11},
            {"frequencia": 922744, "nome": "GABRIEL", "ranking": 12},
            {"frequencia": 814709, "nome": "RAFAEL", "ranking": 13},
            {"frequencia": 706527, "nome": "DANIEL", "ranking": 14},
            {"frequencia": 690098, "nome": "MARCELO", "ranking": 15},
            {"frequencia": 663271, "nome": "BRUNO", "ranking": 16},
            {"frequencia": 628539, "nome": "EDUARDO", "ranking": 17},
            {"frequencia": 615924, "nome": "FELIPE", "ranking": 18},
            {"frequencia": 611174, "nome": "RAIMUNDO", "ranking": 19},
            {"frequencia": 598825, "nome": "RODRIGO", "ranking": 20}
        ],
        "sexo": "M"
    }
]
# Elabore um programa python que acesse os dados em json acima provenientes da internet, converta-o para variável no formato python tipo lista ou string. Finalmente, liste apenas os dados dos rankings pares conforme abaixo:

# Nomes com ranking par:
{'nome': 'JOAO', 'frequencia': 2971935, 'ranking': 2}
{'nome': 'FRANCISCO', 'frequencia': 1765197, 'ranking': 4}
{'nome': 'PAULO', 'frequencia': 1417907, 'ranking': 6}
{'nome': 'LUCAS', 'frequencia': 1116818, 'ranking': 8}
{'nome': 'MARCOS', 'frequencia': 1101126, 'ranking': 10}
{'nome': 'GABRIEL', 'frequencia': 922744, 'ranking': 12}
{'nome': 'DANIEL', 'frequencia': 706527, 'ranking': 14}
{'nome': 'BRUNO', 'frequencia': 663271, 'ranking': 16}
{'nome': 'FELIPE', 'frequencia': 615924, 'ranking': 18}
{'nome': 'RODRIGO', 'frequencia': 598825, 'ranking': 20}


import requests

url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M'
req = requests.get(url)
dados = req.json()

print("Nomes com ranking par:")

for info in dados[0]['res']:
    if info % 2 == 0:
        print(info)