# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 011 - Pintando Parede
# Para este Desafio devo ter assistido até a aula 07
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área 
# de 2m2
# Link para a resolução: https://youtu.be/mzSJpn9ldt4
# =================================================================================================

# Como fiz:
largura = float(input('Informe a Largura da parede: '))
altura = float(input('Informe a Altura da parede> '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f} m2'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tinta))

# Como foi resolvido
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(larg, alt, area))