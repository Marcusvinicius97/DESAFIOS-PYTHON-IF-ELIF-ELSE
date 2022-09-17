#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

N = int(input('Digite o seu ano de nascimento: '))

Atual = date.today().year
Data = Atual - N
Atraso = Data-18
Adiantado = -(Data-18)

if Data == 18:
    print(f'Você está aprovado para se alistar ao exercito')
elif Data > 18:
    print(f'Sua data de alistamento já passou do prazo, você está atrasado já tem {Atraso} ano(s)')
else:
    print(f'Você ainda não está apito ao alistamento, para se alistar aguarde {Adiantado} ano(s)')

