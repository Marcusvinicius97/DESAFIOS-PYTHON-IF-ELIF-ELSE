#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n1 = float(input('Digite sua a nota da N1: '))
n2 = float(input('Digite sua a nota da N2: '))

média = (n1+n2)/2

if 7 > média >= 5:
    print(f'Você foi para recuperação, sua média foi {média:.1f}')
elif  média < 5:
    print(f'Você foi reprovado, sua média foi {média:.1f}')
else:
    print(f'Você foi aprovado, sua média foi {média:.1f}')

