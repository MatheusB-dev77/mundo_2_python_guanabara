n = float(input('Digite o valor do lado:'))
m = float(input('Digite o valor do outro lado:'))
o = float(input('Digite o valor do outro lado:'))

if  n < m + o and m < n + o and o < m + n:
    print('É um trângulo')
    if n == m and m == o:
        print('Todos os lados são iguais.')
        print('É um triângulo equilatero')
    elif n == m or n == o or m == o:
        print('Dois lados são iguais e um diferente')
        print('É um triângulo isósceles')
    elif n != m and m != o and o != n:
        print('Três lados diferentes')
        print('Você tem um triagulo Escaleno')
else:
    print('Não foi possível formar um triângulo')

#professor guanabara

r1 = float(input('Digite o valor do segmento:'))
r2 = float(input('Digite o valor do segmento:'))
r3 = float(input('Digite o valor do segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um trângulo')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isoceles')







