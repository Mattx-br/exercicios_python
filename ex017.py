'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
n1 = float(input('digite sua nota: '))
n2 = float(input('digite sua segunda nota: '))
lista = [n1,n2]
media = sum(lista)/ 2
if media == 10:
 print('aprovado com distinção')
elif media >= 7:
 print('aprovado')
else:
 print('reprovado')