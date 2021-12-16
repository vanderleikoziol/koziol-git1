"""
Faça um algorítimo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

    IMC                     CLASSIFICAÇÃO
<= 18.5                      Abaixo do peso
 18.6 - 24.9                 Saudável
 25.0 - 29.9                 Peso em excesso
 30.0 - 34.9                 Obesidade Grau I
 35.0 - 39.9                 Obesidade Grau II (severa)
    >= 40                     Obesidade Grau III (mórbida)
IMC = Peso ÷ (Altura × Altura)

"""


print('#' * 100)
print('*' * 20)
print('   CALCULO DE IMC')
print('*' * 20)
print()
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso.')
elif 18.5 < imc <= 24.9:
    print(f'Seu IMC é {imc:.2f} e você está saudável.')
elif 24.9 < imc <= 29.9:
    print(f'Seu IMC é {imc:.2f} e você está com peso em excesso.')
elif 29.9 < imc <= 34.9:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade Grau I.')
elif 34.9 < imc <= 39.9:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade Grau II.')
else:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade Grau III.')



