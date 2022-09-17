# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('****************** BEM VINDO AO JOKENPÔ ******************')

jogador = int(input(' \n[0]PAPEL'
                    ' \n[1]PEDRA'
                    ' \n[2]TESOURA'
                    ' \nDIGITE UMA DAS OPÇÕES ACIMA:  '))

inteiro = ['PAPEL', 'PEDRA', 'TESOURA']
computer = randint(0, 2)

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

if computer == 0:  # PAPEL
    if jogador == 0:
        print(f'\n*********** EMPATE ***********'
              f'\nCOMPUTADOR ESCOLHEU {inteiro[computer]} E VOCÊ {inteiro[jogador]}.')
    elif jogador == 1:
        print(f' \n*********** VOCÊ PERDEU ***********'
              f' \nCOMPUTADOR ESCOLHEU {inteiro[computer]} E VOCÊ {inteiro[jogador]}.')
    elif jogador == 2:
        print(f'\n*********** VOCÊ GANHOU ***********'
              f'\nCOMPUTADOR ESCOLHEU {inteiro[computer]} E VOCÊ {inteiro[jogador]}.')
    else:
        print('\nOPÇÃO INVÁLIDA')


elif computer == 1:  # PEDRA
    if jogador == 0:
        print(f'\n*********** VOCÊ GANHOU ***********'
              f'\nCOMPUTADOR ESCOLHEU {inteiro[computer]} E VOCÊ {inteiro[jogador]}.')
    elif jogador == 1:
        print(f'\n*********** EMPATE ***********'
              f'\nCOMPUTADOR ESCOLHEU {inteiro[computer]} E VOCÊ {inteiro[jogador]}.')
    elif jogador == 2:
        print(f'\n*********** VOCÊ PERDEU ***********'
              f'\nCOMPUTADOR ESCOLHEU {inteiro[computer]} E VOCÊ {inteiro[jogador]}.')
    else:
        print('\nOPÇÃO INVÁLIDA')


elif computer == 2:  # TESOURA
    if jogador == 0:
        print(f'\n*********** VOCÊ PERDEU ***********'
              f'\nCOMPUTADOR ESCOLHEU {inteiro[computer]} E VOCÊ {inteiro[jogador]}.')
    elif jogador == 1:
        print(f'\n*********** VOCÊ GANHOU ***********'
              f'\nCOMPUTADOR ESCOLHEU {inteiro[computer]} E VOCÊ {inteiro[jogador]}.')
    elif jogador == 2:
        print(f'\n*********** EMPATE ***********'
              f'\nCOMPUTADOR ESCOLHEU {inteiro[computer]} E VOCÊ {inteiro[jogador]}.')
    else:
        print('\nOPÇÃO INVÁLIDA')


