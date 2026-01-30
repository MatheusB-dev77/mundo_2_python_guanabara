from datetime import date
ano = date.today().year
for c in range(1, 7):
    nasc = int(input(f'Pessoa {c} — em que ano você nasceu? '))
    idade = ano - nasc

    if idade <= 30:
        print("Você é experiente, mas jovem")
    elif idade <= 40:
        print('Tá chegando a hora kk')
    elif idade <= 50:
        print('Panela velha é que faz comida boa')
    else:
        print('Experiência nível mestre 👑')

#professor gunabara


atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemo {} pessoal menores de idade'.format(totmenor))


