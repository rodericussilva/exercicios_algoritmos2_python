# Aula 8 - Exercícios em Sala de Aula

# Exercícios sobre estrutura de controle if, else, elif e match-case

# Exercício

# Verificar se uma usina hidrelétrica está funcionando acima da capacidade máxima. A variável energia_produzida armazena a quantidade de energia produzida em MWh e a variável capacidade_maxima armazena a capacidade máxima da usina em MWh. Utilizar uma estrutura if para imprimir se a usina está funcionando acima da capacidade máxima.

# Verifique se a usina hidrelétrica está funcionando acima da capacidade máxima
from nis import match
from unittest import case


energia_produzida = 1050
capacidade_maxima = 1000
if energia_produzida > capacidade_maxima:
    print("A usina está funcionando acima da capacidade máxima.")

# Exercício
# Neste exercício, você deve criar uma lista precos contendo preços de cinco produtos e verificar se o preço de algum produto é maior que 100 reais, se for, imprima "Produto caro".

precos = [50, 120, 80, 30, 110]
if max(precos) > 100:
    print("Produto caro")
    
# Exercício

# Verificar se é possível abastecer um veículo elétrico. A variável tipo_combustivel pode ser "eletrico" ou "gasolina". Se o tipo de combustível for elétrico, imprima "Pode abastecer". Caso contrário, imprimir "Não pode abastecer".

# Verifique se é possível abastecer um veículo elétrico
tipo_combustivel = "eletrico"
if tipo_combustivel == "gasolina":
    print("Pode abastecer.")
else:
    print("Não pode abastecer.")

# Exercício

# Neste exercício, você vai criar uma variável chamada estoque que será um dicionário contendo três produtos e suas respectivas quantidades. Você deve usar uma estrutura de controle if para verificar se a quantidade de um produto é menor que 5. Se for menor, imprima o nome do produto e a mensagem "Quantidade baixa".

estoque = {"ProdutoA": 4, "ProdutoB": 10, "ProdutoC": 3}

for produto, quantidade in estoque.items():
    if  quantidade > 5:
        print(f"{produto} - Quantidade baixa")

# Exercício
# Neste exercício, crie uma variável produto contendo o nome de um produto e uma variável disponibilidade contendo um valor booleano. Use if e else para imprimir "Produto disponível" ou "Produto indisponível" baseado no valor da variável disponibilidade.

produto = "ProdutoX"
disponibilidade = False
if produto == disponibilidade:
 print("Produto disponível")
else:
  print("Produto indisponível")

# Exercício
# Uma organização ambiental quer classificar diferentes fontes de energia renovável com base em sua sustentabilidade. A sustentabilidade é avaliada em três níveis: "Sustentável", "Moderadamente Sustentável" e "Pouco Sustentável". Dado um dicionário contendo tipos de energia renovável e seus respectivos níveis de sustentabilidade, escreva um programa que agrupe e imprima os tipos de energia por categoria de sustentabilidade.

sustentabilidade_energia = {
    "solar": "Sustentável",
    "eólica": "Sustentável",
    "hidrelétrica": "Moderadamente Sustentável",
    "biomassa": "Pouco Sustentável",
    "geotérmica": "Sustentável"
}

for tipo, sustentabilidade in sustentabilidade_energia.items():
    match sustentabilidade:
        case "Sustentável":
            print(f"A energia {tipo} é classificada como Sustentável.")
        case "Moderadamente Sustentável":
            print(f"A energia {tipo} é classificada como Moderadamente Sustentável.")
        case "Pouco Sustentável":
            print(f"A energia {tipo} é classificada como Pouco Sustentável.")

# Exercício
# Um investidor está avaliando diferentes tipos de projetos de energia renovável. Cada tipo de projeto tem um nível de retorno esperado: "Alto", "Médio" ou "Baixo". Dado um dicionário com tipos de energia renovável como chaves e os níveis de retorno esperado como valores, escreva um programa que informe o investidor quais projetos são considerados investimentos viáveis, assumindo que apenas projetos com retorno "Alto" são viáveis.

projetos_energia = {
    "solar": "Alto",
    "eólica": "Médio",
    "hidrelétrica": "Baixo",
    "biomassa": "Alto",
    "geotérmica": "Médio"
}

for tipo, retorno in projetos_energia.items():
    match retorno:
        case "Alto":
            print(f"O projeto de energia {tipo} é considerado um investimento viável.")
        case "baixo":
            print(f"O projeto de energia {tipo} não é considerado um investimento viável.")

# Exercício
# Dada uma lista de temperaturas médias anuais em diferentes locais, determinar se um local é adequado para a instalação de sistemas de energia geotérmica. Se a temperatura média anual estiver acima de 15°C, considera-se viável; caso contrário, considera-se inviável.

temperaturas = [12, 14, 16, 18, 20, 22, 19, 17, 15, 13, 11, 10]
viabilidade_geotermica = "Viável" if max(temperaturas) > 15 else "Inviável"
print(viabilidade_geotermica)

# Exercício
# Dada uma lista de emissões de CO2 (em toneladas por ano) de várias usinas, classifique cada usina em "Baixo", "Médio" ou "Alto" impacto de emissão de CO2. Use os seguintes critérios: Baixo (menos de 1000 toneladas/ano), Médio (entre 1000 e 5000 toneladas/ano), Alto (mais de 5000 toneladas/ano).

# Obs: use if, elif e else na construção do código

emissoes_co2 = [800, 1200, 500, 6000, 4500]

for emissao in emissoes_co2:
  if emissao > 5000:
   print("Alto")
  elif emissao >= 1000 and emissao <= 5000:
   print("Médio")
  else:
   print("Baixo")

# Exercício
# Você está desenvolvendo um programa para calcular a eficiência energética de diferentes tipos de sistemas de energia renovável. Você tem os seguintes critérios de classificação:

# Se a eficiência estiver acima de 90%, é considerada "excelente".

# Se estiver entre 80% e 90%, é considerada "boa".

# Se estiver entre 70% e 80%, é considerada "razoável".

# Abaixo de 70%, é considerada "insatisfatória".

# Você recebe um dicionário contendo o tipo de sistema de energia renovável como chave e sua eficiência como valor. Escreva um programa Python que classifique cada sistema de energia de acordo com os critérios mencionados.

# Obs: use a estrutura match-case combinada com if

sistemas_energia = {
    "solar": 88,
    "eólica": 72,
    "hidrelétrica": 95,
    "biomassa": 65,
    "geotérmica": 82
}

for sistema, valeur in sistemas_energia.items():
    
    match valeur:
        case valeur if valeur > 90:
            result = "excelente"
            print(f"{sistema}: {result}")
        case valeur if 80 <= valeur <= 90:
            result = "boa"
            print(f"{sistema}: {result}")
        case valeur if 70 <= valeur < 80:
            result = "razoavel"
            print(f"{sistema}: {result}")


# Exercício
# Uma empresa de energia renovável deseja classificar a eficiência de suas turbinas eólicas baseada na quantidade de energia que cada uma produz em um dia. A eficiência é classificada em três categorias: "Alta", "Média" e "Baixa". A classificação depende do seguinte critério:

# "Alta" eficiência: turbinas que produzem mais de 200 MWh por dia.
# "Média" eficiência: turbinas que produzem entre 100 MWh e 200 MWh por dia.
# "Baixa" eficiência: turbinas que produzem menos de 100 MWh por dia.
# Você tem uma lista com a produção diária (em MWh) de várias turbinas e deve determinar quantas turbinas se enquadram em cada categoria de eficiência.

producao_diaria = [150, 230, 90, 180, 210, 95, 110, 205, 130, 160]
eficiencia = {"Alta": 0, "Média": 0, "Baixa": 0}

for producao in producao_diaria:
    if producao > 200:
        eficiencia["Alta"] += 1
    elif 100 <= producao <= 200:
        eficiencia["Média"] += 1
    else:
        eficiencia["Baixa"] += 1
        
for categoria, quantidade in eficiencia.items():
    print(f"{categoria}: {quantidade}")