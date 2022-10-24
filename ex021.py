# =================================================================================================
# Curso em Vídeo - Curso Python (Mundo 1) por Gustavo Guanabara
# Desafio 021 - Tocando um MP3
# Para este Desafio devo ter assistido até a aula 08
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
# Link para a resolução: https://youtu.be/9FiEji_fzvk
# =================================================================================================

# Como foi resolvido
# 1º Alternativa
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()