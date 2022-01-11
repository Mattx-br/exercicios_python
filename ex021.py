'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''
x = str.lower((input("qual horario você estuda:\n M para matutino\n V para vespertino\n N para noturno\n ")))
if x == 'm':
 print(' Bom dia')
elif x == 'v':
 print('Boa tarde')
else:
 print('Boa noite')