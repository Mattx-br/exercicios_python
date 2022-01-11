'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''
n1 = float(input('digite sua nota: '))
n2 = float(input('digite sua segunda nota: '))
lista = [n1,n2]
media = sum(lista)/ 2
if media >= 9:      #A
 print('notas:', n1,',', n2)
 print('média:',round(media))
 print('conceito: A')
 print('APROVADO')
elif media >= 7.5:  #B
 print('notas:', n1,',', n2)
 print('média:', round(media))
 print('conceito: B  ')
 print('APROVADO')
elif media >= 6:  #C
 print('notas:', n1,',', n2)
 print('média:', round(media))
 print('conceito: C  ')
 print('APROVADO')
elif media >= 4:  #D
 print('notas:', n1,',', n2)
 print('média:', round(media))
 print('conceito: D  ')
 print('REPROVADO')
else:               #E
 print('notas:', n1,',', n2)
 print('média:', round(media))
 print('conceito: E  ')
 print('REPROVADO')