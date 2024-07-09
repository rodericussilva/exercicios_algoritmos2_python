# # Aula 30 - Analisar Eficiência de Algoritmos
# # Agenda
# # Notação Big O para análise de eficiência de algoritmos

# A notação Big O, também conhecida em português como "Grande O", é uma terminologia usada na ciência da computação e na matemática para descrever a complexidade de um algoritmo. Essencialmente, ela é uma forma de classificar algoritmos com base em quão rapidamente o tempo de execução ou espaço necessário cresce em relação ao tamanho da entrada de dados.

# Vamos considerar o seguinte exemplo
# Problema: Dados os dois algoritmos abaixo que calculam a soma dos n primeiros números. Qual dos dois é o melhor?
# Como analisar de forma objetiva qual o melhor de dois ou mais algoritmos para solucionar um mesmo problema?

# Duas formas de analisar o algoritmo:

# espaço em memória ocupado
# tempo de execução do algoritmo
# Neste curso iremos focar na análise de tempo.

# Problema: Calcular a soma os n primeiros números.
# para n = 5

# soma = 1 + 2 + 3 + 4 + 5 = 15

# Quais dos dois algoritmos abaixo é o mais eficiente (melhor tempo de execução)?

# Método 1:

#   n= 5
#   total_soma = 0
#   for i in range(1, n+1):
#      total_soma = total_soma + i
#   print (total_soma)
  
# Método 2:

#   n = 5
#   total_soma = n * (n + 1) / 2
#   print (total_soma)

# Problema: Calcular a soma os n primeiros números.
# Método 1: iterando sobre os números e acumulando a soma
# Solução sem medição de tempo
# Solução com medição de tempo

# para n = 5
# soma = 1 + 2 + 3 + 4 + 5 = 15

# def soma_metodo_1(n):
#   total_soma = 0
#   for i in range(1, n+1):
#      total_soma = total_soma + i
#   return n, total_soma

# n, soma = soma_metodo_1(10000)

# print(f"N={n}, Soma={soma}")
# [ ]
# #agora vamos medir o tempo do algoritmo pelo método 1 de soma

# import time

# def soma_metodo_1(n):
#   t_inicio = time.time()
#   total_soma = 0
#   for i in range(1, n+1):
#      total_soma = total_soma + i
#   t_fim = time.time()
#   return n, total_soma, (t_fim-t_inicio)

# n, soma, tempo = soma_metodo_1(10000)

# print(f"N={n}, Soma={soma}, Tempo={tempo}")

# Calcular a soma do n primeiros números
# Método 2 - Usando fórmula matemática
# Solução sem medição de tempo
# Solução com medição de tempo
# [ ]
# #método 2 de soma

# def soma_metodo_2 (n):
#   total_soma = n * (n + 1) / 2
#   return n, total_soma

# n, soma = soma_metodo_2(10000)

# print(f"N={n}, Soma={soma}")


# [ ]
# #Agora vamos medir o tempo do algoritmo de soma pelo método 2

# import time
# def soma_metodo_2 (n):
#   t_inicio = time.time()
#   total_soma = n * (n + 1) / 2
#   t_fim = time.time()
#   return n, total_soma, (t_fim-t_inicio)

# n, soma, tempo = soma_metodo_2(10000)

# print(f"N={n}, Soma={soma}, Tempo={tempo}")


# [ ]

# Commencez à coder ou à générer avec l'IA.
# Problemas com a medição de tempo
# Analisando a eficiência de um algoritmo com a biblioteca time há vários problemas.

# tempo varia na mesma máquina
# tempo varia entre máquinas
# tempo varia dependendo da linguagem de programação
# Veja a Demonstração rodando várias vezes

# [ ]
# import time
# def soma_metodo_1(n):
#   t_inicio = time.time()
#   total_soma = 0
#   for i in range(1, n+1):
#      total_soma = total_soma + i
#   t_fim = time.time()
#   return n, total_soma, (t_fim-t_inicio)

# n, soma, tempo = soma_metodo_1(10000)

# for i in range(5):
#   n, soma, tempo = soma_metodo_1(10000)
#   print(f"N={n}, Soma={soma}, Tempo={tempo}")
# Desafio
# Encontrar uma forma que possamos analisar a eficiência do algoritmo independente do tempo de execução do algoritmo que sabemos ser afetado por vários fatores para um mesmo algoritmo (tipo de máquina, linguagem de programação, estrutura do algoritmo, tipo de sistema operacional, etc)

# Solução
# Em vez de usar o tempo de execução como medida que tal se usássemos a quantidade de passos que o algoritmo usou para resolver o problema? Cada um desses passos seria considerado uma unidade básica de computação e o tempo de execução de uma algoritmo seria expresso pelo número de passos para resolver o problema e, portanto, dependeria de como o algoritmo foi implementado.

# Uma boa unidade básica de cálculo para comparar os algoritmos de soma mostrados anteriormente poderia ser contar o número de instruções de atribuição executadas:

# Método 2: Algoritmo de soma n números

# def soma_metodo_2 (n):
#   total_soma = n * (n + 1) / 2
#   return n, total_soma
# Na função acima soma_metodo_2(n), o número de instruções de atribuição é 1. Portanto T(n)=1 atribuição.

# Método 1: Algoritmo para somar n números

# def soma_metodo_1(n):
#   total_soma = 0
#   for i in range(1, n+1):
#      total_soma = total_soma + i
#   return n, total_soma
# Na função soma_metodo_1(n), o número de instruções de atribuição é 1 (total_soma =0) mais o valor de n (o número de vezes que realizamos total_soma = total_soma +1). Podemos denotar isso por uma função, chamada T, onde T(n) = 1+ n. O parâmetro n é frequentemente referido como o “tamanho do problema”, e podemos ler isso como “T(n) é o tempo necessário para resolver um problema de tamanho n, ou seja, 1+n passos.

# Notação Big O
# Os cientistas da computação preferem levar esta técnica de análise um passo adiante. Acontece que o número exato de operações não é tão importante quanto determinar a parte mais dominante da função. Em outras palavras, à medida que o problema se torna maior, alguma parte da função T(n) tende a dominar o resto. Esse termo dominante é o que, no final das contas, é usado para comparação. A ordem de grandeza (magnitude) da função descreve a parte que T(n) que aumenta mais rapidamente à medida que o valor de n aumenta. A ordem de grandeza é frequentemente chamada de notação Big-O (“ordem”) e escrita como O(f(n)). Essa notação permite termos uma aproximação útil para o número real de etapas do algoritmo ou o esforço de computação para processar. A função f(n) fornece uma representação simples da parte dominante do original T(n).

# No exemplo acima, T(n) = 1 + n. À medida que n aumenta, a constante 1 se torna cada vez menos significativa para o resultado final. Se estivermos procurando uma aproximação para T(n), então podemos eliminar 1 e simplesmente dizer que o tempo de execução é O(n). É importante notar que o 1 é certamente significativo para T(n). No entanto, à medida que n aumenta, nossa aproximação será igualmente precisa sem ele.

# Como outro exemplo, suponha que para algum algoritmo, o número exato de etapas seja T(n)=5n2+27n+1005. Quando n é pequeno, digamos 1 ou 2, a constante 1005 parece ser a parte dominante da função. No entanto, à medida que n aumenta, o termo n2 se torna o mais importante. Na verdade, quando n é realmente grande, os outros dois termos tornam-se insignificantes em relação ao resultado final da função. Novamente, para aproximar T(n) à medida que n aumenta, podemos ignorar os outros termos e focar em 5n2. Além disso, o coeficiente 5 também torna-se insignificante à medida que n aumenta. Diríamos então que a função T(n) tem uma ordem de grandeza f(n)=n2, ou simplesmente que é O(n2).

# Embora não vejamos isso no exemplo da soma, às vezes o desempenho de um algoritmo depende dos valores exatos dos dados e não simplesmente do tamanho do problema. Para esses tipos de algoritmos, precisamos caracterizar seu desempenho em termos de melhor caso, pior caso ou desempenho médio. O pior caso de desempenho refere-se a um conjunto de dados específico onde o algoritmo tem um desempenho especialmente ruim. Considerando que um conjunto de dados diferente para exatamente o mesmo algoritmo pode ter um desempenho extraordinariamente bom. No entanto, na maioria dos casos, o algoritmo funciona em algum lugar entre esses dois extremos (caso médio). É importante que um cientista da computação compreenda essas distinções para que não seja enganado por um caso específico.

# Uma série de funções de ordem de magnitude muito comuns surgirão continuamente à medida que você estuda algoritmos. Estas são mostradas na Tabela 1. Para decidir qual dessas funções é a parte dominante de qualquer função, devemos ver como eles se comparam à medida que n aumenta.

# f(n)	Name
# 1	Constant
# logn	Logarithmic
# n	Linear
# nlogn	Log Linear
# n2	Quadratic
# n3	Cubic
# 2n	Exponential
# imagem_1.png

# Exemplo
# Como exemplo, suponha que temos o fragmento de código Python abaixo. Embora esse programa não faça nada, é instrutivo ver como podemos pegar o código real e analisar o desempenho usando a metodologia BIG O.

# [ ]
# a = 5
# b = 6
# c = 10
# for i in range(n):
#  for j in range(n):
#   x = i * i
#   y = j * j
#   z = i * j
# for k in range(n):
#   w = a * k + 45
#   v = b * b
# d = 33
# O número de operações de atribuição é a soma de quatro termos. O primeiro termo é a constante 3, representando as três instruções de atribuição no início do fragmento. O segundo termo é 3n2, uma vez que existem três instruções que são executadas n2 vezes devido à iteração aninhada. O terceiro termo é 2n , duas instruções iteradas n vezes. Finalmente, o quarto termo é a constante 1, representando a declaração de atribuição final. Isso nos dá T(n)=3+3n2+2n+1=3n2+2n+4. Olhando para os expoentes, podemos ver facilmente que o termo n2 será dominante e, portanto, este fragmento de código é O(n2). Observe que todos os outros termos, bem como o coeficiente do termo dominante, podem ser ignorados à medida que n aumenta.

# imagem_2.png

# [ ]

# Commencez à coder ou à générer avec l'IA.
# [ ]

# Commencez à coder ou à générer avec l'IA.
# Double-cliquez (ou appuyez sur Entrée) pour modifier

# Estudo de caso
# Considere o problema de calcular o menor número em uma lista. Podemos resolver esse problema utilizando duas abordagens:

# A primeira função compara cada número com os outros números da lista para achar o menor. Esse método tem complexidade quadrática O(n2).

# A segunda função também calcula o mínimo usando outro método e tem complexidade linear O(n).

# A seguir vamos analisar as complexidades dos dois algoritmos:

# 1. Função com complexidade quadrática O(n2):
# [ ]
# def find_min_quadratic(numbers):

#     min_num = numbers[0]  # Supor o primeiro número da lista como o menor

#     # Iterar sobre cada elemento da lista
#     for num in numbers:
#         is_min = True
#         # Compare o número atual com todos os outros números da lista
#         for other_num in numbers:
#             if num > other_num:
#                 is_min = False
#                 break  # Saia do loop mais cedo se um número menor for encontrado
#         if is_min:
#             min_num = num  # Atualize o número mínimo se um número menor for encontrado
#     return min_num

# lista = [10,9,3,1,4,8]

# print (find_min_quadratic(lista))
# Análise da Eficiência do Algoritmo em termos de sua complexidade:
# Para analisar a complexidade de tempo do algoritmo fornecido acima, vamos examinar cada parte do código e determinar quantas operações são realizadas em termos de n, onde n é o número de elementos na lista numbers.

# Inicialização da variável min_num:

#  min_num = numbers[0]
# Esta linha de código é uma operação de tempo constante, O(1).

# Primeiro laço for (iterar por cada número na lista):

#  for num in numbers:
# Este laço será executado n vezes, onde n é o número de elementos em numbers.

# Segundo laço for (comparar o número atual com cada outro número na lista):

#  for other_num in numbers:
# Este laço aninhado também será executado n vezes para cada iteração do primeiro laço.

# Operações dentro do segundo laço for:

#  if num > other_num:
#      is_min = False
#      break
# As operações dentro do segundo laço são de tempo constante, O(1). No pior caso, o if e o break são executados n vezes para cada iteração do primeiro laço.

# Atribuição condicional fora do segundo laço for:

#  if is_min:
#      min_num = num
# Esta atribuição condicional também é de tempo constante, O(1), mas ocorre n vezes devido ao primeiro laço.

# Complexidade Total

# A complexidade total de tempo é O(1)+O(1)∗O(n)+O(1)∗O(n)∗O(n)+O(1)∗O(n)=O(1)+O(n∗1)+O(n2∗1)=O(n2+n+1)=O(n2)

# Portanto, a complexidade é determinada pelo comportamento do laço aninhado. Para cada iteração do primeiro laço (que é O(n)), o segundo laço também executa n vezes. Portanto, a complexidade de tempo total do algoritmo é O(n) vezes O(n) = O(n2).

# Resumo:

# A complexidade de tempo do algoritmo fornecido é O(n2).

# 2. Função com complexidade linear O(n)
# [ ]
# def find_min_linear(numbers):

#     min_num = numbers[0]  # Supor o primeiro número da lista como o menor

#     # Iterar cada número da lista começando no segundo elemento
#     for num in numbers[1:]:
#         if num < min_num:
#             min_num = num  # Atualize o número mínimo se um número menor for encontrado
#     return min_num

# lista = [10,9,3,1,4,8]

# print (find_min_linear(lista))
# Análise:
# Para analisar a complexidade de tempo do algoritmo fornecido acima, vamos examinar cada parte do código e determinar quantas operações são realizadas em termos de n, onde n é o número de elementos na lista numbers.

# Inicialização da variável min_num:

#  min_num = numbers[0]
# Esta linha de código é uma operação de tempo constante, O(1).

# Laço for (iterar por cada número na lista a partir do segundo elemento):

#  for num in numbers[1:]:
# Este laço será executado n−1 vezes, onde n é o número de elementos em numbers. No entanto, para fins de análise de complexidade, consideramos n−1 como n, já que a constante não afeta a complexidade assintótica.

# Operação condicional dentro do laço for:

#  if num < min_num:
#      min_num = num
# A operação condicional e a possível atribuição dentro do laço são de tempo constante, O(1). Essas operações são executadas n−1 vezes. No entanto, para fins de análise de complexidade, consideramos n−1 como n, já que a constante não afeta a complexidade assintótica.

# Complexidade Total

# A complexidade total de tempo do algoritmo é O(1)+O(n) * O(1)=O(n+1)=O(n).

# Portanto, a complexidade é determinada pelo comportamento do laço. Para cada iteração do laço (que é O(n)), executamos operações de tempo constante O(1).

# Resumo:

# A complexidade de tempo do algoritmo fornecido é O(n).

# Apêndice
# Explicação da função logarítmica
# A função logarítmica, frequentemente referida como logn na análise de complexidade de algoritmos, é crucial para entender como certos algoritmos ou operações escalam com o aumento do tamanho da entrada, n. Para tornar essa explicação mais acessível, vamos começar com uma breve revisão de como a função logarítmica se comporta e, em seguida, explicar seu papel em problemas de Big O.

# O que é logn?
# A função logarítmica, especificamente logb (logaritmo de n na base b, indica quantas vezes você precisa multiplicar a base b por si mesma para obter n. Por exemplo, log28=3 porque 23=8.

# No contexto de ciência da computação, quando a base não é especificada, geralmente assume-se a base 2. Portanto, logn geralmente implica log2n.

# Logaritmos em Análise de Complexidade (Big O)
# Exemplo: Divisão por Dois
# Considere um algoritmo que divide repetidamente um número n por 2 até que n seja menor ou igual a 1. Quantas divisões são necessárias? Como já mencionado, essa é uma situação onde você precisa do logaritmo de n na base 2 para determinar o número de divisões, ou seja, log2n. Se n=1024, então log21024=10, o que significa que 10 divisões são necessárias.

# Algoritmos de Pesquisa Binária
# Outro exemplo clássico é a pesquisa binária em uma lista ordenada. A pesquisa binária localiza o item desejado ao dividir repetidamente a lista pela metade. Se a lista tiver 1024 elementos, a pesquisa binária pode encontrar qualquer item em no máximo 10 passos log21024=10. A cada passo, a metade da lista onde o item não pode estar é eliminada, reduzindo significativamente o espaço de pesquisa.

# Estruturas de Dados Balanceadas
# Estruturas como árvores binárias de busca balanceadas (como AVL ou árvores vermelho-preto) mantêm suas alturas limitadas a logn, onde n é o número de elementos na árvore. Isso significa que operações como busca, inserção e exclusão podem ser realizadas em tempo logarítmico, logn, tornando essas operações eficientes mesmo para grandes volumes de dados.

# Complexidade de Algoritmos
# Quando um algoritmo tem uma complexidade de tempo (O(logn), isso indica que o tempo necessário para executar o algoritmo aumenta muito lentamente à medida que o tamanho da entrada n aumenta. Isso é particularmente poderoso em contextos onde n pode se tornar extremamente grande, pois o aumento do tempo de execução é mantido a um ritmo muito controlado.

# Conclusão
# O logaritmo, em análise de complexidade, reflete algoritmos e operações que dividem o problema em partes cada vez menores, geralmente pela metade, a cada passo. Esta é uma característica de eficiência que faz com que logn seja uma métrica desejada para a complexidade do tempo de execução, especialmente em comparação com complexidades lineares, quadráticas ou exponenciais.

# n	logn atribuições	n atribuições	n2atribuições
# 1	0	1	1
# 2	1	2	4
# 4	2	4	16
# 8	3	8	64
# 16	4	16	256
# 32	5	32	1024
# 64	6	64	4096
# 128	7	128	16384
# 256	8	256	65536
# 512	9	512	262144
# 1024	10	1024	1048576
# 2048	11	2048	4194304
# 4096	12	4096	16777216
# 8192	13	8192	67108864
# 16384	14	16384	268435456
# 32768	15	32768	1073741824
# 65536	16	65536	4294967296
