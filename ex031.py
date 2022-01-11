'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''


l = int(input('digite a qnt de l: '))
tipo = str(input('selecione o tipo: "A","G": ')).upper()
conceito, j = [['A', 0.03, 0.05, 1.9],['G', 0.04, 0.06, 2.5]], 0
lista = []
for i in range(2):
  if l <= 20:
    preco_desconto =  ((l * conceito[i][j+3]) * conceito[i][j+1])
    lista.append(preco_desconto)
  else:
    preco_desconto = ((l * conceito[i][j+3]) * conceito[i][j+2])
    lista.append(preco_desconto)

print(lista)

if tipo == 'A':
  print((l * 1.9) - lista[0])
elif tipo == 'G':
  print((l * 2.5) - lista[1])