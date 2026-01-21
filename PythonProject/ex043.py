peso = float(input('Qual o seu peso (KG)'))
altura = float(input('Qual a sua altura (m)'))
imc = peso / (altura * altura)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc < 40:
    print('obesidade')
elif imc >= 40:
    print('Obesidade morbida')