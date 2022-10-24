# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 005 - Antecessor e Sucessor
# Para este Desafio devo ter assistido até a aula 07
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as 
# informações sobre ele
# Link para a resolução: https://youtu.be/664e0G_S9nU
# =================================================================================================

# Como fiz:
n1 = int(input('Digite um número: '))
antecessor = n1 - 1
sucessor = n1 + 1
print('Analisando o valor {}, seu antecessor é {}, e o sucessor é {}'.format(n1, antecessor, sucessor))

# Como foi resolvido
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))