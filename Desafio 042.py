#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))

if (n2-n3) < n1 < n2+n3 and (n1 - n3) < n2 < n1+n3 and (n1-n2) < n3 < n1+n2:
  print('Os segmentos digitados podem formar um triângulo: ', end='')
  if n1 == n2 == n3:
      print('EQUILÁTERO')
  elif n1!=n2!=n3!=n1:
      print('ESCALENO')
  else:
      print('ISÓSCELES')

else:
    print(f'\33[0:33:40mOs valores digitados não podem formar um triângulo')
