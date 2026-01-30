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


