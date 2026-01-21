n = float(input('Digite o valor do lado:'))
m = float(input('Digite o valor do outro lado:'))
o = float(input('Digite o valor do outro lado:'))

if  n < m + o and m < n + o and o < m + n:
    print('É um trângulo')
if n == m and m == o:
    print('Todos os lados são iguais.')
    print('É um triângulo equilatero')
elif n == m and o != m:
    print('Dois lados são iguais e um diferente')
    print('É um triângulo isósceles')
elif n != m and m != o and o != n:
    print('Três lados diferentes')
    print('Você tem um triagulo Escaleno')
