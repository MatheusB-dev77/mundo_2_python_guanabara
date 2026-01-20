casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador?'))
ano = float(input('Quantos anos de financiamento?'))
prestaçao = casa / (ano * 12)
if prestaçao <= salario * 0.3:
    print ('Seu financiamneto pode ser aprovado!')
elif prestaçao > salario * 0.3:
    print ('Seu financiamento não pode ser reprovado!')

print('Para pagar um casa de R${} em {} anos a prestação será de R${:.2f}'.format(casa, ano, prestaçao, ))

#professor guanabara

casa = float(input('Qual o valor da casa? '))
salário = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 0.30
print('Para pagar um casa de R${:.2f} em {} anos'.format(casa, anos,),end='')
print(' a pretação será de R${:.2}'.format(prestação))
if prestação <= mínimo:
    print('Seu financiamento pode ser aprovado!')
else:
    print('Empréstimo negado!')
