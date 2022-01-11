'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
numero = input("digite um numero menor que 1000 ---> ")
qtNumero = len(numero)
centena = numero[0:1]
dezena = numero[1:2]
unidade = numero[2:3]
while True:
  try:
    if qtNumero == 3:
        print(numero, "=", centena, "centenas,", dezena,"dezenas,", unidade, "unidades")

    if qtNumero == 2:
        dezena = numero[0:1]
        unidade = numero[1:2]
        print(numero+" = ", dezena, "dezenas,", unidade,"unidades")

    if qtNumero == 1:
        unidade = numero[0:1]
        print(numero, "=", unidade, "unidades")
    else:
      if qtNumero >= 4:
        print('numero invalido')
  finally:
      restart = str(input('\nPressione Enter para reiniciar o programa.\n'))
      if restart != '':
        break