# Aula 18 - Exercícios em Sala de Aula
# Exercícios sobre lista de dicionários

# Exercício 1

# Dada lista de dicionários abaixo representando análises de sentimentos, seu objetivo é atualizar o score do segundo dicionário para 0.55. Em seguida, imprima o dicionário atualizado.

sentimentos = [
    {'label': 'POSITIVE', 'score': 0.9998704195022583},
    {'label': 'NEGATIVE', 'score': 0.9988259673118591},
    {'label': 'POSITIVE', 'score': 0.9998812675476074},
    {'label': 'POSITIVE', 'score': 0.9998786449432373},
    {'label': 'POSITIVE', 'score': 0.9996154308319092}
]

for sentimento in sentimentos:
    if sentimento['score'] == 0.9988259673118591:
        sentimento['score'] = 0.55
print(sentimentos)

#ou

sentimentos = [
    {'label': 'POSITIVE', 'score': 0.9998704195022583},
    {'label': 'NEGATIVE', 'score': 0.9988259673118591},
    {'label': 'POSITIVE', 'score': 0.9998812675476074},
    {'label': 'POSITIVE', 'score': 0.9998786449432373},
    {'label': 'POSITIVE', 'score': 0.9996154308319092}
]

sentimentos[1]['score'] = 0.55
print(sentimentos)

#Exercício 2
#A partir da mesma lista sentimentos, você deve adicionar um novo dicionário ao final da lista com os seguintes dados: {'label': 'NEUTRO', 'score': 0.75}. Em seguida, exclua o primeiro dicionário da lista. Por fim, imprima a lista modificada.

sentimentos = [
    {'label': 'POSITIVE', 'score': 0.9998704195022583},
    {'label': 'NEGATIVE', 'score': 0.9988259673118591},
    {'label': 'POSITIVE', 'score': 0.9998812675476074},
    {'label': 'POSITIVE', 'score': 0.9998786449432373},
    {'label': 'POSITIVE', 'score': 0.9996154308319092}
]

sentimentos.append({'label': 'NEUTRO', 'score': 0.75})

sentimentos.remove({'label': 'POSITIVE', 'score': 0.9998704195022583})
print(sentimentos)
#ou
for sentimento in sentimentos:
    if sentimento['score'] == 0.9998704195022583:
        sentimentos.remove(sentimento)
        
print(sentimentos)

#Exercício 3
#Dadas duas listas de dicionários lista_a e lista_b:

lista_a = [{'label': 'POSITIVE', 'score': 0.9999},
           {'label': 'NEGATIVE', 'score': 0.9988}]

lista_b = [{'label': 'NEUTRAL', 'score': 0.7777},
           {'label': 'POSITIVE', 'score': 0.8888}]

#Você deve concatenar lista_b ao final de lista_a, formando uma única lista. Em seguida, exclua o par chave/valor 'score' do primeiro dicionário da lista resultante. Imprima a lista final.

lista_a.extend(lista_b)
del(lista_a[0]['score'])
print(lista_a)
#ou
for lista in lista_a:
    if lista['score'] == 0.9999:
        del(lista['score'])
print(lista_a)


# Exercício 4
# Dado uma lista de dicionários lista_original, cada dicionário contendo uma chave 'label' e uma chave 'score', o objetivo é adicionar uma nova chave 'score_arredondado' em cada dicionário, com o valor da chave 'score' arredondado com duas casas decimais.

# Lista de dicionários original
lista_original = [
    {'label': 'POSITIVE', 'score': 0.9998704195022583},
    {'label': 'NEGATIVE', 'score': 0.9988259673118591},
    {'label': 'POSITIVE', 'score': 0.9998812675476074},
    {'label': 'POSITIVE', 'score': 0.9998786449432373},
    {'label': 'POSITIVE', 'score': 0.9996154308319092}
]

# Sintaxe da função round():

# round(numero, ndigits)
# numero: O número que será arredondado.
# ndigits: O número de dígitos decimais para o qual você deseja arredondar.

for lista in lista_original:
    lista['score.arredondado'] = round(lista['score'], 2)
print(lista_original)

#Exercício 5
#Dada a lista de dicionário abaixo, você precisa remover todos os dicionários da lista em que a chave 'score' tenha um valor menor que 0.999.

# Lista de dicionários
lista_de_alunos = [
    {'label': 'POSITIVE', 'score': 0.9998704195022583},
    {'label': 'NEGATIVE', 'score': 0.9988259673118591},
    {'label': 'POSITIVE', 'score': 0.9998812675476074},
    {'label': 'POSITIVE', 'score': 0.9998786449432373},
    {'label': 'POSITIVE', 'score': 0.9996154308319092}
]

for lista in lista_de_alunos:
    if lista['score'] < 0.999:
        del(lista['score'])
print(lista_de_alunos)

#Exercício 6
#Dada a lista de dicionários produtos representando diferentes itens em estoque, cada um com um nome, categoria e quantidade em estoque, escreva um programa que itere sobre a lista e imprima os nomes dos produtos que são da categoria "eletrônicos" e têm mais de 10 unidades em estoque.

produtos = [
    {'nome': 'Laptop', 'categoria': 'eletrônicos', 'quantidade': 5},
    {'nome': 'Smartphone', 'categoria': 'eletrônicos', 'quantidade': 15},
    {'nome': 'Frigideira', 'categoria': 'utensílios domésticos', 'quantidade': 7},
    {'nome': 'Tablet', 'categoria': 'eletrônicos', 'quantidade': 12}
]

for produto in produtos:
    if produto['categoria'] == 'eletrônicos' and produto['quantidade'] > 10:
        print(produto['nome']) #imprime somente o nome
        #print(produto) imprime a lista na condição

#Exercício 7
#Considere uma lista de dicionários alunos onde cada dicionário contém o nome do aluno e sua nota. Escreva um programa que incremente em 10% as notas dos alunos que tenham nota inferior a 7, e então imprima a lista atualizada.

alunos = [
    {'nome': 'Ana', 'nota': 8.5},
    {'nome': 'João', 'nota': 6.4},
    {'nome': 'Mariana', 'nota': 5.7},
    {'nome': 'Pedro', 'nota': 9.0},
    {'nome': 'Julia', 'nota': 6.8}
]

for aluno in alunos:
    if aluno['nota'] < 7.0:
        aluno['nota'] *= 1.1
print(alunos)
        
#Exercício 8
#A partir de uma lista de dicionários itens que representam compras realizadas em uma loja, onde cada item tem uma categoria e um valor, escreva um programa que itere sobre a lista e crie um novo dicionário onde as chaves são as categorias e os valores são a soma dos valores de itens dessa categoria. Por fim, imprima o dicionário resultante.

itens = [
    {'categoria': 'eletrônicos', 'valor': 1200},
    {'categoria': 'vestuário', 'valor': 200},
    {'categoria': 'eletrônicos', 'valor': 600},
    {'categoria': 'alimentos', 'valor': 50},
    {'categoria': 'vestuário', 'valor': 150}
]

