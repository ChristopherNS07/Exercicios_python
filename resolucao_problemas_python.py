# Exercício 1
# Faça um programa que receba dois números, calcule e mostre a subtração do primeiro número pelo segundo.

# entrada dos dados inteiros.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Processamento do calculo.
resultado = num1 - num2

# Saida do resultado.
print(f'O resultado da subtração do primeiro pelo segundo é: {resultado}')

#------------------------------------------------------------------------------------------------------------
# Exercício 2
# Faça um programa que receba três números. Calcule e mostre a multiplicação desses numeros.

#Entrada dos números para a operação em float devido a possibilidade de casas decimais.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# Processo da multiplicação dos números contidos nas três variáveis.
resultado = num1 * num2 * num3

# Resultado do calculo da multiplicação.
print(f'O resultado da multiplicação dos três número é: {resultado:.2f}')

#------------------------------------------------------------------------------------------------------------
# Exercício 3
# Faça um programa que receba dois números, calcule e mostre a divisão do primeiro número pelo segundo. Sabe-se que o segundo número não pode ser zero. Portanto não é necessário se preocupar com validações.

# Entrada dos números para a operação.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Processo da divisão da primeira variável pela segunda.
resultado_div = num1 // num2

# Saída do resultado do calculo da divisão realizada.
print(f'O resultado da divisão do primeiro numero pelo segundo é: {resultado_div:.2f}')

#------------------------------------------------------------------------------------------------------------
# Exercício 4
# Faça um programa que receba duas notas, calcule e mostre a média poderada dessas notas, considerando peso 2 para a primeira nota e peso 3 para a segunda nota.

# Entrada dos valores nas variáveis das notas e dos pesos que nesse caso são valores constantes.
peso_1 = 2
peso_2 = 3
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

# Processo do calculo de média ponderada onde multiplica as notas pelo peso correspondente e soma os dois resultados dividindo pela quantidade de notas.
resultado_media = ((nota1 * peso_1) + (nota2 * peso_2)) / 2

# Resultado da média ponderada.
print(f'A média podenrada das notas é: {resultado_media}')

#------------------------------------------------------------------------------------------------------------
# Exercício 5
# Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

# Entrada do preço do produto.
preco_produto = float(input('Digite o preço do produto: '))

# Calculo do desconto sendo aplicado no preço atual do produto.
desconto = preco_produto - (preco_produto * 0.1)

# Resultado do preço do produto com os 10% de desconto aplicado.
print(f'Preço atualizado do produto com desconto: {desconto}')

#------------------------------------------------------------------------------------------------------------
# Exercício 6
# Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre a comissão e o salário final do funcionário.

# Variáveis de venda total do funcionário com as constantes de salario e comissão.
venda_total = float(input('Digite a venda total do funcionário: '))
salario_base = 1350
comissao = 0.04

# Calculo de quanto é a comissão sobre a venda e soma da comissão com o salário base.
calculo_comissao = venda_total * comissao
salario_final = salario_base + calculo_comissao

#Saída do resultado da comissão e o salário total.
print(f'A comissão do funcionário será de: {calculo_comissao} ')
print(f'O salário final é: {salario_final}')

#------------------------------------------------------------------------------------------------------------
# Exercício 7
# Faça um programa que receba o peso de uma pessoa, calcule e mostre:
# a) o novo peso se a pessoa engordar 15% sobre o peso digitado;
# b) o novo peso se a pessoa emagrecer 20% sobre o peso digitado.

# Entrada do peso da pessoa.
peso_pessoa = float(input('Digite seu peso: '))

#Calculo das hipoteses do peso com 15% a mais e 20% a menos.
engordar = peso_pessoa + (peso_pessoa * 0.15)
emagrecer = peso_pessoa - (peso_pessoa * 0.20)

# Print do peso com o adicional de 15% e a redução de 20%.
print(f'Novo peso caso engorde 15%: {engordar:.1f} kg')
print(f'Novo peso caso emagreça 20%: {emagrecer:.1f} kg')

#------------------------------------------------------------------------------------------------------------
# Exercício 8
# Faça um programa que receba o peso de uma pessoa em quilos. calcule e mostre esse peso em gramas.

#Entrada do peso para conversão.
peso_pessoa_kg = float(input('Digite o peso:'))

# Calculo de conversão do peso em kilo para gramas.
peso_gr = peso_pessoa_kg * 1000

# Saída da conversão do peso em KG para gramas.
print((f'Peso em gramas: {peso_gr}'))

#------------------------------------------------------------------------------------------------------------
# Exercício 9
# Faça um programa que calcule e mostre a área de um trapézio.

# Entrada das bases do trapésio.
base_maior = float(input('Digite a base maior: '))
base_menor = float(input('Digite a base menor: '))
altura = float(input('Digite a altura: '))

# Calculo da área do trapésio somando as bases, multiplicando pela altura e dividindo por 2.
calculo_area = ((base_maior + base_menor) * altura) / 2

# Resultado da área do trapésio.
print(f'A área do trapésio é: {calculo_area} ')

#------------------------------------------------------------------------------------------------------------
# Exercício 10
# Faça um programa que calcule e mostre a área de um quadrado

# Valores dos lados do quadrado.
lado1 = int(input('Digite o valor do lado 1: '))
lado2 = int(input('Digite o valor do lado 2: '))

# Processo do calculo para saber a área do quadrado multiplicando os lados.
area_quadrado = lado1 * lado2

# Valor final do calculo da área do quadrado.
print(f'O valor da área do quadrado é: {area_quadrado}')

#------------------------------------------------------------------------------------------------------------
# Exercício 11
# Faça um programa que calcule e mostre a área de um quadrado.

# Variáveis que contem o valor da diagonal maior e diagonal menor.
diagonal_maior = int(input(f'Digite o valor do diagonal maior: '))
diagonal_menor = int(input(f'Digite o valor do diagonal menor: '))

# Calculo da área do losango multiplicando a diagonal maior pela diagonal menor e dividindo por 2.
area_losango = (diagonal_maior * diagonal_menor) / 2

# Resultado do calculo da área do losango.
print(f'O valor da área do losango é: {area_losango}')

#------------------------------------------------------------------------------------------------------------
# Exercício 12
# Faça um programa que receba o valor do salário minimo e o valor do salário de um funcionário, calcule e mostre a quantidade de salários minimos que ganha esse funcionário.

# Valores incluidos nas variáveis correspondentes ao salario minimo atual e salario do funcionário.
salario_minimo = 1200
salario_funcionario = float(input('Digite o salário do funcionario: '))

# Calculo para saber o equivalente quantos salarios minimos o salario do funcionário corresponde.
quantidade_salarios = salario_funcionario / salario_minimo

# Resultado de quantos salários minimos o funcionário recebe.
print(f'O funcionário ganha o equivalente a: {quantidade_salarios:.2f} salários minimos')

#------------------------------------------------------------------------------------------------------------
# Exercício 13
# Faça um programa que calcule e mostre a tabuada de um número digitado pelo usuário.

# Variável que ira conter o valor que o usuário quer
num_init = int(input('Digite o número para a tabuada: '))

# Calculo do número digitado pelo usuário pelos respectivos números da tabuada.
calculo1 = num_init * 1
calculo2 = num_init * 2
calculo3 = num_init * 3
calculo4 = num_init * 4
calculo5 = num_init * 5
calculo6 = num_init * 6
calculo7 = num_init * 7
calculo8 = num_init * 8
calculo9 = num_init * 9
calculo10 = num_init * 10

# Resultado do calculo das variáveis
print(f'{num_init}x1 = {calculo1}')
print(f'{num_init}x2 = {calculo2}')
print(f'{num_init}x3 = {calculo3}')
print(f'{num_init}x4 = {calculo4}')
print(f'{num_init}x5 = {calculo5}')
print(f'{num_init}x6 = {calculo6}')
print(f'{num_init}x7 = {calculo7}')
print(f'{num_init}x8 = {calculo8}')
print(f'{num_init}x9 = {calculo9}')
print(f'{num_init}x10 = {calculo10}')


#------------------------------------------------------------------------------------------------------------
# Exercício 14
# Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# a) a idade dessa pessoa em anos;
# b) a idade dessa pessoa em meses;
# c) a idade dessa pessoa em semanas;
# d) a idade dessa pessoa em dias.

# Variáveis que armazenam o ano de nascimento do usuário e o ano atual
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = 2023

# Processo de calculo da idade da pessoa em anos, meses, semanas e dias.
idade_pessoa = ano_atual - ano_nascimento
idade_mes = (ano_atual - ano_nascimento) * 12 # quantos meses tem no ano
idade_semanas = (ano_atual - ano_nascimento) * 52.14 # quantas semanas tem no ano
idade_dias = (ano_atual - ano_nascimento) * 365 # quantos dias tem no ano

print(f'Sua idade é: {idade_pessoa}')
print(f'Sua idade em meses: {idade_mes}')
print(f'Sua idade em semanas: {idade_semanas}')
print(f'Sua idade em dias: {idade_dias}')  

#------------------------------------------------------------------------------------------------------------
# Exercício 15
# João recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta. Faça um programa que calcule e mostre quanto restará do salário do João.

# Valores da multa, salario e as duas contas
multa = 0.02
conta1 = float(input('Digite o valor da primeira conta: '))
conta2 = float(input('Digite o valor da segunda conta: '))
salario = 1500

# Calculo das contas com o acréscimo das multas sendo descontado diretamente do salário
calculo_multa1 = (conta1 + multa)
calculo_multa2 = (conta2 + multa)
resto_salario = salario - conta1 - conta2

print(f'Valor do salário após pagar as contas: {resto_salario}')

#------------------------------------------------------------------------------------------------------------
# Exercício 16
# Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.

# Valores dos catetos
cateto1 = int(input('Digite o valor do primeiro cateto: '))
cateto2 = int(input('Digite o valor do segundo cateto: '))

# Calculando o valor da hipotenusa
calculo_hipotenusa = (cateto1**2 + cateto2**2)**0.5

print(f'O valor da Hipotenusa é: {calculo_hipotenusa:.2f}')

#------------------------------------------------------------------------------------------------------------
# Exercício 24
# Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa vai viajar possui. Essa pessoa vai passar por vários países e precisa converter seu dinheiro em dólares, marco alemão e libra esterlina. sabe-se que a cotação do dólar é de R$ 1.80, do marco alemão é de R$ 2.00, e da libra esterlina é de R$ 1.57. O programa deve fazer as conversões e mostra-lás.

# Cotação das moedas segundo o problema estabeleceu
valor_reais = float(input('Digite o dinheiro em reais para conversão: '))

cotacao_dolar = 1.80
cotacao_marco =  2.00
cotacao_libra = 1.57

# Calculo de conversão nas diversas moedas propostas
conversao_dolar = valor_reais / cotacao_dolar
conversao_marco = valor_reais / cotacao_marco
conversao_libra = valor_reais / cotacao_libra

# Saida das conversões
print(f'Seu dinheiro em real é {valor_reais} e convertido para dolar fica {conversao_dolar:.2f}')
print(f'Seu dinheiro em real é {valor_reais} e convertido para dolar fica {conversao_marco:.2f}')
print(f'Seu dinheiro em real é {valor_reais} e convertido para dolar fica {conversao_libra:.2f}')

#------------------------------------------------------------------------------------------------------------
# Exercício 25
# Faça um programa que receba uma hora (uma variável para hora e outra para minutos), calcule e mostre:
# a) a hora digitada convertida em minutos;
# b) o total dos minutos, ou seja, os minutos digitados mais a conversão anterior;
# c) o total dos minutos convertidos em segundos.

# Valor de horas e minutos digitados pelo usuário
horas = int(input('Digite a hora: '))
minutos = int(input('Digite os minutos: '))

# Calculo de conversão de horas em minutos, a soma dos minutos digitados pelo usuario com a conversão anterior de horas em minutos e a transformação em segundos do total de minutos. 
hora_minutos = horas * 60
total_minutos = minutos + hora_minutos  
total_segundos = total_minutos * 60

print(f'A hora convertida em minutos: {hora_minutos}')
print(f'Minutos digitados + hora convertido em minutos: {total_minutos}')
print(f'O total de minutos convertidos em segundos é: {total_segundos}')