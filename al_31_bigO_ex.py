#Aula 31 - Analisar Eficiência de Algoritmos

#Exercícios:
#Exercício 1:
#Dado o seguinte fragmento de código, qual é o Big-O (ordem de grandeza) do tempo de execução? Explique por que.

n = 10
test = 0
for i in range(n):
   for j in range(n):
      test = test + i * j
A. O(n)

B. O(n2)

C. O(logn)

D. O(n3)

# O(1)+O(1)+ O(n)vezes O(n)vezes O(1)=O(n2) 
#A complexidade de tempo do algoritmo fornecido é  O(n2) item B

#Exercício 2:
#Dado o seguinte fragmento de código, qual é o Big-O (ordem de grandeza) do tempo de execução? Explique por que.

n = 10
test = 0
for i in range(n):
   test = test + 1

for j in range(n):
   test = test - 1

A. O(n)

B. O(n2)

C. O(logn)

D. O(n3)

# O(1)+O(1)+O(n)+O(n)=O(2n)=O(n)
# A complexidade de tempo do algoritmo fornecido é  O(n) item A

#Exercício 3:
# Dado o seguinte fragmento de código, qual é o Big-O (ordem de grandeza) do tempo de execução? Explique por que.

n = 8
i = n
while i > 1:
   k = 2 + 2
   i = i // 2

A. O(n)

B. O(n2)

C. O(logn)

D. O(n3)

# 2∗O(1)+2∗O(1)∗O(logn)=O(2+2∗logn)=O(Logn) 
# a complexidade do algoritmo é  O(logn)

#Exercício 4:
#Dado o seguinte fragmento de código, qual é o Big-O (ordem de grandeza) do tempo de execução? Explique por que.

n = 8
i = n
w = 0
while i > 1:
    for j in range(n):  
        w = w + 1
    k = 2 + 2
    i = i // 2

A. O(n)

B. O(n2)

C. O(logn)

D. O(n3)

# 3∗O(1)+O(1)∗O(n)∗O(logn)+2∗O(1)∗O(logn)=O(3+n∗logn+2∗logn)=O(n∗logn)
# a complexidade do algoritmo é  O(nlogn) item C

# Exercício 5:
# Dado o seguinte fragmento de código, qual é o Big-O (ordem de grandeza) do tempo de execução? Explique por que.

n = 10
for i in range(n):
   for j in range(n):
      for k in range(n):
         k = 2 + 2

A. O(n)

B. O(n2)

C. O(logn)

D. O(n3)

# O(1)  +  O(n)  vezes  O(n)  vezes  O(n)  vezes  O(1)=O(n3)
# A complexidade de tempo do algoritmo fornecido é  O(n3) item D

# Exercício 6:
# Dado o seguinte fragmento de código, qual é o Big-O (ordem de grandeza) do tempo de execução? Explique por que.

n = 10
for i in range(n):
   k = 2 + 2
for j in range(n):
   k = 2 + 2
for k in range(n):
   k = 2 + 2

A. O(n)

B. O(n2)

C. O(logn)

D. O(n3)

# O(n)+O(n)+O(n)=O(3n)
# A complexidade de tempo do algoritmo fornecido é  O(n) item A