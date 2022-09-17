#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto;
#– à vista no cartão: 5% de desconto;
#– em até 2x no cartão: preço formal;
#– 3x ou mais no cartão: 20% de juros.

produto = float(input('Digite o valor do produto: R$'))
pagamento = int(input('\n[1] À VISTA DINHEIRO OU CHEQUE'
                      '\n[2] À VISTA NO CARTÃO'
                      '\n[3] EM ATÉ 2x NO CARTÃO'
                      '\n[4] 3x ou MAIS NO CARTÃO'
                      '\nDIGITE UMA DAS OPÇÕES ACIMA: '))

opcao1 = produto-(produto*0.1)
opcao2 = produto-(produto*0.05)
opcao3 = produto/2
if pagamento == 1:
    print(f'À vista dinheiro/cheque: 10% de desconto, '
          f'\nVALOR: R${opcao1:.2f}')
elif pagamento == 2:
    print(f'À vista no cartão: 5% de desconto '
          f'\nVALOR: R${opcao2:.2f} ')
elif pagamento == 3:
    print(f'Em até 2x no cartão: preço formal de R${produto:.2f} vai ficar, '
          f'\nR${opcao3:.2f} de 2 vezes')
elif pagamento == 4:
    parcelas = int(input('Digite em quantas parcelas deseja pagar o produto: '))
    total = (produto * 0.2)+produto
    parcelatotal = (total)/parcelas
    print(f'\n3x ou mais no cartão: 20% de juros, '
          f'\nValor Total: R${total:.2f} sendo R${parcelatotal:.2f} de {parcelas} vezes')
else:
    print('OPÇÃO INVALIDA')
