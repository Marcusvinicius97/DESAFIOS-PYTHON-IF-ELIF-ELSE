#A Confederação Nacional de Natação precisa de um
# programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date

NASCIMENTO = int(input('Digite o seu ano de nascimento: '))

ATUAL = date.today().year
CAT = ATUAL - NASCIMENTO

if CAT <= 9:
    print(f'Sua categoria é a MIRIM')
elif 14>= CAT > 9:
    print(f'Sua categoria é a INFANTIL')
elif 19>= CAT > 14:
    print(f'Sua categoria é a JÚNIOR')
elif 25>= CAT > 19:
    print(f'Sua categoria é a SÉNIOR')
elif CAT > 25:
    print(f'Sua categoria é a MASTER')

