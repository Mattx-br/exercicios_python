'''Faça um Programa que peça dois números e imprima o maior deles. '''
n1 = float(input('Digite o n1: '))
n2 = float(input('Digite o n2: '))
if n1 > n2:
  print(n1)
elif n2 > n1:
  print(n2)
else:
  print('iguais')