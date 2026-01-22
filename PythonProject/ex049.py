n = int(input('Digite um numero para saber sua tabuada:'))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, c * n))