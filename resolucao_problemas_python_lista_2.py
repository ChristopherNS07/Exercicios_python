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

#------------------------------------------------------------------------------------------------------------

# Exercício 22
# Faça um programa que receba o código, o salário-base e o tempo de serviço de um funcionário. Calcule e mostre.

# O imposto que está na tabela a seguir 
# Se salário-Base menor que R$ 200,00 -- isento de imposto
# Se está entre R$ 200,00 e R$ 450,00 -- 3%
# Se está entre R$ 451,01 e R$ 700,00 -- 8%
# Se maior que R$ 700 -- 12%
#-----------------------------------------------------------------------------------------------------------------
# A gratificação que está na tabela a seguir
# Se salário-base for MENOR que R$ 500,00 com até 3 anos de tempo de serviço -- gratificação = 23
# Se salário-base for MENOR que R$ 500,00 entre 3 anos a 6 anos de tempo de serviço -- gratificação = 35
# Se salário-base for MENOR que R$ 500,00 acima de 6 anos de tempo de serviço -- gratificação = 33
# Se salário-base for MAIOR que R$ 500,00 com até 3 anos de tempo de serviço -- gratificação = 20
# Se salário-base for MAIOR que R$ 500,00 com mais de 3 anos de tempo de serviço -- gratificação = 30
#-----------------------------------------------------------------------------------------------------------------
# O salário líquido, ou seja, salário-base menos imposto mais gratificação;
# A categoria que estpa na tabela a seguir.
# Salário liquido até R$ 350,00 -- classificação = A
# Salário líquido entre R$ 350,01 a R$ 600,00 -- classificação = B
# Salário liquido acima de R$ 600,01 -- classificação = C

codigo = int(input('Digite o código do funcionário: '))
salario = float(input('Salário do funcionário: '))
tempoServico = int(input('Tempo de serviço: '))

if salario < 200:
  inposto = 0
elif salario >= 200 and salario < 450:
  imposto = salario *  0.03
elif salario >= 450 and salario < 700:
  imposto = salario *  0.08
else:
  imposto = salario *  0.12

if tempoServico >= 0:
  if salario < 500 and tempoServico < 3:
    gratificacao = 23
  elif salario < 500 and tempoServico >= 3 and tempoServico < 6:
    gratificacao = 35
  elif salario < 500 and tempoServico > 6:
    gratificacao = 33
  elif salario >= 500 and tempoServico < 3:
    gratificacao = 20
  else:
    gratificacao = 30

salarioLiquido = salario + imposto + gratificacao

if salarioLiquido < 350:
  classificacao = "A"
elif salarioLiquido >= 350 and salarioLiquido < 600:
  classificacao = "B"
else:
  classificacao = "C"

print(f'O valor do imposto é: {imposto}')
print(f'A gratificação será no valor de: {gratificacao}')
print(f'Salário liquido: {salarioLiquido}')
print(f'Sua classificação é: {classificacao}')

#-----------------------------------------------------------------------------------------------------------------

# Exercício 23

valorSalarioMin = float(input('Digite o valor do salário minimo do funcionário: '))
turnoTrabalho = input('Turno trabalhado (M-Matutino, V-Vespertino, N-Noturno): ')
categoriaFunc = input('Categoria do seu cargo (O-Operário, G-Gerente): ')
horasTrabalhadas = int(input('Horas trabalhadas no mês: '))


# Coeficiente do salário mínimo
if turnoTrabalho.upper() == 'M':
  valorCoeficiente = valorSalarioMin * 0.1
elif turnoTrabalho.upper() == 'V':
  valorCoeficiente = valorSalarioMin * 0.15
elif turnoTrabalho.upper() == 'N':
  valorCoeficiente = valorSalarioMin * 0.12
else:
  print('Turno invalido!')

print(f'Valor do coeficiente é: {valorCoeficiente:.2f}')

# Salário Bruto
salarioBruto = horasTrabalhadas * valorCoeficiente

print(f'Valor do salário Bruto é: {salarioBruto:.2f}')

# Valor do imposto
if categoriaFunc.upper() == 'O':
  if salarioBruto < 300:
    imposto = salarioBruto * 0.03
  
  else:
    imposto = salarioBruto * 0.5

elif categoriaFunc.upper() == 'G':
   if salarioBruto < 400:
      imposto = salarioBruto * 0.06
   
   else:
      imposto = salarioBruto * 0.04

else:
  print('valor inválido')  

print(f'Valor do imposto é: {imposto:.2f}')

#Gratificação do funcionário
if turnoTrabalho.upper() == 'N' and horasTrabalhadas >= 80:
  gratificacaoFunc = 50
else:
  gratificacaoFunc = 30

print(f'Valor do gratificação é: {gratificacaoFunc:.2f}')

#Auxílio Alimentação
if categoriaFunc == 'O' or valorCoeficiente <= 25:
  auxAlimentacao = salarioBruto / 3
else:
  auxAlimentacao = salarioBruto / 2

print(f'Valor do auxilio alimentação é: {auxAlimentacao:.2f}')

#Salário Líquido
salarioLiquido = salarioBruto - imposto + gratificacaoFunc + auxAlimentacao

print(f'Valor do salário líquido é: {salarioLiquido:.2f}')

if salarioLiquido < 350:
  print('Mal remunerado')
elif salarioLiquido >= 350 and salarioLiquido < 600:
  print('Normal')
else:
  print('Bem remunerado')

#-----------------------------------------------------------------------------------------------------------------

# Exercício 24
# Faça um programa que receba o preço, o tipo (A - Alimentação, L - Limpeza e V - Vestuário) e a refrigeração (S - Produto que necessita de refrigeração e N - Produto que não necessita de refrigeração) de um produto. Suponha que haverá apenas a digitação de dados válidos e, quando houver digitação de letras, utilize letras maiúsculas, Calcule e mostre:

# O valor adicional, de acordo com a tabela a seguir.
# Se refrigeração = 'N', tipo do produto = 'A' e preço do produto MENOR que 15, o valor adicional será no valor de R$ 2,00 e se o preço do produto for MAIOR OU IGUAL que 15 o valor adicional será no valor de R$ 5,00
# Se refrigeração = 'N', tipo do produto = 'L' e preço do produto MENOR que 10, o valor adicional será no valor de R$ 1,50 e se o preço do produto for MAIOR OU IGUAL que 10 o valor adicional será no valor de R$ 2,50
# Se refrigeração = 'N', tipo do produto = 'V' e preço do produto MENOR que 30, o valor adicional será no valor de R$ 3,00 e se o preço do produto for MAIOR OU IGUAL que 30 o valor adicional será no valor de R$ 2,50
# Se refrigeração = 'S', tipo do produto = 'A' o valor adicional será no valor de R$ 8,00
# Se refrigeração = 'S', tipo do produto = 'L' ou 'V' será isento do valor adicional

# O valor do imposto, de acordo com a regra a seguir.
# Se preço for MENOR que 25 o percentual sobre o preço será de 5%
# Se preço for MAIOR OU IGUAL que 25 o percentual sobre o preço será de 8%

# O preço de custo, ou seja, somar preço mais imposto.

# O desconto, de acordo com as regras a seguir.
# Calcular o desconto com base nas seguintes regras:
# Caso o tipo do produto = 'A' ou tipo de refrigeração = 'S' desconto = 0 caso não preencha nenhum desses requisitos o desconto será de 3%

# O novo preço, ou seja, preço mais adicional menos desconto.

# A classificação, de acordo com a regra a seguir.
# Caso o novo preço seja MENOR OU IGUAL a R$ 50,00 será classificado como Barato
# Caso o novo preço ESTEJA ENTRE R$ 50,00 e R$ 100,00 será classificado como Normal
# Caso o novo preço seja MAIOR OU IGUAL a R$ 100,00 será classificado como caro

refrigeracao = input('Digite "S" para produto que necessita de refrigeração ou "N" para produto que não necessita: ') 
tipoProduto = input('Digite o tipo do produto (A - Alimentação, L - Limpeza, V - Vestuário): ')
valorPreco = float(input('Digite o preço do produto: '))

# Condicional que restrige a escolha a letra "N" e a letra "S"
if refrigeracao.upper() == 'N' or refrigeracao.upper() == 'S':
  
  # Sendo digitado o tipo de refrigeração 'N', o tipo do produto sendo 'A' e menor que 15 o valor Adicional será de 2,00 caso contrário sera de 5,00
  if refrigeracao.upper() == 'N':
      if tipoProduto.upper() == 'A':
        if valorPreco < 15: 
            valorAdicional = 2
        else:
            valorAdicional = 5
      
      # Caso o tipo do produto seja 'L' e menor que 10 o valor Adicional será de 1,50 caso contrário sera de 2,50
      elif tipoProduto.upper() == 'L':
        if valorPreco < 10:
          valorAdicional = 1.50
        else:
          valorAdicional = 2.50  
      # Caso o tipo do produto seja 'V' e menor que 30 o valor Adicional será de 3,00 caso contrário será de 2,50
      elif tipoProduto.upper() == 'V':
        if valorPreco < 30:
          valorAdicional = 3
        else:
          valorAdicional = 2.50
      else:
         print('Erro: tipo de produto inexistente!1')
  
  # Sendo digitado o tipo de refrigeração 'S', o tipo do produto sendo 'A' e menor que 15 o valor Adicional será de 8,00
  if refrigeracao.upper() == 'S':
      if tipoProduto == 'A':
        valorAdicional = 8
      # Caso o tipo do produto seja 'L' ou 'V' será isento do valor adicional
      elif tipoProduto == 'L'or tipoProduto == 'V':
        valorAdicional = 0
      else:
        print('Erro: tipo de produto inexistente!')
else:
      print('Erro na seleção de categoria de resfriamento')

# Imposto
if valorPreco < 25:
  imposto = valorPreco * 0.05
else:
  imposto = valorPreco * 0.08

print(f'Valor imposto: R$ {imposto:.2f}')

# Preço de custo
precoCusto = valorPreco + imposto
print(f'Preço de custo: R$ {precoCusto:.2f}')


# Desconto
if tipoProduto == 'A' or refrigeracao == 'S':
  desconto = 0
else:
  desconto = valorPreco * 0.03

print(f'Valor desconto: R$ {desconto:.2f}')

# Calculo do novo preço
novoPreco = valorPreco + valorAdicional - desconto

print(f'Novo preço do produto: R$ {novoPreco:.2f}')

if novoPreco <= 50:
  classificacao = 'barato'
elif novoPreco > 50 and novoPreco < 100:
  classificacao = 'Normal'
else:
  classificacao = 'Caro'

print(f'Classificação: {classificacao}')