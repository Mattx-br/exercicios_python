'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo: 
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''

x = int(input('Fatorial de: '))

fato = x - 1
tt = x * (x - fato)
print('{}! = '.format(x), end='')
for i in range(1, x):
  tt = tt * (x - fato)
  print(fato + 1, end =' * ')
  fato -= 1
print('1 =', tt)