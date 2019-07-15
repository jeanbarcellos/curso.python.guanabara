# Faça um programa em Pytho que abra e reproduza o áudio de um arquivo mp3

import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

pygame.init()
pygame.event.wait()
