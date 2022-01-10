'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''
#minha versão
z = str(input('escreva uma letra: '))
vogais = ['a', 'e', 'i', 'o', 'u']
if z.lower() in vogais:
 print('essa letra é uma vogal')
else:
 print('essa letra é consoante')