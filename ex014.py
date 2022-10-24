# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 014 - Conversor de Temperaturas
# Para este Desafio devo ter assistido até a aula 07
# Escreva um programa que converta uma temperatura digitada em °C e converta para °F
# Link para a resolução: https://youtu.be/9l_Gay8BuAw
# =================================================================================================

# Como fiz:
celcius = float(input('Digite a temperatura em °C: '))
fareheint = ( celcius * 1.8 ) + 32

print('A conversão de {:.1f}ºC corresponde a {:.1f}°F'.format(celcius, fareheint))

# Como foi resolvido
c = float(input('Informe a temperatura em °C:'))
f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))