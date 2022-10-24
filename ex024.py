# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 024 - Verificando as primeiras letras de um texto
# Para este Desafio devo ter assistido até a aula 09
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
# Link para a resolução: https://youtu.be/QroT8cZMRnc
# =================================================================================================

# Como foi resolvido
# 1º Alternativa
cidade = str(input('Em que cidade voê nasceu? ')).strip() # O MÉTODO strip irá remover espaços em branco 
print(cidade[:5].upper() == 'SANTO') # O upper irá passar o texto para Maiúscula para comparar 