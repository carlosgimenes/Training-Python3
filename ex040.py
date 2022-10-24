# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 2) por Gustavo Guanabara
# Desafio 040 - Aquele clássico da Média
# Para este Desafio devo ter assistido até a aula 12
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
# Link para a resolução: https://youtu.be/QuWDyUeoaJs
# =================================================================================================

# Como fiz
'''nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(
        'Sua média foi {:.2f} e inferior a 5.0, infelizmente você foi REPROVADO!'.format(media))
elif media >= 5 and media < 7:
    print(
        'Sua média foi {:.2f} e ficou entre 5.0 e 6.9, você ficou em RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('Sua média foi {:.2f} Parabéns, você foi APROVADO!'.format(media))'''


# Como foi resolvido
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(
    nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO')
elif media >= 7:
    print('O aluno está APROVADO.')
