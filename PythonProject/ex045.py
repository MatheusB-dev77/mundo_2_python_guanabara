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


#professor guanabara
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('\n')
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('\n')
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Computador Venceu!')
    else:
        print('Jogada invalida!')
elif computador == 1:
    if jogador == 0:
        print('Computador VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VECEU!')
    else:
        print('Jogada invalida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Computador VENCEU!')
    else:
        print('Jogada invalida!')



