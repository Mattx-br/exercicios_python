'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''
x = int(input('informe um num para saber o dia da semana: '))
lista = ['null', 'domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']
if x == 1:
 print(lista[1])
elif x == 2:
 print(lista[2])
elif x == 3:
 print(lista[3])
elif x == 4:
 print(lista[4])
elif x == 5:
 print(lista[5])
elif x == 6:
 print(lista[6])
elif x == 7:
 print(lista[7])
else:
 print('numero inválido')