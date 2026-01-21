n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 8:
    print('Parabén pelo seu excelente trabalho! Sua nota {}'.format(media))
elif media >= 7:
    print('Suas nostas foram {} e {} e voce aprovado com média {}.'.format(n1, n2, media))
elif media >= 5 and media < 7:
    print('Infelizmente você não conseguiu corresponder com as expectativas e sua media foi {}'.format(media))
    print('Recuperação')
elif media < 5:
    print('Reprovado')

#professor guanabara

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2, média))
if 7 > média >= 5:
    print('O aluno está em recuperação')
elif média < 5:
    print('O aluno está REPRVADO.')
elif média <= 7:
    print('O aluno está reprovado')

