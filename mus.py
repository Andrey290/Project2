from os import path
import pygame

snd_dir = path.join(path.dirname(__file__), 'music')
playlist = ['auto-nward.mp3', 'auto-glass-ocean-lost-boys.mp3']


def play():
    for i, soundtrack in enumerate(playlist):
        if i == len(playlist):
            play()
        else:
            pygame.mixer.music.load(path.join(snd_dir, soundtrack))
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
