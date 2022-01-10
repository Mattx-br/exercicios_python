'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.''' 
sexo = input('digite seu sex(m-masc,f-femin )').lower()
if sexo == 'f':
  print('seu sexo é feminino')
elif sexo == 'm':
  print('seu sexo é masculino')
else:
  print('seu sexo esta no LGBTQ')