# 0️⃣0️⃣1️⃣
# print("olá mundo")

# 0️⃣0️⃣2️⃣
'''Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].'''
# numero = input('Digite um número: ')
# print('seu numero é', float(numero))

# 0️⃣0️⃣3️⃣
'''Faça um Programa que peça dois números e imprima a soma.'''
# numero1 = float(input('digite um numero: '))
# numero2 = float(input('digite um numero: '))
# print('a soma delas é:', round(numero1 + numero2,5))

# 0️⃣0️⃣4️⃣
#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
'''num1 = float(input('fala ai tua nota no 1º bimestre'))
num2 = float(input('fala ai tua nota no 2º bimestre'))
num3 = float(input('fala ai tua nota no 3º bimestre'))
num4 = float(input('fala ai tua nota no 4º bimestre'))
media = num1 + num2 + num3 + num4
print("tua média é:", round(media/4, 3))'''

# 0️⃣0️⃣5️⃣
'''Faça um Programa que converta metros para centímetros.'''
# metros = int(input("digite o m:"))
# print('a quantidade disso em cm é:', metros * 100)

# 0️⃣0️⃣6️⃣
'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
# r = float(input("digite o relampago marquinhos:"))
# print('o raio dms eh', r ** 2)

# 0️⃣0️⃣7️⃣
'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. '''
  #1l = 3m
  #1 lata = 18l
  #1 lata = 80$
  #ele informa os m
  #eu tenho q retornar as lata/preço
# import math
# metros = int(input("informe por obsequio a quantidade em metros que deseja pintar:"))
# litro = metros / 3
# lata = math.ceil(litro / 18)
# print('a quantidade de latas vão ser:',lata, '\nPreço:', lata*80)

# 0️⃣0️⃣8️⃣
'''Faça um Programa que peça dois números e imprima o maior deles. '''
# n1 = float(input('Digite o n1: '))
# n2 = float(input('Digite o n2: '))
# if n1 > n2:
#   print(n1)
# elif n2 > n1:
#   print(n2)
# else:
#   print('iguais')

# 0️⃣0️⃣9️⃣
'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. '''
# n1 = float(input("digite um n:"))
# if n1 > 0:
#   print(n1,'é maior que zero')
# elif n1 < 0:
#   print(n1, 'é menor que zero')
# else:
#   print(n1, 'é zero o seu ')

# 0️⃣1️⃣0️⃣
'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.''' 
# sexo = input('digite seu sex(m-masc,f-femin )').lower()
# if sexo == 'f':
#   print('seu sexo é feminino')
# elif sexo == 'm':
#   print('seu sexo é masculino')
# else:
#   print('seu sexo esta no LGBTQ')

# 0️⃣1️⃣1️⃣
'''Faça um Programa que leia três números e mostre-os em ordem decrescente. '''
'''n1 = float(input('n1: '))
n2 = float(input('n2: '))
n3 = float(input('n3: '))
lista = [n1, n2, n3]
print(sorted(lista, reverse=True))'''

# 0️⃣1️⃣2️⃣
'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
    # Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    # salários até R$ 280,00 (incluindo) : aumento de 20%
    # salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    # salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    # salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    # o salário antes do reajuste;
    # o percentual de aumento aplicado;
    # o valor do aumento;
    # o novo salário, após o aumento. '''
'''sal = float(input('digite o salario'))
if sal <= 280:
  au = sal * 0.2
  new = sal + au
  print(sal,',', 0.2,',', au,',', new)'''

# 0️⃣1️⃣3️⃣
'''TREINO'''
#ar = float(input('digite um numero'))
#i = 0
#while (i <= 10):
  #print(ar * i)
  #i = i+1

'''TREINO DE TABUADA'''
# x = 0
# print("while")
# while(x<10):
#     print(x)
#     x+=1;
# else:
#     while(x > 0):
#       print(x)
#       x = x - 1
# print("fim")

'''TREINO'''
#nesse caso, vai imprimir o b
#lista = ['a','b','c']
#print(lista[1])

# 0️⃣1️⃣4️⃣
'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''
#h = float(input('digite quanto você ganha por hora: '))
#m =float(input('digite quantas horas você trabalha por mês: '))
#bru = h * m
#ir = bru * .11
#inss = bru * .08
#sind = bru * .05
#desc = ir + inss + sind
#liq = bru - desc
#print(
#'bruto', round(bru),'\n'
#'inss', round(inss),'\n'
#'sindicato', round(sind),'\n'
#'salario liquido', round(liq),'\n')
#a = float(input('digite um n: '))
#b = float(input('digite outro n: '))
#if a > b:
#  print(a)
#else:
#  print(round(b, 3))


# 0️⃣1️⃣5️⃣
'''Faça um Programa que peça dois números e imprima o maior deles.'''
#a = float(input('digite um num: '))
#b = float(input('digite outro num: '))
#lista = [a,b]
#print(round(max(lista),3))

# 0️⃣1️⃣6️⃣
'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''
#minha versão
#z = str(input('escreva uma letra: '))
#vogais = ['a', 'e', 'i', 'o', 'u']
#if z.lower() in vogais:
#  print('essa letra é uma vogal')
#else:
#  print('essa letra é consoante')

# 0️⃣1️⃣7️⃣
'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
#n1 = float(input('digite sua nota: '))
#n2 = float(input('digite sua segunda nota: '))
#lista = [n1,n2]
#media = sum(lista)/ 2
#if media == 10:
#  print('aprovado com distinção')
#elif media >= 7:
#  print('aprovado')
#else:
#  print('reprovado')

# 0️⃣1️⃣8️⃣
'''Faça um Programa que leia três números e mostre o maior deles.'''
#a = float(input('digite um num: '))
#b = float(input('digite outro num: '))
#c = float(input('digite mais um num: '))
#lista = [a, b, c]
#print(max(lista))

# 0️⃣1️⃣9️⃣
'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''
#a = float(input('digite um num: '))
#b = float(input('digite outro num: '))
#c = float(input('digite mais um num: '))
#lista = [a, b, c]
#print(max(lista))
#print(min(lista))

# 0️⃣2️⃣0️⃣
'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''
#p1 = float(input('informe o preço do produto 1: '))
#p2 = float(input('informe o preço do produto 2: '))
#p3 = float(input('informe o preço do produto 3: '))
#lista = [p1 , p2, p3]
#if p1 == min(lista):
#  print('\nvocê deve comprar o produto 1')
#elif p2 == min(lista):
#  print('\nvocê deve comprar o produto 2')
#else:
#  print('\nvocê deve comrpar o produto 3')

'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
#p1 = float(input('informe o preço do produto 1: '))
#p2 = float(input('informe o preço do produto 2: '))
#p3 = float(input('informe o preço do produto 3: '))
#lista = [p1 , p2, p3]
#lista.sort(reverse=True)
#print(lista)

# 0️⃣2️⃣1️⃣
'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''
#x = str.lower((input("qual horario você estuda:\n M para matutino\n V para vespertino\n N para noturno\n ")))
#if x == 'm':
#  print(' Bom dia')
#elif x == 'v':
#  print('Boa tarde')
#else:
#  print('Boa noite')

# 0️⃣2️⃣2️⃣
'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''
#h = float(input('informe quanto você ganha por hora: '))
#m = float(input('informe quanto você trabalha por mês: '))
#sb = h * m #salario bruto
#if sb <= 900:
#  ir = sb * 1
#elif sb <= 1500:
#  ir = sb * .05
#elif sb <= 2500:
#  ir = sb * .10
#else:
#  ir = sb * .20
#inss = sb * .10
#fgts = sb * .11
#desc = ir + inss + fgts
#sl = sb - desc
#print('\nSalario Bruto:', sb)
#print('IR:',ir)
#print('INSS:',inss)
#print('FGTS:',fgts)
#print('Desconto:',desc)
#print('Salario Liquido:',sl)

# 0️⃣2️⃣3️⃣
'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''
#x = int(input('informe um num para saber o dia da semana: '))
#lista = ['null', 'domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']
#if x == 1:
#  print(lista[1])
#elif x == 2:
#  print(lista[2])
#elif x == 3:
#  print(lista[3])
#elif x == 4:
#  print(lista[4])
#elif x == 5:
#  print(lista[5])
#elif x == 6:
#  print(lista[6])
#elif x == 7:
#  print(lista[7])
#else:
#  print('numero inválido')

# 0️⃣2️⃣4️⃣
'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''
#n1 = float(input('digite sua nota: '))
#n2 = float(input('digite sua segunda nota: '))
#lista = [n1,n2]
#media = sum(lista)/ 2
#if media >= 9:      #A
#  print('notas:', n1,',', n2)
#  print('média:',round(media))
#  print('conceito: A')
#  print('APROVADO')
#elif media >= 7.5:  #B
#  print('notas:', n1,',', n2)
#  print('média:', round(media))
#  print('conceito: B  ')
#  print('APROVADO')
#elif media >= 6:  #C
#  print('notas:', n1,',', n2)
#  print('média:', round(media))
#  print('conceito: C  ')
#  print('APROVADO')
#elif media >= 4:  #D
#  print('notas:', n1,',', n2)
#  print('média:', round(media))
#  print('conceito: D  ')
#  print('REPROVADO')
#else:               #E
#  print('notas:', n1,',', n2)
#  print('média:', round(media))
#  print('conceito: E  ')
#  print('REPROVADO')

# 0️⃣2️⃣5️⃣
'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

# l1 = float(input('informe um lado do triângulo: '))
# l2 = float(input('informe outro lado do triângulo: '))
# l3 = float(input('informe o seguinte lado do triângulo: '))

# if l1 + l2 >= l3 and l2 + l3 >= l1 and l1 + l3 >= l2:
#   print('é um triângulo.')
#   if l1 == l2 and l1 == l3:
#       print(' É equilatero.')
#   elif l1 == l2 or l1 == l3:
#       print('É isósceles')
#   else:
#       print('É escaleno')
# else:
#  print('não é um triângulo.')

# 0️⃣2️⃣6️⃣
'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: '''
# while True:
#   try:
#     numero = int(input('\nDigite um número Inteiro: '))
#   except ValueError:
#     print('\nReinicie o programa e digite um número INTEIRO')
#   else:
#     for i in range(1, 11):
#       print('{} X {} = {}'.format(numero, i, numero*i))
#   finally:
#     opt = str(input('\nDigite R para reiniciar')).upper()
#     if opt != 'R':
#       break

# 0️⃣2️⃣7️⃣
'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. '''
# while True:
#   try:
#     ne = int(input('Digite o numero de eleitores: '))
#   except ValueError:
#     print('Digite apenas número inteiros')
#   else:
#     cont, votos = 1, []
#     print(ne)
#     while cont <= ne:
#       try:
#         e = int(input('\nEleitor {}\nDigite o número do seu candidato [1 a 3]:  '.format(cont)))
#       except ValueError:
#         print('\nDigite um número INTEIRO entre 1 e 3')
#         continue
#       else: 
#         if e not in range(1, 4):
#           print('\nDigite um número entre 1 e 3')
#           continue
#         else:
#           votos.append(e)
#           cont += 1
#   finally:
#     for i in range(1, 4):
#       print('\nCandidato {} : {} votos'.format(i, votos.count(i)))
#     restart = str(input('\nPressione Enter para reiniciar o programa.\n'))
#     if restart != '':
#       break

# 0️⃣2️⃣8️⃣
'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo: 
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''

# x = int(input('Fatorial de: '))

# fato = x - 1
# tt = x * (x - fato)
# print('{}! = '.format(x), end='')
# for i in range(1, x):
#   tt = tt * (x - fato)
#   print(fato + 1, end =' * ')
#   fato -= 1
# print('1 =', tt)

# 0️⃣2️⃣9️⃣
'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
'''numero = input("digite um numero menor que 1000 ---> ")
qtNumero = len(numero)
centena = numero[0:1]
dezena = numero[1:2]
unidade = numero[2:3]
while True:
  try:
    if qtNumero == 3:
        print(numero, "=", centena, "centenas,", dezena,"dezenas,", unidade, "unidades")

    if qtNumero == 2:
        dezena = numero[0:1]
        unidade = numero[1:2]
        print(numero+" = ", dezena, "dezenas,", unidade,"unidades")

    if qtNumero == 1:
        unidade = numero[0:1]
        print(numero, "=", unidade, "unidades")
    else:
      if qtNumero >= 4:
        print('numero invalido')
  finally:
      restart = str(input('\nPressione Enter para reiniciar o programa.\n'))
      if restart != '':
        break'''

# 0️⃣3️⃣0️⃣
'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

# notas = []
# for i in range(2):
#   n = float(input('Digite sua {} nota: '.format(i+1)))
#   notas.append(n)
# media, j, conceitos = sum(notas)/2, 0, [['APROVADO', 'A', 9.0, 10.0], ['APROVADO', 'B', 7.5, 9.0], ['APROVADO', 'C', 6.0, 7.5],  ['REPROVADO', 'D', 4.0, 6.0], ['REPROVADO', 'E', -1, 4.0]]

# for i in range(5):
#     if media > conceitos[i][j+2] and media <= conceitos[i][j+3]:
#       nota_letra = conceitos[i][j+1]
#       conceito_final = conceitos[i][j]

# 0️⃣3️⃣1️⃣
'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''


# l = int(input('digite a qnt de l: '))
# tipo = str(input('selecione o tipo: "A","G": ')).upper()
# conceito, j = [['A', 0.03, 0.05, 1.9],['G', 0.04, 0.06, 2.5]], 0
# lista = []
# for i in range(2):
#   if l <= 20:
#     preco_desconto =  ((l * conceito[i][j+3]) * conceito[i][j+1])
#     lista.append(preco_desconto)
#   else:
#     preco_desconto = ((l * conceito[i][j+3]) * conceito[i][j+2])
#     lista.append(preco_desconto)

# print(lista)

# if tipo == 'A':
#   print((l * 1.9) - lista[0])
# elif tipo == 'G':
#   print((l * 2.5) - lista[1])

# 0️⃣3️⃣2️⃣
'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.'''

# x = int(input('digite um numero inteiro: '))
# y = int(input('digite um numero inteiro: '))
# z = float(input('digite um numero real: '))
# dobro = (x * 2) * (y / 2)
# triplo = (x * 3) + z
# cubo = z ** 3
# nd = ''
# print ('produto do dobro do primeiro com metade do segundo: ', dobro)
# print ('a soma do triplo do primeiro com o terceiro:{0:>10}{1}'.format(nd, triplo))
# print ('o terceiro elevado ao cubo:{0:>28}{1}'.format(nd, cubo))

# 0️⃣3️⃣3️⃣
'''treino com .format()'''

# s = 'Adoro Python'

# # alinha a direita com 20 espaços em branco
# print("{0:>20}".format(s))

# # alinha a direita com 20 símbolos #
# print("{0:#>20}".format(s))

# # alinha ao centro usando 10 espaços em branco a esquerda e 10 a direita
# print("{0:^28}".format(s))

# # imprime só as primeiras cinco letras
# print("{0:.5}".format(s))