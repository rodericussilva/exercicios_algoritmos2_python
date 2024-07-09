#Aula 3 - Exercícios em Sala de Aula

#Exercícios sobre estrutura de dados tipo String

#Exercício 1

#Criar uma variável chamada cultura que deverá conter o nome "Milho" e em seguida concatená-la com a palavra "Plantado" para formar a string "Milho Plantado".

cultura = "Milho"
resultado = cultura + " Plantado "
print(resultado)

#Exercício 2
#Criar uma variável chamada fruta com o valor "Laranja" e utilizar a função len() para encontrar o número de caracteres na string.

fruta = "Laranja"
tamanho = len(fruta)
print(tamanho)

#Exercício 3
#Criar uma variável chamada clima com o valor "Chuvoso" e transformá-la toda para letras maiúsculas.

clima = "Chuvoso"
resultado = clima.upper()
print(resultado)

#Exercício 4
#Criar uma string chamada solo com o valor "Solo Arenoso". Use o método replace() para trocar "Arenoso" por "Pedregoso".

solo = "Solo Arenoso"
solo = solo.replace("Arenoso", "Pedregoso")
print(solo)

#Exercício 5
#Criar uma variável chamada destino com o valor "Paris" e uma variável preco com o valor 1200. Use f-string para imprimir "A viagem para Paris custa 1200 dólares". Lembre-se que as f-strings são utilizadas para intercalar várias string.

destino = "Paris"
preco = 1200
print(f"A viagem para {destino} custa {preco} dólares")

#Exercício 6
#Neste exercício, você deve formatar o nome de um aluno e sua nota para exibição utilizando f-string.
# Formate o nome do aluno e sua nota usando f-string

nome = "Carlos"
nota = 89
resultado = f"O aluno {nome} obteve a nota {nota}."
print(resultado)

#Exercício 7
#Formate o nome da escola e sua localização utilizando f-string.

escola = "Escola Estadual João XXIII"
localizacao = "São Paulo"
info = f"A {escola} está localizada em {localizacao}."
print(info)

#Exercício 8
#Neste exercício, você deve encontrar a posição inicial do nome do imposto 'ISS'.

impostos = "ICMS, IPI, ISS, IOF"
posicao = impostos.find("ISS")
print(posicao)

#Exercício 9
#Neste exercício, você deve obter o ano contido na variável tipo string taxa. 

taxa = "IRRF2023"
ano_taxa = taxa[4:]
print(ano_taxa)

#Exercício 10
#Neste exercício, verifique se a string termina com o sufixo "2023".

declaracao = "Imposto de Renda 2023"
resultado = declaracao.startswith("2023")
print(resultado)