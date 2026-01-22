for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 != 0:
            print(c, end=',')

print()
print('FIM')

#professor guanabara
soma = 0 #soma o valores entre si
cont = 0 #conta quantos valores tem
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
