# Aula 10 - Exercícios em Sala de Aula

# Exercícios sobre list comprehension

# Exercício 1
# Imagine que você está programando um robô para reconhecer números ímpares que são cruciais para a ativação de diferentes módulos de um sistema de automação. Crie uma lista chamada numeros_impares com os números ímpares de 1 a 10 usando list comprehension.

import code


numeros_impares = [numero for numero in range(1, 11) if numero % 2 != 0]
print(numeros_impares)

# Exercício 2
# Para um sistema de visão computacional que identifica peças robóticas, precisamos listar todos os IDs de peças que começam com a letra 'R'. Dado uma lista de IDs ['R01', 'B02', 'R03', 'M04', 'R05'], crie uma lista chamada ids_robos usando list comprehension que contém apenas os IDs que começam com 'R'.

ids = ['R01', 'B02', 'R03', 'M04', 'R05']
ids_robos = [id for id in ids if id.startswith('R')]
print(ids_robos)

# Exercício 3
# Num projeto de automação, é essencial identificar e catalogar as velocidades de diferentes motores robóticos. Dada a lista de velocidades velocidades = [100, 200, 300, 400, 500], crie uma lista chamada velocidades_reduzidas usando list comprehension que contenha todas as velocidades reduzidas pela metade, pois o sistema precisa operar em uma capacidade mais segura.

velocidades = [100, 200, 300, 400, 500]
velocidades_reduzidas = [velocidade / 2 for velocidade in velocidades]
print(velocidades_reduzidas)

# Exercício 4
# Em um sistema de controle de qualidade, você precisa identificar peças com defeito cujo código termina com 'D' e marcá-las como defeituosas. Dada uma lista de códigos de peças codigos = ['X1D', 'X2', 'X3D', 'X4'], crie uma lista chamada codigos_defeituosos usando list comprehension, onde cada código válido é seguido por '_DEF'.

codigos = ['X1D', 'X2', 'X3D', 'X4']
codigos_defeituosos = [cod + '_DEF' for cod in codigos if cod.endswith('D')]
print(f"{codigos_defeituosos}")

# Exercício 5
# Considere uma fábrica de robôs onde cada modelo é identificado por um código único composto por letras e números. Você tem uma lista de códigos de modelos produzidos (modelos_produzidos) e uma lista com os códigos dos modelos que falharam no teste de qualidade (modelos_falhos). Seu desafio é criar uma lista de códigos dos modelos que passaram no teste de qualidade e outra lista com esses códigos adicionando a sufixo "_OK" para indicar que estão prontos para a venda. Utilize list comprehension para realizar essa tarefa.

modelos_produzidos = ['R2D2', 'R3D3', 'R4D4', 'R5D5', 'R2F2']
modelos_falhos = ['R2D2', 'R4D4']

modelos_aprovados = [modelo for modelo in modelos_produzidos if modelo not in modelos_falhos]

modelos_aprovados_ok = [modelo + "_OK" for modelo in modelos_aprovados]

print("Modelos aprovados:", modelos_aprovados)
print("Modelos aprovados com sufixo '_OK':", modelos_aprovados_ok)

# Exercício 6
# Em um laboratório de automação e robótica, você precisa monitorar a temperatura (em Celsius) de vários sensores distribuídos em um robô. Converta a lista de temperaturas (temperaturas_celsius) para Fahrenheit e gere uma nova lista com as temperaturas acima de 50°F. Use list comprehensions para ambas as conversões e filtragens.

# obs: a fómula para para tranformar de temperatura celsiu para farehheit é f = (celsius * 9/5) + 32

temperaturas_celsius = [20, 15, 30, 10, 25]

temperaturas_fahrenheit_acima_50 = [temp_fahrenheit for temp_celsius in temperaturas_celsius if (temp_fahrenheit := (temp_celsius * 9/5) + 32) > 50]

print("Temperaturas em Fahrenheit acima de 50°F:", temperaturas_fahrenheit_acima_50)

#Exercício 7
#Num projeto de automação residencial, você precisa controlar dispositivos baseados em seu consumo de energia. Dada uma lista de consumos de energia em watts (consumos_watts) de vários dispositivos, crie duas listas: uma com os dispositivos de baixo consumo (menos de 100 watts) e outra com os consumos convertidos para kilowatts, com a adição do sufixo " kW" para cada valor. Utilize list comprehensions para ambas as tarefas.

consumos_watts = [50, 150, 75, 200, 100]

dispositivos_baixo_consumo = [consumo for consumo in consumos_watts if consumo < 100]
consumos_kilowatts = [f"{consumo / 1000} kW" for consumo in consumos_watts]
print("Dispositivos de baixo consumo:", dispositivos_baixo_consumo)
print("Consumos em kilowatts:", consumos_kilowatts)