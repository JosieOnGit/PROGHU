
import pygame

pygame.mixer.init()
pygame.mixer.music.load("Win7Boot.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy:
    continue
