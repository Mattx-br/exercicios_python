'''Faça um Programa que leia três números e mostre-os em ordem decrescente. '''
n1 = float(input('n1: '))
n2 = float(input('n2: '))
n3 = float(input('n3: '))
lista = [n1, n2, n3]
print(sorted(lista, reverse=True))