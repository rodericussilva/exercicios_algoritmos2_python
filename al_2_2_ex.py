#Aula 2 - Exercícios

#Exercício 1
#Neste exercício, você deve criar uma variável chamada salario e permitir que o usuário insira o valor do salário de um funcionário. Em seguida, crie uma variável chamada aumento e permita que o usuário insira o valor do aumento percentual que o funcionário receberá. Por fim, calcule e imprima o novo salário do funcionário.

#Obs: o percentual de aumento a ser inserido no formato percentual.Ex: 10 para representar 10%. Lembre-se que o separador decimal no python é o ponto.

salario = float(input("Digite o salário do funcionário: "))
aumento = float(input("Digite o aumento percentual do funcionário: "))
novo_salario = salario * (1 + aumento / 100)
print("O novo salário do funcionário é R$",novo_salario)

#Exercício 2
#Neste exercício, você deve criar uma variável chamada horas_trabalhadas e permitir que o usuário insira o número de horas trabalhadas por um funcionário em um mês. Em seguida, crie uma variável chamada valor_hora e permita que o usuário insira o valor da hora trabalhada. Por fim, calcule e imprima o salário bruto do funcionário.

horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))
salario_bruto = horas_trabalhadas * valor_hora
print("O salário bruto do funcionário é R$", salario_bruto)

#Exercício 3
#Neste exercício, você deve criar uma variável chamada nota1 e atribuir a ela a nota da primeira avaliação de um aluno. Em seguida, crie uma variável chamada nota2 e atribua a ela a nota da segunda avaliação do mesmo aluno. Por fim, calcule e imprima a média final do aluno.

nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
media = (nota1 + nota2) / 2
print("A média final do aluno é ",media)

#Exercício 4
#Neste exercício, você deve criar uma variável chamada alunos e atribuir a ela o número total de alunos em uma turma. Em seguida, crie uma variável chamada aprovados e atribua a ela o número de alunos aprovados na turma. Por fim, calcule e imprima a porcentagem de alunos aprovados na turma.

alunos = int(input("Informe o número de alunos: "))
aprovados = int(input("Agora informe o número de aprovados: "))
porCent = (aprovados * 100) / alunos
print(f"Foram aprovados {porCent:.2f}% da turma")

#Exercício 5
#Neste exercício, você deve criar uma variável chamada peso e atribuir a ela o peso de uma pessoa em quilogramas. Em seguida, crie uma variável chamada altura e atribua a ela a altura da mesma pessoa em metros. Por fim, calcule e imprima o índice de massa corporal (IMC) da pessoa.

peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))
imc = peso / (altura*2)
print(f"O IMC é {imc:.2f}")

#Exercício 6
#Neste exercício, você deve criar uma variável chamada batimentos e atribuir a ela o número de batimentos cardíacos de uma pessoa em um minuto. Em seguida, crie uma variável chamada idade e atribua a ela a idade da mesma pessoa. Por fim, calcule e imprima a frequência cardíaca máxima da pessoa.

batimentos = int(input("Informe o número de batimentos cardiácos/minuto: "))
idade = int(input("Informe a idade: "))
freq = batimentos * idade
print("A frequencia maxima é:", freq)