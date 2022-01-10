#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
num1 = float(input('fala ai tua nota no 1º bimestre'))
num2 = float(input('fala ai tua nota no 2º bimestre'))
num3 = float(input('fala ai tua nota no 3º bimestre'))
num4 = float(input('fala ai tua nota no 4º bimestre'))
media = num1 + num2 + num3 + num4
print("tua média é:", round(media/4, 3))