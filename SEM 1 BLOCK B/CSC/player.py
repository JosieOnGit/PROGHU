
import pygame

pygame.mixer.init()
pygame.mixer.music.load("REC007.wav")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy:
    continue
