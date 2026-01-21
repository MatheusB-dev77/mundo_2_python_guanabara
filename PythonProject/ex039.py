from datetime import date

n1 = int(input('Ano de nascimento: '))
n2 = date.today().year - n1
if n2 == 18:
    print('Você está na idade correta para se alistar')
elif n2 < 18:
    print('Você não está na idade certa para se alistar, pois você tem {} anos.'.format(n2))
    print('Seu alistamento será somente em {} quando completará 18 anos'.format(date.today().year + (18 - n2)))
elif n2 > 18:
    print('Já passou da hora de você se alistar Soldado, pois seu alistamento deveria ser feito em {}'
          .format(date.today().year - (n2 - 18)))
#professor guanabara

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {}anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {}anos para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(atual))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    saldo = atual - saldo
    print('Seu alistamento foi em {}.'.format(atual))




