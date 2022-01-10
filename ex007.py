'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. '''
#1l = 3m
#1 lata = 18l
#1 lata = 80$
#ele informa os m
#eu tenho q retornar as lata/preço
import math
metros = int(input("informe por obsequio a quantidade em metros que deseja pintar:"))
litro = metros / 3
lata = math.ceil(litro / 18)
print('a quantidade de latas vão ser:',lata, '\nPreço:', lata*80)