# Aula 38 - Json Exercícios
# Agenda
# Visão geral das Aulas Json
# Resumo dos Enpoints a serem focados
# Nomes, cep, moeda
# Resumo das estruturas de loops for para as APIs acima
# Tipos de questões:
# Exercícios leitura de dados de APIs Json na WEB

# Exercícios leitura/gravação de dados de APIs Json em arquivos

# Exercícios de análise de dados da API Json

# base dos exercícios é saber fazer loop nessas estruturas de dados resulstantes das APIs

# Imprimir dados
# Selecionar dados específicos
# Contar elementos
# Acumular elementos
# Calcular: média, percentuais, etc
# Usando apenas uma variável de entrada
# Usando mais de uma variável de entrada relacionadas
# Armazenando resultado do cálculo em variáveis temporárias para uso posterior
# Selecionar maior elemento
# Selecionar menor elemento
# Ordenar
# Incluir, Excluir, Alterar e Deletar elementos
# etc
# Relação de APIs e endpoints a serem considerados no exercícios:
# Api Nome
# Página de descrição:
# https://servicodados.ibge.gov.br/api/docs/nomes?versao=2#api-_
# Endpoints:
# Frequência por nome
# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana
# Ranking por frequência
# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M
# API CEP
# Página de descrição:
# https://viacep.com.br/
# Endpoint: Relação de CEPs por localização
# https://viacep.com.br/ws/CE/fortaleza/pontes+vieira/json
# API de Moeda
# Página de descrição:
# https://docs.awesomeapi.com.br/api-de-moedas
# Endpoint: Cotação de fechamento diária de uma moeda em relação a outra
# https://economia.awesomeapi.com.br/json/daily/USD-BRL/7
# Detalhamento das APIs
# API Nomes
# https://servicodados.ibge.gov.br/api/docs/nomes?versao=2#api-_
# 1- Frequência por nome
# Obtém a frequência de nascimentos por década para o nome consultado
# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ana

[
  {
    "nome": "ANA",
    "sexo": null,
    "localidade": "BR",
    "res": [
      {
        "periodo": "1930[",
        "frequencia": 33395
      },
      {
        "periodo": "[1930,1940[",
        "frequencia": 56160
      },
      {
        "periodo": "[1940,1950[",
        "frequencia": 101259
      },
      {
        "periodo": "[1950,1960[",
        "frequencia": 183941
      },
      {
        "periodo": "[1960,1970[",
        "frequencia": 292835
      },
      {
        "periodo": "[1970,1980[",
        "frequencia": 421531
      },
      {
        "periodo": "[1980,1990[",
        "frequencia": 529266
      },
      {
        "periodo": "[1990,2000[",
        "frequencia": 536302
      },
      {
        "periodo": "[2000,2010[",
        "frequencia": 935169
      }
    ]
  }
]
#Estrutura de loop for

for registro in dados_nome[0]['res']:
      print (registro["frequencia"])
      
      
# 2- Ranking por frequência
# Obtém o ranking dos nomes segundo a frequência de nascimentos
# https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?sexo=M

[
  {
    "localidade": "BR",
    "sexo": "M",
    "res": [
      {
        "nome": "JOSE",
        "frequencia": 5732508,
        "ranking": 1
      },
      {
        "nome": "JOAO",
        "frequencia": 2971935,
        "ranking": 2
      },
      {
        "nome": "ANTONIO",
        "frequencia": 2567494,
        "ranking": 3
      },
      {
        "nome": "FRANCISCO",
        "frequencia": 1765197,
        "ranking": 4
      },
      {
        "nome": "CARLOS",
        "frequencia": 1483121,
        "ranking": 5
      },
      {
        "nome": "PAULO",
        "frequencia": 1417907,
        "ranking": 6
      },
      {
        "nome": "PEDRO",
        "frequencia": 1213557,
        "ranking": 7
      },
      {
        "nome": "LUCAS",
        "frequencia": 1116818,
        "ranking": 8
      },
      {
        "nome": "LUIZ",
        "frequencia": 1102927,
        "ranking": 9
      },
      {
        "nome": "MARCOS",
        "frequencia": 1101126,
        "ranking": 10
      },
      {
        "nome": "LUIS",
        "frequencia": 931530,
        "ranking": 11
      },
      {
        "nome": "GABRIEL",
        "frequencia": 922744,
        "ranking": 12
      },
      {
        "nome": "RAFAEL",
        "frequencia": 814709,
        "ranking": 13
      },
      {
        "nome": "DANIEL",
        "frequencia": 706527,
        "ranking": 14
      },
      {
        "nome": "MARCELO",
        "frequencia": 690098,
        "ranking": 15
      },
      {
        "nome": "BRUNO",
        "frequencia": 663271,
        "ranking": 16
      },
      {
        "nome": "EDUARDO",
        "frequencia": 628539,
        "ranking": 17
      },
      {
        "nome": "FELIPE",
        "frequencia": 615924,
        "ranking": 18
      },
      {
        "nome": "RAIMUNDO",
        "frequencia": 611174,
        "ranking": 19
      },
      {
        "nome": "RODRIGO",
        "frequencia": 598825,
        "ranking": 20
      }
    ]
  }
]
#Estrutura de loop for

for registro in dados_nome[0]['res']:
      print (registro["frequencia"])
      
      
# API CEP
# https://viacep.com.br/
# -Relação de CEPs por localização
# Para consultar a relação de CEPs de uma localização são necessários três parâmetros obrigatórios (UF, Cidade e Logradouro),

# https://viacep.com.br/ws/CE/fortaleza/pontes+vieira/json


[
  {
    "cep": "60135-238",
    "logradouro": "Avenida Pontes Vieira",
    "complemento": "de 1552 ao fim - lado par",
    "bairro": "Dionisio Torres",
    "localidade": "Fortaleza",
    "uf": "CE",
    "ibge": "2304400",
    "gia": "",
    "ddd": "85",
    "siafi": "1389"
  },
  {
    "cep": "60130-973",
    "logradouro": "Avenida Pontes Vieira",
    "complemento": "133",
    "bairro": "Joaquim Távora",
    "localidade": "Fortaleza",
    "uf": "CE",
    "ibge": "2304400",
    "gia": "",
    "ddd": "85",
    "siafi": "1389"
  },
  {
    "cep": "60130-959",
    "logradouro": "Avenida Pontes Vieira",
    "complemento": "722",
    "bairro": "Tauape",
    "localidade": "Fortaleza",
    "uf": "CE",
    "ibge": "2304400",
    "gia": "",
    "ddd": "85",
    "siafi": "1389"
  },
  {
    "cep": "60130-235",
    "logradouro": "Avenida Pontes Vieira",
    "complemento": "até 989 - lado ímpar",
    "bairro": "Joaquim Távora",
    "localidade": "Fortaleza",
    "uf": "CE",
    "ibge": "2304400",
    "gia": "",
    "ddd": "85",
    "siafi": "1389"
  },
  {
    "cep": "60130-971",
    "logradouro": "Avenida Pontes Vieira",
    "complemento": "722",
    "bairro": "Tauape",
    "localidade": "Fortaleza",
    "uf": "CE",
    "ibge": "2304400",
    "gia": "",
    "ddd": "85",
    "siafi": "1389"
  },
  {
    "cep": "60135-237",
    "logradouro": "Avenida Pontes Vieira",
    "complemento": "de 991 ao fim - lado ímpar",
    "bairro": "Dionisio Torres",
    "localidade": "Fortaleza",
    "uf": "CE",
    "ibge": "2304400",
    "gia": "",
    "ddd": "85",
    "siafi": "1389"
  },
  {
    "cep": "60130-240",
    "logradouro": "Avenida Pontes Vieira",
    "complemento": "até 1550 - lado par",
    "bairro": "Tauape",
    "localidade": "Fortaleza",
    "uf": "CE",
    "ibge": "2304400",
    "gia": "",
    "ddd": "85",
    "siafi": "1389"
  }
]

#Estrutura de loop for

for registro in dados_cep:
  print (registro['logadouro'])
  
  
# API Cotação de Moedas
# https://docs.awesomeapi.com.br/api-de-moedas
# -Posição defechamento dos últimos dias da contação de uma moeda em relação a outra.
# https://economia.awesomeapi.com.br/json/daily/USD-BRL/7

[
  {
    "code": "USD",
    "codein": "BRL",
    "name": "Dólar Americano/Real Brasileiro",
    "high": "5.3886",
    "low": "5.3152",
    "varBid": "0.0076",
    "pctChange": "0.14",
    "bid": "5.3522",
    "ask": "5.3527",
    "timestamp": "1718051963",
    "create_date": "2024-06-10 17:39:23"
  },
  {
    "high": "5.354",
    "low": "5.2416",
    "varBid": "0.0092",
    "pctChange": "0.17",
    "bid": "5.353",
    "ask": "5.355",
    "timestamp": "1717957808"
  },
  {
    "high": "5.3483",
    "low": "5.2416",
    "varBid": "0.0888",
    "pctChange": "1.69",
    "bid": "5.3436",
    "ask": "5.3461",
    "timestamp": "1717793996"
  },
  {
    "high": "5.3483",
    "low": "5.2416",
    "varBid": "0.0881",
    "pctChange": "1.68",
    "bid": "5.3436",
    "ask": "5.3446",
    "timestamp": "1717793976"
  },
  {
    "high": "5.2614",
    "low": "5.255",
    "varBid": "0.003",
    "pctChange": "0.06",
    "bid": "5.2585",
    "ask": "5.2594",
    "timestamp": "1717710765"
  },
  {
    "high": "5.3028",
    "low": "5.2966",
    "varBid": "0.0057",
    "pctChange": "0.11",
    "bid": "5.3016",
    "ask": "5.3026",
    "timestamp": "1717622967"
  },
  {
    "high": "5.2899",
    "low": "5.2857",
    "varBid": "0.003",
    "pctChange": "0.06",
    "bid": "5.2886",
    "ask": "5.2896",
    "timestamp": "1717536558"
  }
]

#Estrutura de loop for

for registro in dados_moeda:
    # Converter o valor de bid de string para float
    bid_atual = float(registro['bid'])
    print (bid_atua*0.1)
    
    
# Explicação dos campos da API - Cotação de Moedas
# Cada registro dentro da lista representa uma atualização ou um ponto específico no tempo relacionado à cotação do dólar americano em relação ao real brasileiro. Os campos principais como high, low, varBid, pctChange, bid, e ask fornecem uma visão detalhada das flutuações e tendências de preços ao longo do tempo.

# Interpretação dos Dados
# Variações Diárias: high e low mostram os extremos de negociação, indicando a volatilidade do câmbio.
# Mudanças Percentuais: pctChange oferece uma ideia rápida de como a moeda está se comportando em relação a períodos anteriores.
# Preços de Compra e Venda: bid e ask são cruciais para entender o spread, ou seja, a diferença entre o preço pelo qual se compra e se vende a moeda.
# Utilização Prática
# Essas informações são extremamente úteis para investidores e empresas que precisam monitorar as taxas de câmbio para tomada de decisão informada em transações financeiras internacionais, importação e exportação de produtos, entre outras atividades econômicas.

# Explicação dos Campos
# 1. code
# Descrição: Código da moeda base.
# Exemplo: "USD"
# Significado: Indica que a moeda base é o dólar americano.
# 2. codein
# Descrição: Código da moeda de conversão.
# Exemplo: "BRL"
# Significado: Indica que a moeda de conversão é o real brasileiro.
# 3. name
# Descrição: Nome da relação entre as moedas.
# Exemplo: "Dólar Americano/Real Brasileiro"
# Significado: Descreve a relação de câmbio entre o dólar americano e o real brasileiro.
# 4. high
# Descrição: Maior valor de negociação do dia.
# Exemplo: "5.3886"
# Significado: O preço mais alto alcançado pelo dólar americano em relação ao real brasileiro durante o período observado.
# 5. low
# Descrição: Menor valor de negociação do dia.
# Exemplo: "5.3152"
# Significado: O preço mais baixo alcançado pelo dólar americano em relação ao real brasileiro durante o período observado.
# 6. varBid
# Descrição: Variação do valor de compra.
# Exemplo: "0.0076"
# Significado: Diferença entre o valor de compra atual e o valor de compra anterior. Representa a variação do preço de compra.
# 7. pctChange
# Descrição: Percentual de mudança.
# Exemplo: "0.14"
# Significado: Percentual de variação no preço da moeda em relação ao período anterior. Indica a mudança percentual do valor de compra.
# 8. bid
# Descrição: Preço de compra.
# Exemplo: "5.3522"
# Significado: O preço pelo qual a moeda é comprada (o quanto se paga em reais para comprar um dólar).
# 9. ask
# Descrição: Preço de venda.
# Exemplo: "5.3527"
# Significado: O preço pelo qual a moeda é vendida (o quanto se recebe em reais ao vender um dólar).
# 10. timestamp
# Descrição: Carimbo de tempo em formato Unix.
# Exemplo: "1718051963"
# Significado: Representa o tempo exato em que a informação foi registrada, em segundos desde 1º de janeiro de 1970 (época Unix).
# 11. create_date
# Descrição: Data e hora da criação do registro.
# Exemplo: "2024-06-10 17:39:23"
# Significado: Data e hora em que o registro foi criado, no formato ano-mês-dia horas:minutos:segundos.
# Resumo das estrutura do loop for para as APIs a serem focadas
# API NOME
# Frequência por nome ou raking por frequência

for registro in dados_nome[0]['res']:
      print (registro["frequencia"])
      
#API CEP
for registro in dados_cep:
  print (registro['logadouro'])
  
#API MOEDA
for registro in dados_moeda:
    # Converter o valor de bid de string para float e verificar se é o maior
    bid_atual = float(registro['bid'])
    print (bid_atual*0.1)
    
# Tipos de questões:
# Exercícios leitura de dados de APIs Json na WEB

# Exercícios leitura/gravação de dados de APIs Json em arquivos

# Exercícios de análise de dados da API Json

# base dos exercícios é saber fazer loop nessas estruturas de dados resulstantes das APIs

# Imprimir dados
# Selecionar dados específicos
# Contar elementos
# Acumular elementos
# Calcular: média, percentuais, etc
# Usando apenas uma variável de entrada
# Usando mais de uma variável de entrada relacionadas
# Armazenando resultado do cálculo em variáveis temporárias para uso posterior
# Selecionar maior elemento
# Selecionar menor elemento
# Ordenar
# Incluir, Excluir, Alterar e Deletar elementos
# etc