'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: '''
while True:
  try:
    numero = int(input('\nDigite um número Inteiro: '))
  except ValueError:
    print('\nReinicie o programa e digite um número INTEIRO')
  else:
    for i in range(1, 11):
      print('{} X {} = {}'.format(numero, i, numero*i))
  finally:
    opt = str(input('\nDigite R para reiniciar')).upper()
    if opt != 'R':
      break