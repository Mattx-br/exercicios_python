'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. '''
# while True:
#   try:
#     ne = int(input('Digite o numero de eleitores: '))
#   except ValueError:
#     print('Digite apenas número inteiros')
#   else:
#     cont, votos = 1, []
#     print(ne)
#     while cont <= ne:
#       try:
#         e = int(input('\nEleitor {}\nDigite o número do seu candidato [1 a 3]:  '.format(cont)))
#       except ValueError:
#         print('\nDigite um número INTEIRO entre 1 e 3')
#         continue
#       else: 
#         if e not in range(1, 4):
#           print('\nDigite um número entre 1 e 3')
#           continue
#         else:
#           votos.append(e)
#           cont += 1
#   finally:
#     for i in range(1, 4):
#       print('\nCandidato {} : {} votos'.format(i, votos.count(i)))
#     restart = str(input('\nPressione Enter para reiniciar o programa.\n'))
#     if restart != '':
#       break