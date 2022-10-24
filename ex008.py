# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 008 - Conversor de Medidas
# Para este Desafio devo ter assistido até a aula 07
# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
# Link para a resolução: https://youtu.be/KjcdG05EAZc
# =================================================================================================

# Como fiz:
n = float(input('Informe um valor em Metros: '))
print('Analisando o valor {}, sua conversão para Centrimentos é {:.0f} CM e sua conversão para Milimetros é {:.0f} MM'.format(n, (n*100), (n*1000)))

# Como foi resolvido
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))