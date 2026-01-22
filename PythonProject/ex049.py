n = int(input('Digite um numero para saber sua tabuada:'))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, c * n))

#professor guanabara

num = int(input('digite um número para ver sua tabuada:'))
for c in range(1,11):
    print('{} x {} = {:.2f}'.format(num, c, c * num))