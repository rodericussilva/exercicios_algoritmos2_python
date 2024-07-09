#Aula 4 - Exercícios em Sala de Aula
#4.1. - Exercícios sobre estrutura de controle if e else
#Exercício 1
#Verificar se uma usina hidrelétrica está funcionando acima da capacidade máxima. A variável energia_produzida armazena a quantidade de energia produzida em MWh e a variável capacidade_maxima armazena a capacidade máxima da usina em MWh. Utilizar uma estrutura if para imprimir se a usina está funcionando acima da capacidade máxima.

energia_produzida = 1050
capacidade_maxima = 1000
if energia_produzida > capacidade_maxima:
    print("A usina está funcionando acima da capacidade máxima.")

#Exercício 2
#Determinar se um carro elétrico tem carga suficiente para uma viagem. A variável carga_atual representa a carga atual da bateria em kWh, e a variável distancia_viagem representa a distância da viagem em km. O carro consome 0.2 kWh por km. Use uma estrutura if para determinar se o carro tem carga suficiente para a viagem.

carga_atual = 50
distancia_viagem = 200
if carga_atual >= distancia_viagem * 0.2:
    print("O carro tem carga suficiente para a viagem.")

#Exercício 3
#Verificar se é possível abastecer um veículo elétrico. A variável tipo_combustivel pode ser "eletrico" ou "gasolina". Se o tipo de combustível for elétrico, imprima "Pode abastecer". Caso contrário, imprimir "Não pode abastecer".

tipo_combustivel = "eletrico"
if tipo_combustivel == "gasolina":
    print("Pode abastecer.")
else:
    print("Não pode abastecer.")

#Exercício 4
#Neste exercício, você deve verificar se uma casa deve mudar para energia solar. A variável consumo_energia pode ser "alto", "medio" ou "baixo". Se o consumo for alto, imprima "Considere mudar para energia solar". Caso contrário, imprima "Mudança para energia solar opcional".

consumo_energia = "alto"
if consumo_energia == "alto":
    print("Considere mudar para energia solar.")
else:
    print("Mudança para energia solar opcional.")

#Exercício 5
#Neste exercício, crie uma variável produto contendo o nome de um produto e uma variável disponibilidade contendo um valor booleano (True, False). Use if e else para imprimir "Produto disponível" ou "Produto indisponível" baseado no valor da variável disponibilidade.

produto = "ProdutoX"
disponibilidade = False
if disponibilidade == True:
    print(produto, "- Produto disponível")
else:
    print(produto, "- Produto indisponível")

#Exercício 6
#Neste exercício, você deve criar uma variável categoria que será uma string representando a categoria de um produto. Utilize uma estrutura de controle para verificar a categoria do produto e imprimir uma mensagem relacionada à categoria.

categoria ="eletrico"
if categoria == "eletrico":
    print("Produto eletrônico selecionado")
else:
    print("Outra categoria selecionada")

#4.2. Exercícios sobre estrutura de dados tipo inteiro
#Exercício 7
#Neste exercício, você vai calcular o lucro total de uma sessão de cinema. Considere o número de ingressos vendidos e o preço de cada ingresso.

preco_ingresso = float(input("Digite o preço do ingresso: "))
quantidade_ingressos_vendidos = int(input("Digite o número de ingressos vendidos: "))

lucro_total = preco_ingresso * quantidade_ingressos_vendidos

print(f"Lucro total: {lucro_total}")

#Exercício 8
#Um cinema oferece desconto para estudantes na compra de ingressos. Se o comprador for estudante, o ingresso custa 15,00 , caso contrário, custa 30,00. Dado o status do comprador (estudante ou não) e a quantidade de ingressos, calcule o valor total a ser pago.

status_comprador = input("O comprador é estudante? (sim/nao): ")
quantidade_ingressos = int(input("Quantidade de ingressos: "))

if status_comprador == "sim":
    valor_total = quantidade_ingressos * 15
else:
    valor_total = quantidade_ingressos * 30
print(f"Valor total: R$ {valor_total}")

#Exercício 9
#Uma produtora de shows está analisando a viabilidade de um evento. Se a venda de ingressos for maior que 500, um lucro adicional de 10% sobre o total de vendas será aplicado. Dado o número de ingressos vendidos e o preço unitário do ingresso, calcule o lucro total. Suponha que o preço unitário do ingresso seja 50,00 e o custo fixo 10.000,00.

ingressos_vendidos = int(input("Digite o número de ingressos vendidos: "))
preco_unitario = 50
custo_fixo = 10000
receita = ingressos_vendidos * preco_unitario
if ingressos_vendidos > 500:
    lucro_total = custo_fixo - (receita * 0.1)
else:
    lucro_total = receita - custo_fixo
print(f"Lucro total: R$ {lucro_total}")

#Exercício 10

#Entrada:
#Solicitar o preço de custo e o preço de venda de um produto.
#Processo:
#Calcular o lucro subtraindo o preço de custo do preço de venda.
#Saída:
#Exibir o lucro.

# Entrada
preco_custo = float(input("Digite o preço de custo do produto: "))
preco_venda = float(input("Digite o preço de venda do produto: "))

# Processo
lucro = preco_venda - preco_custo

# Saída
print(f"Lucro: {lucro}")

#4.3. Exercícios sobre estrutura de dados tipo float

#Exercício 11
#A prefeitura de uma cidade planeja renovar a iluminação de uma praça, estimando um custo total de 12.500. Para cada doação recebida de 500, o governo municipal adicionará um valor igual até o limite de 6.250. Calcule o valor total arrecadado com as doações e a contribuição do governo. O valor total arrecadado do tipo float deverá ser formatado com duas casas decimais.

doacoes_recebidas = float(input("Digite o valor das doações recebidas: "))
doacao_governo = 500
limite_governo = 6250
contribuicao_governo = (doacoes_recebidas // doacao_governo) * doacao_governo
if contribuicao_governo > limite_governo:
    contribuicao_governo = limite_governo
valor_total_arrecadado = doacoes_recebidas + contribuicao_governo
print(f"Valor total arrecadado: R$ {valor_total_arrecadado:.2f}")

#4.4. Exercícios sobre estrutura de dados tipo boleano
#Exercício 12
#Agora, você deve elaborar a tabela verdade da operação lógica OR.

# Tabela Verdade de OR
print("Tabela Verdade de OR:")
print("True or True =", True or True)
print("True or False =", True or False)
print("False or True =", False or True)
print("False or False =", False or False)

#Exercício 13
#Agora, você deve elaborar a tabela verdade da operação lógica NOT.

# Tabela Verdade de NOT
print("Tabela Verdade de NOT:")
print("not True =", not True)
print("not False =", not False)

#Exercício 14
#Agora, você deve elaborar a tabela verdade da operação lógica NAND. A NAND B é verdadeira apenas quando A e B são falsas.

# Tabela Verdade de NAND
print("Tabela Verdade de NAND:")
print("True nand True: ", not (True and True))
print("True nand False: ", not (True and False))
print("False nand True: ", not (False and True))
print("False nand False: ", not (False and False))