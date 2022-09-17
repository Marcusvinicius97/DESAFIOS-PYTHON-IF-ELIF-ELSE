#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
import numpy
N = int(input('Digite um valor inteiro: '))
B = int(input(f'\n[1] Binário'
              f'\n[2] Octal'
              f'\n[3] Hexadecimal '
              f'\nEscolha uma das opções da base de conversão: '))

if B == 1:
    print(f'O valor convertido em binário: {numpy.binary_repr(N)}')
elif B == 2:
    print(f'O valor convertido em octal: {oct(N)}')
elif B == 3:
    print(f'O valor convertido em hexadecimal: {hex(N)}')
else:
    print(f'OPÇÃO INVÁLIDA, TENTE NOVAMENTE')






