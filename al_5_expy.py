#Aula 5 - Exercícios em Sala de Aula

#Exercícios sobre estrutura de dados tipo Lista

#Exercício 1
#Criar uma variável lista chamada destinos_populares contendo os seguintes destinos turísticos: "Paris", "Nova York", "Londres", "Tóquio", "Sydney".

destinos_populares = ["Paris", "Nova York", "Londres", "Tóquio", "Sydney"]
print(destinos_populares)

#Exercício 2
#Remover o destino "Tóquio" da lista destinos_populares criada no Exercício anterior.

destinos_populares.remove("Tóquio")
print(destinos_populares)

#Exercício 3
#Temos uma lista de hotéis chamada hoteis contendo: "Hilton", "Sheraton", "Marriott". Adicione o hotel "Ibis" ao final da lista.

hoteis = ["Hilton", "Sheraton", "Marriott"]
hoteis.append("Ibis")
print(hoteis)

#Exercício 4
#Dada uma lista com a quantidade de luas dos planetas quan_luas = [0, 0, 1, 2, 79, 82, 27, 14], verifique qual planeta tem mais luas. Os planetas estão em ordem: ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"]

quan_luas = [0, 0, 1, 2, 79, 82, 27, 14]
planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"]

luas = max(quan_luas)
indexLua = quan_luas.index(luas)

print(f"O planeta com mais luas é {planetas[indexLua]} com {luas} luas")

#Exercício 5
#Crie uma lista com os nomes dos 8 planetas do sistema solar. Em seguida, utilizando um loop for, imprima os nomes dos planetas que têm mais de 5 letras, juntamente com o número de letras de cada um.

planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"]
for planeta in planetas:
    if len(planetas) > 5:
        print(f"{planeta} tem {len(planetas)} letras.")

#Exercício 6
#Dada uma lista de planetas do sistema solar planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"], exclua da lista os planetas que iniciem com a letra 'M'.

planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"]

planetas_copy = planetas.copy() #faz uma cópia da lista para não alterar a original
for planeta in planetas_copy:
    if planeta[0] == 'M':
        planetas.remove(planeta)

print(planetas)

#Exercício 7
#Temos uma lista com os nomes dos planetas anões do sistema solar planetas_anoes = ['Plutão', 'Haumea', 'Makemake', 'Éris'] e outra lista com suas distâncias médias do sol em UA (Unidades Astronômicas) distancias = [39.5, 43.1, 45.8, 68.3]. Sua tarefa é imprimir os nomes dos planetas anões que estão a mais de 50 UA do sol.

planetas_anoes = ['Plutão', 'Haumea', 'Makemake', 'Éris']
distancias = [39.5, 53.1, 45.8, 68.3]
for planeta, distancia in zip(planetas_anoes, distancias):
    if distancia > 50:
        print(planeta)

#Exercício 8
#Dada uma lista com os nomes dos planetas do sistema solar planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"], crie uma nova lista apenas com os planetas que têm a letra 'a' no nome.

planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"]
planetas_com_a = []
# for planeta in planetas:
#     if 'a' in planeta:
#         planetas_com_a.append(planeta)

#ou
planetas_com_a = [planeta for planeta in planetas if 'a' in planeta]
print(planetas_com_a)

#Exercício 9
#Neste exercício, você deve concatenar duas listas. A primeira lista chamada 'diretores' contém os nomes de diretores de escolas primárias. A segunda lista chamada 'coordenadores' contém os nomes de coordenadores dessas escolas. Concatene as duas listas em uma nova lista chamada 'gestores'.

# Concatene as listas 'diretores' e 'coordenadores' para criar a lista 'gestores'
diretores = ['Ana Silva', 'Paulo Gomes']
coordenadores = ['Ricardo Neves', 'Beatriz Souza']
gestores = diretores + coordenadores
print(gestores)

#Exercício 10
#Neste exercício, você deve ordenar em ordem alfabética uma lista chamada 'disciplinas' que contém nomes de disciplinas escolares.

# Ordene a lista 'disciplinas' em ordem alfabética
disciplinas = ['História', 'Matemática', 'Geografia', 'Português']
ordenada = disciplinas.sort()
print(ordenada)

#Exercício 11
#Neste exercício, você deve encontrar o índice de um professor específico chamado 'Carlos Medeiros' na lista 'docentes'.

# Encontre o índice do professor 'Carlos Medeiros' na lista 'docentes'
docentes = ['Lúcia Barros', 'Carlos Medeiros', 'Roberto Silva']
professor = docentes.index('Carlos Medeiros')
print(professor)

#Exercício 12
#Neste exercício, você deve extrair uma sublista da lista 'alunos' que contém os nomes dos alunos do terceiro ao quinto.

# Extraia uma sublista da lista 'alunos' do terceiro ao quinto aluno
alunos = ['Ana', 'João', 'Pedro', 'Márcia', 'Eduardo', 'Luísa']
sublista = alunos[2:5]
print(sublista)

#Exercício 13
#Neste exercício, verifique se o professor 'Renata Lopes' está presente na lista 'professores'.

# Verifique se 'Renata Lopes' está na lista 'professores'
professores = ['Antônio Moura', 'Renata Lopes', 'Vitória Pires']
esta_presente = 'Renata Lopes' in professores
print(esta_presente)

#Exercício 14
#Dada a lista pacientes contendo os tempos que pacientes aguardaram para serem atendidos [23, 45, 17, 30], calcular o tempo médio de espera.

# Calcule o tempo médio de espera da lista 'pacientes'
tempos = [23, 45, 17, 30]
media_espera = sum(tempos) / len(tempos)
print(media_espera)

#Exercício 15
#Dada uma lista chamada 'notas', retorne a maior e a menor nota dos alunos.

# Retorne a maior e a menor nota da lista 'notas'
notas = [75, 85, 90, 60, 78, 88]
maior_nota = max(notas)
menor_nota = min(notas)
print("Maior nota:", maior_nota)
print("Menor nota:", menor_nota)

#Exercício 16
#Você possui uma lista com os nomes de algumas estrelas estrelas = ['Alfa Centauri A', 'Alfa Centauri B', 'Alfa Centauri C', 'Barnard'] e outra lista com suas respectivas velocidades radiais em relação à Terra em km/s velocidades = [-21.4, -18.6, -21.7, -110.6]. Sua tarefa é imprimir as estrelas que se movem a mais de 50 km/s em relação à Terra.

estrelas = ['Alfa Centauri A', 'Alfa Centauri B', 'Alfa Centauri C', 'Barnard']
velocidades = [21.4, 18.6, 21.7, 110.6]
for estrela, velocidade in zip(estrelas, velocidades):
    if velocidade > 50:
        print(estrela)
