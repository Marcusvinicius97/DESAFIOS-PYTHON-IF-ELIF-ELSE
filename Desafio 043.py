#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
#–IMC abaixo de 18,5: Abaixo do Peso
#–Entre 18,5 e 25: Peso Ideal
#–25 até 30: Sobrepeso
#–30 até 40: Obesidade
#–Acima de 40: Obesidade Mórbida
#Aula Anterior

peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite a sua altura em metros e centimetros: '))

calculo = peso/(altura**2)

if calculo < 18.5:
    print(f"Seu IMC foi {calculo:.2f}: ABAIXO DO PESO")
elif 18.5 <= calculo <= 25:
    print(f'Seu IMC foi {calculo:.2f}: PESO IDEAL')
elif 25 < calculo <= 30:
    print(f'Seu IMC foi {calculo:.2f}: SOBREPESO')
elif 30 < calculo <= 40:
    print(f'Seu IMC foi {calculo:.2f}: OBESIDADE')
elif 40 < calculo:
    print(f'Seu IMC foi {calculo:.2f}: OBSEDIDADE MÓRBIDA')

