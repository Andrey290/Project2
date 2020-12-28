from settings import *
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_position
        self.angle = player_angle

    # свойство, которое возвращает позицию по x и y
    @property
    def pos(self):
        return (self.x, self.y)

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x -= player_speed * cos_a
            self.y -= player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y -= player_speed * cos_a
        if keys[pygame.K_d]:
            self.x -= player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_q]:
            self.angle -= angle_speed
        if keys[pygame.K_e]:
            self.angle += angle_speed

        self.angle %= math.pi * 2
