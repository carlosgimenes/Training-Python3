# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 2) por Gustavo Guanabara
# Desafio 041 - Classificando Atletas
# Para este Desafio devo ter assistido até a aula 12
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
# Link para a resolução: https://youtu.be/ZiC5NgSGJXU
# =================================================================================================

# Como fiz
'''from datetime import date
print('->-' * 30)
print('Confederação Nacional de Natação - Analisador de Categoria v1.0')
print('-<-' * 30)
nascimento = int(input('Informe o ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Este atleta se enquadra na categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Este atleta se enquadra na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Este atleta se enquadra na categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print('Este atleta se enquadra na categoria SÊNIOR')
elif idade > 25:
    print('Este atleta se enquadra na categoria MASTER')'''


# Como foi resolvido
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
