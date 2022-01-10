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
h = float(input('digite quanto você ganha por hora: '))
m =float(input('digite quantas horas você trabalha por mês: '))
bru = h * m
ir = bru * .11
inss = bru * .08
sind = bru * .05
desc = ir + inss + sind
liq = bru - desc
print(
'bruto', round(bru),'\n'
'inss', round(inss),'\n'
'sindicato', round(sind),'\n'
'salario liquido', round(liq),'\n')
a = float(input('digite um n: '))
b = float(input('digite outro n: '))
if a > b:
 print(a)
else:
 print(round(b, 3))