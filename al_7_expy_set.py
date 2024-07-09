# Aula 7 - Exercícios em Sala de Aula
# Exercícios sobre estrutura de dados tipo 'conjunto'

# Exercício 1

# Neste exercício, você deve criar um conjunto de números inteiros chamado numeros e adicionar os números 5, 10 e 15 ao conjunto. Adicione estes números ao conjunto inicial {1, 2, 3} e imprima o conjunto resultante.

numeros = {1, 2, 3}
numeros.add(5)
numeros.add(10)
numeros.add(15)
print(numeros)

# Exercício 2

# Neste exercício, dado um conjunto cores contendo as cores "vermelho", "azul" e "verde", você deve remover a cor "azul" do conjunto e imprimir o conjunto atualizado.

cores = {"vermelho", "azul", "verde"}
cores.remove("azul")
print(cores)

# Exercício 3

# Neste exercício, verifique se o elemento "vermelho" está presente no conjunto cores e imprima True se estiver presente, ou False caso contrário.

cores = {"vermelho", "azul", "verde"}
print("vermelho" in cores)

# Exercício 4

# Neste exercício, dados dois conjuntos, conjuntoA = {1, 2, 3} e conjuntoB = {4, 5, 6}, encontre a união desses dois conjuntos e imprima o resultado.

conjuntoA = {1, 2, 3}
conjuntoB = {3, 4, 5, 6}
uniao = conjuntoA.union(conjuntoB)
print(uniao)

# Exercício 5
# Neste exercício, você deve criar um conjunto chamado modalidades_esportivas contendo os nomes de diferentes esportes. Em seguida, use um loop for para iterar sobre este conjunto. Se o nome do esporte contiver mais de 6 letras, imprima o nome do esporte.

modalidades_esportivas = {'futebol', 'basquete', 'natação', 'vôlei', 'tênis'}
for esporte in modalidades_esportivas:
    if len(esporte) > 6:
        print(esporte)

# Exercício 6

# Neste exercício, você deve inicializar um conjunto chamado atletas com nomes de atletas. Em seguida, crie um loop for para verificar se o nome 'Carlos' está no conjunto. Se estiver, imprima "Carlos é um atleta".

atletas = {'Ana', 'Carlos', 'João', 'Mariana'}
for atleta in atletas:
    if atleta == 'Carlos':
        print('Carlos é um atleta')

# Exercício 7

# Neste exercício, você deve criar um conjunto chamado exercicios contendo nomes de diferentes exercícios físicos. Em seguida, use um loop for para iterar sobre este conjunto e uma instrução if para imprimir apenas os exercícios que contêm a palavra 'corrida'.

exercicios = {'corrida de rua', 'natação', 'corrida em esteira', 'ciclismo'}
for exercicio in exercicios:
    if 'corrida' in exercicio:
        print(exercicio)
        
# Exercício 8

# Neste exercício, você deve criar um conjunto chamado dias_treino contendo os dias da semana que você planeja treinar. Use um loop for para iterar sobre o conjunto e uma instrução if para imprimir "Hoje tem treino!" se o dia for 'Segunda', 'Quarta' ou 'Sexta'.

dias_treino = {'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'}
for dias in dias_treino:
    if dias == 'Segunda' and 'Quarta' and 'Sexta':
        print("Hoje tem treino")

# Exercício 9

# Dados dois conjuntos de cores, encontre e imprima as cores que são comuns a ambos os conjuntos.

conjunto_cores1 = {'vermelho', 'azul', 'verde'}
conjunto_cores2 = {'azul', 'verde', 'amarelo'}

inter = conjunto_cores1.intersection(conjunto_cores2)
print(inter)