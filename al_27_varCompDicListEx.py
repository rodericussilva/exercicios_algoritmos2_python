#Aula 27 - dicionário de listas

#Tarefa Imprimir
#Considere o dicionário de listas abaixo que apresenta a distribuição de recursos e beneficiários de programas de saúde em diferentes regiões, facilitando a avaliação do impacto das políticas públicas de saúde em escala regional.

#obs: valores em milhões de reais

prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}
#Gerar um relatório detalhado mostrando todas as regiões, totais de beneficiários por região e o investimentos por região, conforme abaixo:

#Relatório de Programas de Saúde:
#--------------------------------
#Região: Norte, Beneficiários: 1200000, Investimento: R$ 300 milhões
#Região: Nordeste, Beneficiários: 950000, Investimento: R$ 250 milhões
#Região: Sudeste, Beneficiários: 800000, Investimento: R$ 200 milhões
#Região: Sul, Beneficiários: 1500000, Investimento: R$ 350 milhões
#Região: Centro-Oeste, Beneficiários: 1300000, Investimento: R$ 320 milhões

print('Relatório de Programas de Saúde:')
print('--------------------------------')
for regiao, total, invest in zip(prog_saude['regiao'], prog_saude['beneficiarios'], prog_saude['investimento']):
    print(f'Regiao: {regiao}, beneficiarios: {total}, investimento: {invest}')

#Tarefa Contar elementos
#Considere o dicionário de listas abaixo.

prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}
#Contar o número todal de regiões analisadas cujo quantidade de beneficiários seja maior que 100000 e investimentos superiores a R$ 200 milhões. Gere a saída no formato abaixo

#Quantidade de regiões: xx

count = 0
for regiao, beneficiario, invest in zip(prog_saude['regiao'], prog_saude['beneficiarios'], prog_saude['investimento']):
    if beneficiario > 100000 and invest > 200:
        count+=1
print(f'Quantidade de regiões: {count}')

#Tarefa Acumular elementos
#Considere o dicionário de listas abaixo.

prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}
#Calcule o total de investimentos realizados Norte e Nordeste. Gere a saída no formato abaixo.

#Total de investimentos realizados nas regiões norte e nordeste: R$ xxxxx milhões

count1 = 0
count2 = 0
for local, invest in zip(prog_saude['regiao'], prog_saude['investimento']):
    if local == 'Norte': 
        count1+=invest
    if local == 'Nordeste':
        count2+=invest
count1 = count1 + count2
print(f'Total de investimentos realizados nas regiões norte e nordeste: R$ {count1} milhões')

#Tarefa Calcular a Média
#Considere o dicionário de listas abaixo.

prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}
#Calcular a média de investimento em reais por beneficiário em cada região. Gerar a saída no formato a seguir. Atentar que os valores investidos estão em milhões de reais e, portanto, devem ser convertidos para reais multiplicando por 1.000.000:

#Região: Norte, Média investimento por beneficiário: R$ 250.0
#Região: Nordeste, Média investimento por beneficiário: R$ 263.1578947368421
#Região: Sudeste, Média investimento por beneficiário: R$ 250.0
#Região: Sul, Média investimento por beneficiário: R$ 233.33333333333334
#Região: Centro-Oeste, Média investimento por beneficiário: R$ 246.15384615384616

m = 0
for regiao, beneficiario, invest in zip(prog_saude['regiao'], prog_saude['beneficiarios'], prog_saude['investimento']):
    m = (invest * 1000000) / beneficiario
    print(f'Região: {regiao}, Média investimento por beneficiário: R$ {m}')

#Tarefa Selecionar Maior Elemento
#Considere o dicionário de listas abaixo.

prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}
#Encontrar regiao com maior número de beneficiários. Gere a saída no formato abaixo.

#Região com maior número de beneficiários: xxxxx, Qtd. beneficiários: yyy

maior = 0
for regiao, beneficiario in zip(prog_saude['regiao'], prog_saude['beneficiarios']):
    if beneficiario > maior:
        maior = beneficiario
print(f'Região com maior número de beneficiários: {regiao}, Qtd. beneficiários: {maior}')

#Tarefa Selecionar Menor Elemento
#Considere o dicionário de listas abaixo.

prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}
#Encontrar regiao com menor numero de investimentos. Gere a saída no formato abaixo.

#Região com o menor investimento: xxx, Montate de investimento: R$ yyy Milhões

menor = 350
reg = ''
for regiao, invest in zip(prog_saude['regiao'], prog_saude['investimento']):
    if invest < menor:
        menor = invest
        reg = regiao
print(f'Região com o menor investimento: {reg}, Montate de investimento: R$ {menor} Milhões')

#Exercícios adicionais
#Calcular: média, percentuais, etc
#Armazenando resultado do cálculo em variáveis temporárias para uso posterior
#Usando mais de uma variável de entrada relacionadas
#Tarefa Calcular o valor adicional de investimentos e armazenar em uma variável temporária
#Considere o dicionário de listas abaixo.

prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}
#O governo federal resolveu liberar verbas adicionais no valor de 10% do montante do investimento atual. Gere uma variável temporária tipo dicionário contendo como chaves as regiões e o valores contendo os adicionais de investimentos liberados. Imprima na saída o conteúdo dessa variável.

{'Norte': 30.0, 'Nordeste': 25.0, 'Sudeste': 20.0, 'Sul': 35.0, 'Centro-Oeste': 32.0}

hhh = dict()
valor = 0
for regiao, invest in zip(prog_saude['regiao'], prog_saude['investimento']):
    valor = invest * (10/100)
    hhh[regiao] = valor

print(hhh)
    
#Tarefa Alterar elementos a partir de duas variáveis de entrada
#Considere o dicionário de listas abaixo e o novo dicionário contendo o valor de incremento populacional que cada região teve.

prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}

incremento_pop = {"Norte": 20000,  "Sudeste": 10000, "Sul": 90000 }
#Atualize os valores da nova quantidade de beneficiários de cada região atualizando a lista de dicionário prog_saude adicionando o incremento populacional contido na variável incremento_pop. Imprima na saída a lista de dicionário prog_saude atualizada.

#obs: atentar que de acordo com o conteúdo da variável incremento_pop nem todas as regiões sofreram incrementos populacionais.

prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}
incremento_pop = {"Norte": 20000,  "Sudeste": 10000, "Sul": 90000 }

for regiao, beneficiario in zip(prog_saude['regiao'], prog_saude['beneficiarios']):
    if regiao == 'Norte':
        atual1 = beneficiario + incremento_pop["Norte"]
        #valor = prog_saude['regiao'].index('Norte')
        prog_saude['beneficiarios'][prog_saude['regiao'].index('Norte')] = atual1
    if regiao == 'Sudeste':
        atual2 = beneficiario + incremento_pop['Sudeste']
        valor2 = prog_saude['regiao'].index('Sudeste')
        prog_saude['beneficiarios'][valor2] = atual2
    if regiao == 'Sul':
        atual3 = beneficiario + incremento_pop['Sul']
        valor3 = prog_saude['regiao'].index('Sul')
        prog_saude['beneficiarios'][valor3] = atual3
print(prog_saude)
