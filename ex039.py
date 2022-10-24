# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 2) por Gustavo Guanabara
# Desafio 039 - Alistamento Militar
# Para este Desafio devo ter assistido até a aula 12
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
# Link para a resolução: https://youtu.be/ePwP4gU_waY
# =================================================================================================

# Como fiz
'''from datetime import date

nascimento = int(input('Informe o ano de seu nascimento: '))
ano = date.today().year
idade = ano - nascimento
prazo = 18 - idade
if idade < 18:
    print('Quem tem {} anos ainda não atigiu a idade obrigatória para Alistamento Militar'.format(idade))
    print('Você ainda tem {} anos para se Alistar'.format(prazo))
elif idade > 18:
    print('Quem tem {} anos já PASSOU da idade obrigatória para Alistamento Militar'.format(idade))
    print('Já passou {} anos do prazo para Alistamento'.format(prazo))
else:
    print('Quem tem {} anos deve se apresentar para o Alistamento Militar'.format(idade))
    print('Você ainda tem {} anos para se Alistar'.format(prazo))'''


# Como foi resolvido
from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o Alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se Alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
