# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 006 - Dobro, Triplo, Raiz Quadrada
# Para este Desafio devo ter assistido até a aula 07
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
# Link para a resolução: https://youtu.be/mqcNw_dhl8I
# =================================================================================================

# Como fiz:
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(n, (n*2), (n*3), (n**2)))

# Como foi resolvido
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))