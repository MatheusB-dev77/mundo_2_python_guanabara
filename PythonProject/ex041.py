
print('Bem Vindo a Confederação de Natação de Jundiai caro Estudante ! '.center(100))

print('\n')

idade = int(input('\033[1;36mDigite a sua idade para ver em qual categoria você se enquadra:\033[m '))

if idade <= 9:
    print('Categoria: \033[1;32mMIRIM\033[m ')
elif idade <= 14:
    print('Categoria: \033[1;34mINFANTIL\033[m')
elif idade <= 25:
    print('Categoria: \033[1;35mSENIOR\033[m')
elif idade > 25:
    print('Categoria: \033[1;31mMASTER\033[m')

#professor guanabara
from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento:'))
idade = atual - nascimento

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR ')
elif idade <= 25:
    print('categoria: SÊNIOR')
elif idade > 25:
    print('categoria: MASTER')




