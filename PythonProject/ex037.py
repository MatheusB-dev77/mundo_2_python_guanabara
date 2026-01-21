num = int(input('Digite um número'))

print(''' Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num,bin(num)))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num,oct(num)))
elif opção == 3:
    print('{} convertido para Hexadecimal é iagual a {}'.format(num,hex(num)))
else:
    print('Opção inválida.Tente novamnete')