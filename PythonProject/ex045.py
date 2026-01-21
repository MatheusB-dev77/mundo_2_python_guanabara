from random import choice
print('''Suas opções:
\033[31m[0] Pedra\033[m
\033[32m[1] Papel\033[m
\033[34m[2] Tesoura\033[m
''')
num = int(input('Sua escolha: '))
itens = ('Pedra', 'Papel', 'Tesoura')
sorteador = choice(itens)

print('A escolha do computador foi {}'.format(sorteador))
if sorteador == 'Pedra':
    if num == 0:
        print('EMPATE')
    elif num == 1:
        print('Papel vence Pedra. Você PERDEU!')
    elif num == 2:
        print('Pedra vence Tesoura. Você VENCEU!')
elif sorteador == 'Papel':
    if num == 0:
        print('Papel vence Pedra. Você PERDEU!')
    elif num == 1:
        print('EMPATE')
    elif num == 2:
        print('Papel perde para Tesoura. Você VENCEU!')
elif sorteador == 'Tesoura':
    if num == 0:
        print('Pedra vence Tesoura. Você VENCEU!')
    elif num == 1:
        print('Tesoura vence Papel. Você PERDEU!')
    elif num == 2:
        print('EMPATE')



