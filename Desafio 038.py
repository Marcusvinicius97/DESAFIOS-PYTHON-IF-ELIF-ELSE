#Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'Primeiro  valor "{n1}" é maior que o segundo valor "{n2}".')

elif n1 == n2:
    print(f'Os dois valores são iguais.')

else:
    print(f'Segundo valor "{n2}" é maior que o primeiro valor "{n1}". ')
