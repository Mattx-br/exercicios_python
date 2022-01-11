'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.'''

x = int(input('digite um numero inteiro: '))
y = int(input('digite um numero inteiro: '))
z = float(input('digite um numero real: '))
dobro = (x * 2) * (y / 2)
triplo = (x * 3) + z
cubo = z ** 3
nd = ''
print ('produto do dobro do primeiro com metade do segundo: ', dobro)
print ('a soma do triplo do primeiro com o terceiro:{0:>10}{1}'.format(nd, triplo))
print ('o terceiro elevado ao cubo:{0:>28}{1}'.format(nd, cubo))