#Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('_______________________T E N D A____________________')

C = float(input('Digite o valor da casa: R$'))
S = float(input('Digite o salário do comprador: R$'))
T = int(input('Digite em quantos anos deseja pagar o valor da casa: '))

min = C/(T*12) #PRESTAÇÕES MINIMA COM BASE NO TEMPO
VPM = S*0.3 #VP (VALOR DA PRESTAÇÃO MINIMA DE 30% DO SALÁRIO)
PORCENTAGEM = (min*100)/S

if min <= VPM:
    print(f'\nParabéns, o empréstimo foi aceito!'
          f'\no valor da prestação foi de R${min:.2f}, ou seja '
          f'\no cliente vai pagar {PORCENTAGEM:.2f}% do seu salário.')
else:
    print(f'Desculpa, o empréstimo foi negado! '
          f'\no valor da prestação foi de R${min:.2f}')

