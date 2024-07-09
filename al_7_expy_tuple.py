# Aula 7 - Exercícios em Sala de Aula

# Exercícios sobre estrutura de dados tipo 'tupla'

# Exercício 1

# Neste exercício, você deve concatenar duas tuplas, tupla1 = (1, 2, 3) e tupla2 = (4,), para criar uma nova tupla chamada tupla3.

tupla1 = (1, 2, 3)
tupla2 = (4,)
tupla3 = tupla1 + tupla2
print(tupla3)

# Exercício 2

# Neste exercício, você deve obter uma sub-tupla da tupla tupla = (1, 2, 3, 4, 5), contendo apenas os elementos do segundo ao quarto.

tupla = (1, 2, 3, 4, 5)
sub_tupla = tupla[1 : 4]
print(sub_tupla)

# Exercício 3

# Neste exercício, você deve acessar e imprimir o primeiro elemento da tupla tupla = (1, 2, 3).

tupla = (1, 2, 3)
elemento = tupla[:1]
print(elemento)

# Exercício 4

# Verifique se o número 2 está presente na tupla tupla = (1, 2, 3).

tupla = (1, 2, 3)
resultado = 2 in tupla
print(resultado)

# Exercício 5

# Determine o tamanho da tupla tupla = (1, 2, 3).

# Determine o tamanho de `tupla`
tupla = (1, 2, 3)
tamanho = len(tupla)
print(tamanho)

# Exercício 6

# Neste exercício, você tem uma tupla chamada maratonistas que contém o tempo, em horas, que cada corredor levou para completar uma maratona. Sua tarefa é encontrar quantos corredores completaram a maratona em menos de 4 horas e imprimir esse número.

maratonistas = (3.5, 4.2, 3.8, 5.1, 2.9, 3.3)
corredores_sub_4h = 0
for tempo in maratonistas:
    if tempo < 4:
        corredores_sub_4h += 1
print(corredores_sub_4h)

# Exercício 7

# Imagine que você tem uma tupla chamada tempos_volta com os tempos, em minutos, de 5 voltas em uma pista de corrida. Sua tarefa é contar e imprimir quantas voltas foram completadas em menos de 5 minutos.

tempos_volta = (4.5, 4.9, 5.1, 4.7, 5.2)
voltas_rapidas = 0
for tempo in tempos_volta:
  if tempo < 5:
    voltas_rapidas+=1
print(voltas_rapidas)

# Exercício 8

# Você tem uma tupla distancias_km com as distâncias, em quilômetros, que você correu cada dia da semana. Sua tarefa é encontrar e imprimir o total de quilômetros corridos na semana.

distancias_km = (5, 8, 6, 10, 7, 0, 0)
total_km = sum(distancias_km)
print(total_km)

# Exercício 9

# Considere uma tupla tempos_ciclismo com os tempos, em horas, de diferentes sessões de treino de ciclismo. Identifique e imprima o menor tempo de treino.

tempos_ciclismo = (2.5, 3.0, 1.75, 2.0, 2.25)
menor_tempo = min(tempos_ciclismo)
print(menor_tempo)

# Exercício 10

# Você tem uma tupla atividades_semanais que lista as atividades físicas praticadas em cada dia da semana, sendo alguns dias de descanso. Sua tarefa é contar e imprimir o número de dias que você praticou alguma atividade física.

atividades_semanais = ("ciclismo", "descanso", "natação", "descanso", "corrida", "descanso", "descanso")
dias_ativos = 0
for week in atividades_semanais:
  if week != "descanso":
    dias_ativos += 1
print(dias_ativos)
