# Aula 32 - Algoritmos para Ordenação
# Ordenação
# Definição
# É o processo de rearranjar uma coleção de objetos de forma a os colocar em uma ordem lógica (ex: numérica crescente ou numérica decrescente, etc) (fonte: Sedgewick, Algorithms).

# outros tipos de lógicas ordenação: alfabética, por categoria, chave composta, etc

# outros objetos ordenáveis: strings, objetos personalizados, elementos de estruturas de dados (listas, árvores e grafos), registros de bancos de dados, etc

# Problema: Dada uma lista desordenada de números gere uma lista ordenada crescente

# Em Python:

# O método sorted() em Python é uma função que retorna uma nova lista contendo todos os elementos da sequência de entrada em ordem ascendente ou descendente.

# [ ]
# # Programa em Python

# lista_desordenada = [5, 3, 1, 4, 2]

# lista_ordenada = sorted (lista_desordenada, reverse= False)

# print (lista_ordenada)
# Importância da ordenação
# Facilita a análise humana de dados:

# Possibilita a apresentação da informação de maneira mais lógica e compreensível. ex: Cartão de Crédito, arquivos, ordenação de pesquisas na web, listas de recomendações, etc

# Possibilita maior eficiência de algoritmos:

# Ordenação reduz o tempo necessário para processar grandes volumes de dados. ex: Banco de dados (junções, agrupamentos e recuperação de registros)

# Tipos de Ordenação
# *selection Sort (ordenação por seleção)
# insertion sort (Ordenação por inserção)
# *Bubble sort
# *Merge Sorte (ordenaçao por intercalação)
# Tree sort
# Quick sort
# Heap sort
# Radix sort
# Timsort (usado na função sort do python (merge sort e insertion sort)
# ...etc
# Selection Sort (ordenação por seleção)
# Demonstração do 'selection sort'
# Primeiro, ache o menor elemento da lista e troque-o com o primeiro elemento da lista. Então, ache o próximo menor elemento do restante da lista e troque-o com o segundo. Continue até que a lista esteja toda ordenada.

# Esse método é chamado de seleção porque ele trabalha repetidamente selecionando o menor elemento da lista restante.

# Exemplo: Lista inicial desordenada: [64, 25, 12, 22, 11]

# Passo 1 - Encontrando o menor elemento (índice 4) e trocando com o primeiro elemento: [11, 25, 12, 22, 64]

# Passo 2 - Considerando a lista restante como não ordenada e encontrando o menor elemento (índice 2) para trocar com o segundo elemento: [11, 12, 25, 22, 64]

# Passo 3 - Novamente, considerando a lista restante como não ordenada e encontrando o menor elemento (índice 3) para trocar com o terceiro elemento: [11, 12, 22, 25, 64]

# Passo 4 - Uma vez mais, considerando a lista restante como não ordenada e encontrando o menor elemento (índice 4) para trocar com o quarto elemento: [11, 12, 22, 25, 64]

# Visualizando o algoritmo 'selection sort'
# https://www.youtube.com/watch?v=92BfuxHn2XE

# Algoritmo 'selection sort' em python
# [ ]
# def selection_sort(lista):
#     tamanho = len(lista)

#     for i in range(tamanho - 1):
#         indice_menor = i

#         # Encontra o índice do menor elemento na parte não ordenada da lista
#         for j in range(i + 1, tamanho):
#             if lista[j] < lista[indice_menor]:
#                 indice_menor = j

#         # Troca o menor elemento encontrado com o primeiro elemento da parte não ordenada
#         if indice_menor != i:
#             lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

# # Exemplo de uso:
# lista = [64, 25, 12, 22, 11]
# selection_sort(lista)
# print("Lista ordenada:", lista)
# Cálculo da Eficiência do algoritmo acima
# Para calcular a complexidade do algoritmo de ordenação por seleção (Selection Sort), analisamos as operações principais do algoritmo em termos de tempo de execução.

# Passos do Algoritmo:
# Inicialização:

# tamanho = len(lista)
# Esta operação é O(1).

# Loop Externo:

# for i in range(tamanho - 1):
#     indice_menor = i
# Este loop executa (n−1) vezes, onde n é o tamanho da lista. Portanto, a complexidade é O(n).

# Encontrar o Menor Elemento:

# for j in range(i + 1, tamanho):
#     if lista[j] < lista[indice_menor]:
#         indice_menor = j
# O loop interno percorre os elementos da lista a partir de i+1 até tamanho, ou seja, percorre (n−i−1) elementos. No pior caso, o loop interno é executado aproximadamente (n−1) vezes na primeira iteração, (n−2) vezes na segunda iteração, e assim por diante, até 1 vez na última iteração. Portanto, a soma das operações é:

# (n−1)+(n−2)+(n−3)+...+1=(n−1)∗n/2

# Isso simplifica para O(n2).

# Troca:

# if indice_menor != i:
#     lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
# Esta operação é O(1) e ocorre (n−1) vezes no loop externo, resultando em O(n).

# Complexidade Total

# Somando todas as complexidades, temos:

# Inicialização: O(1)
# Loop Externo: O(n)
# Encontrar o Menor Elemento: O(n2)
# Troca: O(n)
# A complexidade dominante é a operação de encontrar o menor elemento, que é O(n2).

# Portanto, a complexidade de tempo total do algoritmo de ordenação por seleção (Selection Sort) é:** O(n2)**

# Este algoritmo é considerado ineficiente quando comparado ao Quick Sort e Merge Sort.

# Visão Geral de alguns algoritmos de ordenação
# Tabela e complexidade de tempo:

# Algoritmo	Complexidade de Tempo no Pior Caso
# Selection Sort	O(n^2)
# Insertion Sort	O(n^2)
# Bubble Sort	O(n^2)
# Merge Sort	O(n log n)
# Tree sort	O(n log n)
# Quick Sort	O(n^2) no pior caso, O(n log n) em média
# Heap Sort	O(n log n)
# Timsort (Python)	O(n log n)
# imagem1.png

# Algoritmo de ordenação Bubble sort
# Demonstração do 'bubble sort' (ordenação por bolha)
# O algoritmo de ordenação por bolha compara repetidamente pares adjacentes de elementos na lista e os troca se estiverem na ordem errada. Este processo é repetido até que a lista esteja ordenada.

# Esse método é chamado de bolha porque os maiores elementos "borbulham" para o topo da lista a cada iteração.

# Exemplo: Lista inicial desordenada: [64, 25, 12, 22, 11]

# Passo 1 - Comparar e trocar elementos adjacentes ao longo da lista:

# Comparar 64 e 25, trocar: [25, 64, 12, 22, 11]
# Comparar 64 e 12, trocar: [25, 12, 64, 22, 11]
# Comparar 64 e 22, trocar: [25, 12, 22, 64, 11]
# Comparar 64 e 11, trocar: [25, 12, 22, 11, 64]
# Passo 2 - Repetir o processo, ignorando o último elemento já ordenado:

# Comparar 25 e 12, trocar: [12, 25, 22, 11, 64]
# Comparar 25 e 22, trocar: [12, 22, 25, 11, 64]
# Comparar 25 e 11, trocar: [12, 22, 11, 25, 64]
# Passo 3 - Repetir o processo, ignorando os dois últimos elementos já ordenados:

# Comparar 12 e 22, sem troca: [12, 22, 11, 25, 64]
# Comparar 22 e 11, trocar: [12, 11, 22, 25, 64]
# Passo 4 - Repetir o processo, ignorando os três últimos elementos já ordenados:

# Comparar 12 e 11, trocar: [11, 12, 22, 25, 64]
# Passo 5 - Última verificação para garantir que a lista está ordenada:

# Comparar 11 e 12, sem troca: [11, 12, 22, 25, 64]
# Após esses passos, a lista está completamente ordenada.

# Algoritmo de Ordenação por Bolha em Python
# Vizualizando o algoritmo Bubble Sort
# https://www.youtube.com/watch?v=Cq7SMsQBEUw

# [ ]
# def bubble_sort(arr):
#     n = len(arr)
#     # Percorre todos os elementos do array
#     for i in range(n):
#         # A última i-ésima posição já estará no lugar certo após i iterações
#         for j in range(0, n-i-1):
#             # Troque se o elemento encontrado for maior que o próximo elemento
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# # Exemplo de uso
# lista = [64, 25, 12, 22, 11]
# sorted_lista = bubble_sort(lista)
# print("Lista ordenada:", sorted_lista)

# Array ordenado: [11, 12, 22, 25, 64]
# Explicação do Algoritmo Bubble Sort
# Inicialização: n = len(arr) define o comprimento do array a ser ordenado.
# Primeiro loop: O loop externo for i in range(n) percorre todos os elementos do array.
# Segundo loop: O loop interno for j in range(0, n-i-1) compara cada par de elementos adjacentes. Ele percorre até n-i-1 porque os últimos i elementos já estarão no lugar certo após i iterações.
# Troca: Se arr[j] > arr[j+1], então arr[j] e arr[j+1] são trocados.
# O algoritmo continua até que todos os elementos estejam na ordem correta. Este é um método de ordenação simples, mas pode ser ineficiente para grandes listas devido à sua complexidade de tempo (O(n2)).

# Algoritmo Merge Sort
# O algoritmo Merge Sort é um algoritmo de ordenação baseado na técnica de divisão e conquista. A ideia principal é dividir a lista a ser ordenada em duas metades, ordenar cada metade de forma recursiva e, finalmente, combinar (merge) as duas metades ordenadas para produzir uma lista ordenada. Aqui está uma explicação detalhada do funcionamento do Merge Sort:

# Divisão:

# Se a lista tem um único elemento ou está vazia, ela já está ordenada.
# Caso contrário, divida a lista ao meio.
# Conquista:

# Ordene recursivamente cada metade da lista.
# Combinação:

# Combine as duas metades ordenadas em uma única lista ordenada.
# [ ]
# def merge_sort(lista):
#     if len(lista) <= 1:
#         return lista

#     # Dividir a lista ao meio
#     meio = len(lista) // 2
#     esquerda = lista[:meio]
#     direita = lista[meio:]

#     # Ordenar cada metade
#     esquerda = merge_sort(esquerda)
#     direita = merge_sort(direita)

#     # Combinar as metades ordenadas
#     return merge(esquerda, direita)

# def merge(esquerda, direita):
#     resultado = []
#     i = j = 0

#     # Comparar os elementos de ambas as metades e combinar de forma ordenada
#     while i < len(esquerda) and j < len(direita):
#         if esquerda[i] < direita[j]:
#             resultado.append(esquerda[i])
#             i += 1
#         else:
#             resultado.append(direita[j])
#             j += 1

#     # Adicionar os elementos restantes
#     resultado.extend(esquerda[i:])
#     resultado.extend(direita[j:])

#     return resultado

# # Exemplo de uso
# lista = [38, 27, 43, 3, 9, 82, 10]
# ordenada = merge_sort(lista)
# print("Lista ordenada:", ordenada)
# Explicação do Código
# Função merge_sort:

# Verifica se a lista tem um ou nenhum elemento (caso base), retornando a lista como está.
# Divide a lista ao meio.
# Chama recursivamente merge_sort para a metade esquerda e a metade direita.
# Combina as duas metades ordenadas usando a função merge.
# Função merge:

# Combina duas listas ordenadas (esquerda e direita) em uma única lista ordenada.
# Utiliza dois índices (i para a lista esquerda e j para a lista direita) para percorrer as listas.
# Adiciona o menor dos elementos atuais das duas listas à lista resultado.
# Adiciona os elementos restantes das listas esquerda e direita ao resultado após a comparação.
# Complexidade
# Complexidade de Tempo: O Merge Sort tem uma complexidade de tempo de O(nlogn) no pior, melhor e caso médio, onde n é o número de elementos na lista.
# Visualizando o Merge Sort
# https://www.youtube.com/watch?v=5Z9dn2WTg9o

# Demonstração do 'merge sort' (ordenação por mesclagem)
# O algoritmo de ordenação por mesclagem divide a lista em sublistas cada vez menores até que cada sublista tenha apenas um elemento. Em seguida, ele combina essas sublistas de volta em uma lista ordenada. Este processo é conhecido como dividir para conquistar.

# Exemplo: Lista inicial desordenada: [38, 27, 43, 3, 9, 82, 10]

# Passo 1 - Dividir a lista ao meio repetidamente até que cada sublista tenha um único elemento:

# Dividir [38, 27, 43, 3, 9, 82, 10] em [38, 27, 43] e [3, 9, 82, 10]
# Dividir [38, 27, 43] em [38] e [27, 43]
# Dividir [27, 43] em [27] e [43]
# Dividir [3, 9, 82, 10] em [3, 9] e [82, 10]
# Dividir [3, 9] em [3] e [9]
# Dividir [82, 10] em [82] e [10]
# Neste ponto, temos sublistas individuais: [38], [27], [43], [3], [9], [82], [10].

# Passo 2 - Combinar as sublistas ordenadas:

# Combinar [27] e [43] em [27, 43]
# Combinar [3] e [9] em [3, 9]
# Combinar [82] e [10] em [10, 82]
# Temos as sublistas: [38], [27, 43], [3, 9], [10, 82]

# Passo 3 - Continuar combinando:

# Combinar [38] e [27, 43] em [27, 38, 43]
# Combinar [3, 9] e [10, 82] em [3, 9, 10, 82]
# Temos as sublistas: [27, 38, 43] e [3, 9, 10, 82]

# Passo 4 - Combinar as sublistas finais:

# Combinar [27, 38, 43] e [3, 9, 10, 82] em [3, 9, 10, 27, 38, 43, 82]
# Após esses passos, a lista está completamente ordenada: [3, 9, 10, 27, 38, 43, 82]

# Explicação dos Passos
# Divisão:

# A lista é dividida repetidamente ao meio até que cada sublista tenha apenas um elemento. Esta é a etapa de dividir e conquistar.
# Combinação:

# As sublistas individuais são combinadas de volta em sublistas maiores e ordenadas. Neste processo, os elementos são comparados e organizados em ordem.
# Repetição do Processo:

# A combinação continua até que todas as sublistas sejam mescladas de volta em uma única lista ordenada.
# Observações
# A divisão da lista ao meio ocorre log2(n) vezes, onde n é o número de elementos na lista.
# A combinação das sublistas envolve comparar e mover elementos, o que leva n operações por nível de combinação.
# Portanto, a complexidade total do Merge Sort é O(nlogn), o que é mais eficiente do que muitos outros algoritmos de ordenação simples como o Bubble Sort.
# Visualizando o Merge Sort
# https://www.youtube.com/watch?v=5Z9dn2WTg9o

# Qual método de sort Python usa internamente?
# lista_desordenada = [5, 3, 1, 4, 2]
# lista_ordenada = sorted (lista_desordenada, reverse= False)
# print (lista_ordenada)
# Timsort is a hybrid, stable sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. It was implemented by Tim Peters in 2002 for use in the Python programming language.

# fonte wikipedia: https://en.wikipedia.org/wiki/Timsort