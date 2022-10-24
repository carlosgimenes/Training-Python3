# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 035 - Analisando Triângulo v1.0
# Para este Desafio devo ter assistido até a aula 10
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não 
# formar um triângulo
# Link para a resolução: https://youtu.be/NZiNphKkxhg
# =================================================================================================

# Como foi resolvido
print('-=-' * 20)
print('Analisador de Triângulos v1.0')
print('-=-' * 20)
segmento1 = float(input('Informe o primeiro segmento: '))
segmento2 = float(input('Informe o segundo segmento: '))
segmento3 = float(input('Informe o terceiro segmento: '))

maior = segmento1
if segmento2 + segmento3 > segmento1 or segmento1 + segmento3 > segmento2 or segmento1 + segmento2 > segmento3:
  print('Os segmentos acima PODEM FORMAR um triângulo!')


# Como foi resolvido
'''# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))'''