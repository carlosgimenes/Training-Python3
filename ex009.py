# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 009 - Tabuada
# Para este Desafio devo ter assistido até a aula 07
# Faça um programa que leia um número Inteiro qualquer e mostre na tela sua tabuada
# Link para a resolução: https://youtu.be/qajq3SI0QQs
# =================================================================================================

# Como fiz:
t = int(input('Digite um número para ver sua tabuada: '))
print('{:=^20}'.format(''))
print('{} x 1 = {}'.format(t, (t * 1)))
print('{} x 2 = {}'.format(t, (t * 2)))
print('{} x 3 = {}'.format(t, (t * 3)))
print('{} x 4 = {}'.format(t, (t * 4)))
print('{} x 5 = {}'.format(t, (t * 5)))
print('{} x 6 = {}'.format(t, (t * 6)))
print('{} x 7 = {}'.format(t, (t * 7)))
print('{} x 8 = {}'.format(t, (t * 8)))
print('{} x 9 = {}'.format(t, (t * 9)))
print('{} x 10 = {}'.format(t, (t * 10)))
print('{:=^20}'.format(''))

# Como foi resolvido
num = int(input('Digite um número para ver sua tabuada: '))
print('=' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('=' * 12)