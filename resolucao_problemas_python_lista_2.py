# Exercicio 1

# A nota final de um estudante é calculada a partir de três notas atribuídas respectivamente a um trabalho de laboratório. a uma avaliação semestral e a um exame final. A média das três nota mencionadas anteriormente obedece aos pesos a seguir:
# Trabalho de laboratório = 2
# Avaliação semestral = 3
# Exame final = 5
# Faça um programa que receba as três notas. calcule e mostre a média ponderada e o conceito que segue a tabela abaixo:
# 8 a 10 = A
# 7 a 8 = B
# 6 a 7 = C
# 5 a 6 = D
# 0 a 5 = E

trabalhoLab = float(input('Digite a 1ª nota do aluno: '))
avaliacaoSemestral = float(input('Digite a 2ª nota do aluno: '))
exameFinal = float(input('Digite a 3ª nota do aluno: '))
peso1 = 2
peso2 = 3
peso3 = 5
somaPesos = peso1 + peso2 + peso3

media = ((trabalhoLab * peso1) + (avaliacaoSemestral * peso2) + (exameFinal * peso3)) / somaPesos
print(f'Média: {media}')

if media >= 8 and media <= 10:
  print('Conceito A')

elif media >= 7 and media < 8:
  print('Conceito B')

elif media >= 6 and media < 7:
  print('Conceito C')

elif media >= 5 and media < 6:
  print('Conceito D')

elif media >= 0 and media < 5:
  print('Conceito E')

else:
  print('Valor inválido')

#---------------------------------------------------------------------------------------------------------

# Exercicio 3
# Faça um programa que receba dois números e mostre o maior.

num1 = int(input('Digite o 1ª número: '))
num2 = int(input('Digite o 2ª número: '))

if num1 > num2:
  print(f'O {num1} é maior que o {num2}')

elif num2 > num1:
  print(f'O {num2} é maior que o {num1}')

else:
  print(f'Os números são iguais')

#---------------------------------------------------------------------------------------------------------

# Exercício 4
# Faça um programa que receba três números e mostre-os em ordem crescente.

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

if num1 > num2 and num1 > num3:
     if num2 > num3:
          print(num3, num2, num1)
     else:
          print(num2, num3, num1)

elif num2 > num1 and num2 > num3:
     if num1 > num3:
          print(num3, num1, num2)
     else:
          print(num1, num3, num2)

else:
     if num1 > num2:
          print(num2, num1, num3)
     else:
          print(num1, num2, num3)

#---------------------------------------------------------------------------------------------------------

# Exercício 6
# Faça um programa que receba um número inteiro e verifique se esse número é par ou ímpar

numero = int(input('Digite para verificar se é par ou impar : '))

if numero % 2 == 0:
  print(f'O número {numero} é par')
else:
  print(f'O número {numero} é impar')

#---------------------------------------------------------------------------------------------------------

# Exercício 12
# Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu salário atual e mostre o novo salário. O s cargos estão na tabela a seguir.
# Codigo = 1 -- Cargo = escrituário -- 50%
# Codigo = 2 -- Cargo = Secretário -- 35%
# Codigo = 3 -- Cargo = Caixa -- 20%
# Codigo = 4 -- Cargo = Gerente -- 10%
# Codigo = 5 -- Cargo = Diretor -- não tem aumento

codigo = int(input('Digite o número correspondente ao cargo: '))
salario = float(input('Digite seu salário atual: '))

if codigo >= 1 and codigo <= 5:
    if codigo == 1:
      cargo = 'Escrituário'
      valorAumento = salario * 0.5
    elif codigo == 2:
      cargo = 'Secretário'
      valorAumento = salario * 0.35
    elif codigo == 3:
      cargo = 'Caixa'
      valorAumento = salario * 0.2
    elif codigo == 4:
      cargo = 'Gerente'
      valorAumento = salario * 0.1
    elif codigo == 5:
      cargo = 'Diretor'
else:
  print('Código inválido!')

salarioTotal = salario + valorAumento

if codigo >= 1 and codigo <= 5:
    if codigo >= 1 and codigo <= 4:
        print(f'Seu cargo é de {cargo}, você terá um aumento de R$ {valorAumento:.2f} e seu salário total será de: R$ {salarioTotal:.2f}')
    elif codigo == 5:
        print(f'Seu cargo é de {cargo}, você não terá aumento e seu salário permanece no valor de: R$ {salario:.2f}')
else:
  print('Código inválido!')

#------------------------------------------------------------------------------------------------------------

# Exercício 13
# Faça um programa que apresente o menu de opções a seguir. permita ao usuário escolher a opçäo desejada, receba os dados necessários para executar a operação e mostre o resultado. Verifique a possibilidade de opção invàlida.

opcao = int(input('*** MENU *** \n\n1. Imposto\n2. Novo Salário\n3. Classificação\n\nDigite a opção desejada: '))
salarioAtual = float(input('Digite seu salário atual: '))

if opcao >= 1 and opcao <= 3 and salarioAtual >= 0:

    if opcao == 1:
        if salarioAtual < 500:
          imposto = salarioAtual * 0.05

        elif salarioAtual >= 500 and salarioAtual < 850:
          imposto = salarioAtual * 0.1

        else:
          imposto = salarioAtual * 0.15

        print(f'Valor do imposto: R$ {imposto:.2f}')

    if opcao == 2:
        if salarioAtual < 450:
          salarioTotal = salarioAtual + 100

        elif salarioAtual >= 450 and salarioAtual < 750:
          salarioTotal = salarioAtual + 75

        elif salarioAtual >= 750 and salarioAtual < 1500:
          salarioTotal = salarioAtual + 50

        else:
          salarioTotal = salarioAtual + 25

        print(f'O valor do seu novo salário será de: R$ {salarioTotal:.2f}')

    if opcao == 3:
        if salarioAtual < 700:
          classificacao = 'Mal remunerado'
        else:
          classificacao = 'Bem remunerado'

        print(f'Classificação: {classificacao}')
else:
  print('valor inválido')

#------------------------------------------------------------------------------------------------------------

# Exercício 14
# Menu de opções:
# 1. Imposto
# 2. Novo salário
# 3. Classificação
# Digite a opção desejada.

# Na opção 1: receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as regras a seguir:
# Salário menor que R$ 500,00  -- Percentual imposto = 5%
# Salário de R$ 500,00 a R$ 850,00  -- Percentual imposto = 10%
# Salário acima de R$ 850,00  -- Percentual imposto = 15%



salarioF = float(input('Digite o salário: '))

if salarioF < 500:
  bonificacao = salarioF * 0.05

elif salarioF >= 500 and salarioF < 1200:
  bonificacao = salarioF * 0.12
else:
  bonificacao = 0

salarioAtual = salarioF + bonificacao

if salarioF < 600:
  auxilioEscola = 150
  salarioAtual += auxilioEscola
else:
  auxilioEscola = 100
  salarioAtual += auxilioEscola

print(f'Seu salário total com beneficios será de: {salarioAtual} ')

#------------------------------------------------------------------------------------------------------------

# exercício 15

salarioMin = float(input('Valor do salário minimo: '))
horasTrab = float(input('Quantidade de horas trabalhadas: '))
quantDependentes = int(input('Quantidade de dependentes: '))
horasExtra = float(input('Quantidade de horas extras: '))

valorHoraTrab = salarioMin / 5
salarioMes = horasTrab * valorHoraTrab
valorDependentes = quantDependentes * 32
valorHoraExtra = valorHoraTrab + (valorHoraTrab * 0.5)
salarioBruto = salarioMes + valorDependentes + (valorHoraExtra * horasExtra)

if salarioBruto < 200:
  imposto = 0
  print('Isento do imposto de renda')
elif salarioBruto >= 200 and salarioBruto < 500:
  imposto = salarioBruto * 0.1
else:
  imposto = salarioBruto * 0.2

salarioLiquido = salarioBruto - imposto

if salarioLiquido < 350:
  gratificacao = 100
else:
  gratificacao = 50

salarioReceber = salarioLiquido + gratificacao

print(f'O valor do salário a receber mais beneficios será de: {salarioReceber}')

#------------------------------------------------------------------------------------------------------------

# Exercício 16

precoAtual = float(input('Preço atual do produto: '))
vendaMediaMes = float(input('Venda mensal média do produto: '))


if precoAtual < 30 and vendaMediaMes < 500:
  reajuste = precoAtual + (precoAtual * 0.1)

elif precoAtual >= 30 and precoAtual < 80 and vendaMediaMes >= 500 and vendaMediaMes < 1200:
  reajuste = precoAtual + (precoAtual * 0.15)

elif precoAtual >= 80 and vendaMediaMes >= 1200:
  reajuste = precoAtual - (precoAtual * 0.2)


print(f'O preço atualizado do produto será: {reajuste}')

#------------------------------------------------------------------------------------------------------------

# Exercício 19

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

if altura < 1.20:
  if peso < 60:
    classificacao = 'A'
  elif peso >= 60 and peso < 90:
    classificacao = 'D'
  else:
    classificacao = 'G'

if altura >= 1.20 and altura < 1.70:
  if peso < 60:
    classificacao = 'B'
  elif  peso >= 60 and peso < 90:
    classificacao = 'E'
  else:
    classificacao = 'H'

if altura >= 1.70:
  if peso < 60:
    classificacao = 'C'
  elif peso >= 60 and peso < 90:
    classificacao = 'F'
  else:
    classificacao = 'i'

print(f'Sua classificação em relação ao seu peso e altura é: {classificacao}')