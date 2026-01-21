n1 = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À VISTA/CHEQUE
[2] À VISTA CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MASI NO CATÃO''')
num = int(input('Digite o numero correspondente a opção desejada: '))
if num == 1:
    print('O valor do produto com desconto de 10% é igual a R${:.2f}'.format(n1 - (n1 * 0.10)))
elif num == 2:
    print('No cartão à vista você terá 5% de desconto e o valor a pagar será de {:.2f}'.format(n1 - (n1 * 0.05)))
elif num == 3:
    print('Em até 2x np cartão o preço sera de R${}'.format(n1))
elif num == 4:
    print('Em 3x ou mais no cartão o proço ficará em {:.2f}'.format(n1 + (n1 * 0.20)))


