print('\n==================')
print('Calculadora de IMC')
print('==================')
peso = float(input('\nDigite o peso do paciente: '))
altura = float(input('Digite a altura do paciente: '))

imc = peso / altura**2

if imc < 16:
    classificacao = 'Magreza grave'
elif imc < 17:
    classificacao = 'Magreza moderada'
elif imc < 18.5:
    classificacao = 'Magreza leve'
elif imc < 25:
    classificacao = 'Eutrófico'
elif imc < 30:
    classificacao = 'Sobrepeso'
elif imc < 35:
    classificacao = 'Obesidade Grau I'
elif imc < 40:
    classificacao = 'Obesidade Grau II (Severa)'
elif imc >= 40:
    classificacao = 'Obesidade Grau III (Mórbida)'
else:
    classificacao = 'Deu merda'

print(f'\nO IMC do paciente é {round(imc, ndigits=4)} e sua classificação é {classificacao}.')