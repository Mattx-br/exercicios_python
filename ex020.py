'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''
p1 = float(input('informe o preço do produto 1: '))
p2 = float(input('informe o preço do produto 2: '))
p3 = float(input('informe o preço do produto 3: '))
lista = [p1 , p2, p3]
if p1 == min(lista):
 print('\nvocê deve comprar o produto 1')
elif p2 == min(lista):
 print('\nvocê deve comprar o produto 2')
else:
 print('\nvocê deve comrpar o produto 3')