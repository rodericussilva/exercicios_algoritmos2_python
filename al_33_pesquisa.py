# Aula 33 - Algoritmos para busca (pesquisa)
# Definição
# A pesquisa de valores objetiva encontrar a presença e a posição (índice) de um valor específico dentro de uma coleção de objetos. (fonte: Sedgewick, Algorithms)

# Problema: Dada uma lista desordenada ou ordenada de números encontre se um elemento existe e a sua posição.

# Exemplo: Pesquisar o Valor 7

# Em Python:

# As funções index() e in são métodos comumente usados em Python para realizar pesquisas em listas e outras coleções de dados.

# lista_desordenada = [4, 1, 7, 3, 9, 2, 8, 5, 6, 0]
# # encontrando o valor 7 no índice 3

# lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# # encontrando o valor 7 no índice 2.
# [ ]
# # Lista ordenada e desordenada
# lista = [4, 1, 7, 3, 9, 2, 8, 5, 6, 0]


# # Realizando pesquisa usando 'in' e 'index'

# if valor in lista: # 'in' localiza se o valor existe
#     resultado = lista.index(valor)  # 'index' retorna a posição
#     print ('O valor existe e a sua posição é:', resultado)
# else:
#     resultado = -1
#     print ('O valor não existe')
# O valor não existe
# fibbonacc.png Importância da pesquisa de valores
# Otimização no tempo da pesquisa:
# Em grandes volumes de dados, a eficiência na pesquisa de valores é fundamental para reduzir o tempo de resposta. ex: pesquisa de registros em banco de dados, mecanismo de busca na web (google), busca na lista de contatos do Samrtphone, busca na caixa de emails, etc

# Tipos de pesquisa
# (*)Linear search (pesquisa linear)
# (*)Binary search (pesquisa binária)
# Interpolation search (Pesquisa por interpolação)
# Exponential seacrch(Pesquisa exponencial)
# ...etc
# Pesquisa Linear
# A pesquisa linear é um método de busca que verifica cada elemento de uma lista ou coleção de dados, um por um, até encontrar o elemento desejado ou até ter examinado todos os elementos sem sucesso. É a maneira mais simples de procurar um elemento em uma lista.

# Pode ser aplicada em listas ordenadas ou desordenadas.

# Explicação do algoritmo de pesquisa linear
# Inicialização:

# O algoritmo começa na primeira posição da lista, ou seja, no índice 0.
# Iteração e Comparação:

# O algoritmo compara o elemento atual da lista com o valor que está sendo procurado.
# Se o elemento atual é igual ao valor procurado, o algoritmo retorna a posição (ou índice) desse elemento na lista.
# Se o elemento atual não é igual ao valor procurado, o algoritmo move-se para o próximo elemento na lista.
# Continuação até o Fim da Lista:

# Esse processo de comparação é repetido para cada elemento da lista, movendo-se sequencialmente de um elemento para o próximo.
# Conclusão da Busca:

# Se o valor procurado for encontrado em algum momento durante a iteração, o algoritmo termina e retorna a posição do elemento.
# Se o algoritmo chega ao final da lista sem encontrar o valor procurado, ele retorna um valor indicativo de que o elemento não está presente na lista (geralmente, -1 ou None)
# Exemplo

# Lista:
# [10, 22, 35, 47, 55, 63, 70, 85, 95]

# Valor a ser Procurado:
# 55

# Passo-a-passo:
# Elemento Atual: 10, Comparação: 10 == 55, Resultado: Não, Próximo Elemento
# Elemento Atual: 22, Comparação: 22 == 55, Resultado: Não, Próximo Elemento
# Elemento Atual: 35, Comparação: 35 == 55, Resultado: Não, Próximo Elemento
# Elemento Atual: 47, Comparação: 47 == 55, Resultado: Não, Próximo Elemento
# Elemento Atual: 55, Comparação: 55 == 55, Resultado: Sim, Conclusão: Encontrado na posição 4
# Algoritmo de pesquisa linear (linear search) em python
# [ ]
# def pesquisa_linear(lista, valor):
#     for i in range(len(lista)):
#         if lista[i] == valor:
#             return i  # Retorna o índice do valor encontrado
#     return -1  # Retorna -1 se o valor não for encontrado

# # Exemplo de uso
# lista_exemplo = [3, 5, 7, 9, 11]
# valor_procurado = 7
# resultado = pesquisa_linear(lista_exemplo, valor_procurado)
# print(f"O valor {valor_procurado} foi encontrado no índice {resultado}" if resultado != -1 else "Valor não encontrado.")
# Eficiência da pesquisa linear
# A pesquisa linear tem uma complexidade de tempo de O(n) no pior caso, onde n é o número de elementos na lista. Isso porque, no pior cenário, todos os elementos da lista precisam ser examinados para encontrar o valor ou determinar que ele não está presente.

# Obs: O Algoritmo interno de pesquisa que o Python utiliza na função lista.index(valor) é deste tipo pesquisa linear.

# Eficiência dos algoritmos de pesquisa
# Método de Pesquisa	Ordem de Complexidade
# Linear Search	O(n)
# Binary Search	O(log n)
# Interpolation Search	O(log log n)
# Exponential Search	O(log n)
# in python	O(n)
# imagem1.png

# Pesquisa Binária (Binary search)
# Na pesquisa binária a lista necessariamente tem que estar ordenada.

# A pesquisa binária é um método eficiente para encontrar um elemento em uma lista ordenada. Em vez de verificar cada elemento da lista um por um, a pesquisa binária divide a lista ao meio a cada passo, reduzindo significativamente o número de comparações necessárias.

# Expicação do algoritmo da Pesquisa Binária:
# Iniciar:

# Defina duas variáveis, inicio e fim, que representam os índices do início e do fim da lista. Inicialmente, inicio é 0 e fim é o último índice da lista.
# Calcular o meio:

# Encontre o índice do meio da lista: meio = (inicio + fim) // 2.
# Comparar o meio:

# Compare o elemento no índice meio com o elemento que você está procurando:
# Se for igual, você encontrou o elemento! Retorne o índice meio.
# Se for menor, significa que o elemento procurado está na metade direita da lista. Ajuste inicio para meio + 1.
# Se for maior, significa que o elemento procurado está na metade esquerda da lista. Ajuste fim para meio - 1.
# Repetir:

# Repita os passos 2 e 3 até que inicio seja maior que fim. Se inicio ultrapassar fim e você não tiver encontrado o elemento, significa que ele não está na lista.
# Exemplo:
# Vamos procurar o número 25 na lista ordenada [11, 12, 22, 25, 64].

# Passo-a-passo
# Inicialização:

# inicio = 0
# fim = 4 (último índice da lista)
# Primeira Iteração:

# Calcular meio: (0 + 4) // 2 = 2
# O elemento no índice 2 é 22
# 22 não é igual a 25, e 25 é maior que 22, então ajustamos inicio para 3.
# Segunda Iteração:

# Calcular meio: (3 + 4) // 2 = 3
# O elemento no índice 3 é 25
# 25 é igual a 25, encontramos o elemento!
# Vantagens:
# Rápida: Muito mais eficiente do que a pesquisa linear para listas grandes.
# Simples: Fácil de entender e implementar para listas ordenadas.
# Desvantagem:
# Requer Ordenação: Funciona apenas em listas que já estão ordenadas.
# Visualizando o algoritmo 'binary search'
# https://www.youtube.com/watch?v=eVuPCG5eIr4

# Algoritmo 'binary search' em python
# [ ]
# def pesquisa_binaria(lista, valor):
#     inicio, fim = 0, len(lista) - 1
#     while inicio <= fim:
#         meio = (inicio + fim) // 2
#         if lista[meio] == valor:
#             return meio  # Retorna o índice do valor encontrado
#         elif lista[meio] < valor:
#             inicio = meio + 1
#         else:
#             fim = meio - 1
#     return -1  # Retorna -1 se o valor não for encontrado

# # Exemplo de uso
# lista_ordenada = [3, 5, 7, 9, 11]
# valor_procurado = 9
# resultado = pesquisa_binaria(lista_ordenada, valor_procurado)
# print(f"O valor {valor_procurado} foi encontrado no índice {resultado}" if resultado != -1 else "Valor não encontrado.")

# Análise da eficiência da pesquisa binária
# Análise da Complexidade de Tempo
# A pesquisa binária opera em uma lista ordenada e funciona dividindo repetidamente a lista ao meio até que o elemento procurado seja encontrado ou os subintervalos sejam reduzidos a zero. Aqui está um passo a passo do que ocorre:

# Inicialização:

# Você começa com uma lista de tamanho n.
# Divisão Repetitiva:

# A cada iteração, a lista é dividida em duas metades.
# Em cada divisão, você descarta metade dos elementos da consideração.
# Isso é equivalente a uma operação de divisão por 2 em termos de redução do número de elementos restantes.
# Número de Iterações:

# No pior caso, para reduzir a lista de n elementos para 1 elemento, você precisa dividir a lista repetidamente até que o tamanho seja 1.
# O número de vezes que você pode dividir n pela metade até chegar a 1 é log2n.
# Portanto, o número de iterações necessárias para encontrar o elemento ou determinar que ele não está na lista é log2n.
# Exemplo:
# Vamos considerar uma lista de 16 elementos. A sequência de operações seria:

# Iteração 1: Lista de 16 elementos → Dividida em duas listas de 8 elementos
# Iteração 2: Lista de 8 elementos → Dividida em duas listas de 4 elementos
# Iteração 3: Lista de 4 elementos → Dividida em duas listas de 2 elementos
# Iteração 4: Lista de 2 elementos → Dividida em duas listas de 1 elemento
# Neste exemplo, são necessárias 4 iterações log216=4 para reduzir a lista de 16 elementos a uma única possibilidade.

# FIM da aula de tipos de pesquisa
# Excerto final
# Na Aula passada foi perguntado um exemplo de algoritmo com complexidade O(2n)

# Exemplo de algoritmo complexidade O(2n)
# Um exemplo clássico de um algoritmo com complexidade O(2n) é o cálculo ingênuo da sequência de Fibonacci usando recursão. Neste método, cada cálculo de Fibonacci gera duas chamadas recursivas (exceto os casos base), o que leva a uma árvore de chamadas exponencialmente grande.

# fibbonacc.jpg

# Sequência de Fibonacci
# A sequência de Fibonacci é definida da seguinte maneira:

# F(0)=0
# F(1)=1
# F(n)=F(n−1)+F(n−2) para n>1
# Algoritmo Recursivo
# Aqui está o algoritmo recursivo para calcular o n-ésimo número de Fibonacci:

# [ ]

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # Exemplo de uso
# n = 5
# print(f'O {n}-ésimo número de Fibonacci é {fibonacci(n)}')

# O 5-ésimo número de Fibonacci é 5
# Passo a Passo do Algoritmo
# Vamos considerar o cálculo de fibonacci(5) para entender melhor o crescimento exponencial:

# fibonacci(5)
# fibonacci(4) + fibonacci(3)
# (fibonacci(3) + fibonacci(2)) + (fibonacci(2) + fibonacci(1))
# ((fibonacci(2) + fibonacci(1)) + (fibonacci(1) + fibonacci(0))) + ((fibonacci(1) + fibonacci(0)) + 1)
# (((fibonacci(1) + fibonacci(0)) + 1) + (1 + 0)) + ((1 + 0) + 1)
# (((1 + 0) + 1) + 1) + (1 + 1)
# (1 + 1) + 1
# 2 + 1
# 3
# Podemos ver que muitos cálculos são repetidos. Por exemplo, fibonacci(2) é calculado várias vezes. Isso leva a um número de chamadas recursivas que cresce exponencialmente com n, resultando em uma complexidade de O(2n).

# Complexidade
# A complexidade de tempo do algoritmo recursivo ingênuo para calcular o n-ésimo número de Fibonacci é O(2n). Isso porque cada chamada para fibonacci(n) resulta em duas chamadas recursivas para fibonacci(n-1) e fibonacci(n-2), levando a um crescimento exponencial do número de chamadas.

