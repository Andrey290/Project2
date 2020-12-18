from os import path
import pygame

snd_dir = path.join(path.dirname(__file__), 'music')


def play():
    pygame.mixer.music.load(path.join(snd_dir, 'auto-nward.mp3'))
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
