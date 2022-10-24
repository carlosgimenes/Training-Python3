# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 007 - Média Aritmética
# Para este Desafio devo ter assistido até a aula 07
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
# Link para a resolução: https://youtu.be/_QfISzy0IKs
# =================================================================================================

# Como fiz:
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = ( nota1 + nota2 ) / 2
print('A média é {:.2f}'.format(media))

# Como foi resolvido
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno; '))
media = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))