
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


