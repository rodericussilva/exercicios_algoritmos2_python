#Aula 22- Variáveis compostas exercícios (zip e dicionário de listas)
#1- Exercícios ZIP
#Exercício 1: Combinar Dados de Listas Paralelas
#Você tem duas listas, uma contendo os nomes de alunos e outra contendo suas notas finais. Crie uma lista de tuplas onde cada tupla contém o nome de um aluno e sua nota correspondente.

nomes = ['Ana', 'João', 'Clara', 'Marcos']
notas = [8.5, 7.0, 9.0, 6.5]
#nome_nota = zip(nomes, notas) #
nome_nota = list(zip(nomes, notas))

for nome in nome_nota:
  print(nome)
  
('Ana', 8.5)
('João', 7.0)
('Clara', 9.0)
('Marcos', 6.5)

#Exercício 2: Comparação de Listas
#Você tem uma lista de nomes de produtos e outra lista com os preços desses produtos. Utilize zip() para criar uma lista de produtos cujos preços estão abaixo de 10.0.

produtos = ['caneta', 'lápis', 'caderno', 'borracha']
precos = [1.5, 0.75, 12.0, 2.0]

produtoLista = []

for produto, preco in zip(produtos, precos):
  if preco < 10.0:
    produtoLista.append(produto)
print(produtoLista)
['caneta', 'lápis', 'borracha']

#Exercício 3: Criar um Dicionário a Partir de Duas Listas
#Dadas duas listas, uma com chaves e outra com valores, crie um dicionário combinando-as.

chaves = ['id', 'nome', 'idade']
valores = [1, 'Ana', 22]
dicKeys = dict(zip(chaves, valores))

print(dicKeys)
{'id': 1, 'nome': 'Ana', 'idade': 22}

#2- Exercícios Dicionário de listas
#Exercício 1: Identificar a Espécie com a Menor População
#Considere a lista de dicionário abaixo e descubra qual espécie listada tem a menor população e determine seu local.

especies_em_extincao = {
    'local': ["nordeste", "norte", "sul", "centro-oeste"],
    'especie': ["preá", "arara", "preguiça", "mico leão"],
    'quantidade_atual': [3000, 5000, 1500, 3200]
}


#Exercício 2: Calcular a Média da População das Espécies em Extinção
#Considere a lista de dicionário abaixo e calcule a média da população das espécies listadas.

especies_em_extincao = {
    'local': ["nordeste", "norte", "sul", "centro-oeste"],
    'especie': ["preá", "arara", "preguiça", "mico leão"],
    'quantidade_atual': [3000, 5000, 1500, 3200]
}

soma = sum(especies_em_extincao['quantidade_atual'])
media = soma / len(especies_em_extincao['quantidade_atual'])
print(media)

#Exercício 3: Listar Espécies com População Acima de um Limite Especificado
#Considere as variáveis lista de dicionário e limite abaixo e liste as espécies cuja população atual seja superior a 2500 indivíduos.

limite = 2500

especies_em_extincao = {
    'local': ["nordeste", "norte", "sul", "centro-oeste"],
    'especie': ["preá", "arara", "preguiça", "mico leão"],
    'quantidade_atual': [3000, 5000, 1500, 3200]
}

especie2500 = [especie for especie, quantidade in zip(especies_em_extincao['especie'], especies_em_extincao['quantidade_atual']) if quantidade > limite]
print(especie2500)

#Exercício 4: Relatório de Espécies em Risco
#Descrição do Problema: Use a estrutura iterativa para criar um relatório formatado que liste cada local junto com a espécie em risco e sua população atual (vide formato da saída abaixo). Este formato facilitará a leitura e pode ser usado para apresentações ou relatórios ambientais.

especies_em_extincao = {
    'local': ["nordeste", "norte", "sul", "centro-oeste"],
    'especie': ["preá", "arara", "preguiça", "mico leão"],
    'quantidade_atual': [3000, 5000, 1500, 3200]
}
# saída
#Relatórios de Espécies em extinção
#---------------------------------
#Local: nordeste - Espécie: preá - População: 3000
#Local: norte - Espécie: arara - População: 5000
#Local: sul - Espécie: preguiça - População: 1500
#Local: centro-oeste - Espécie: mico leão - População: 3200
#Solução em Python:

especies_em_extincao = {
    'local': ["nordeste", "norte", "sul", "centro-oeste"],
    'especie': ["preá", "arara", "preguiça", "mico leão"],
    'quantidade_atual': [3000, 5000, 1500, 3200]
}

print ('Relatórios de Espécies em extinção')
print ('----------------------------------')
for i in range(len(especies_em_extincao["local"])):
    dic_info = {chave: valor[i] for chave, valor in especies_em_extincao.items()}
    print(f"Local: {dic_info['local']} - Espécie: {dic_info['especie']} - População: {dic_info['quantidade_atual']}")
