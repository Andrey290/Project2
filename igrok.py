from pygame import *
import pygame

MOVE_SPEED = 1
hero = pygame.image.load("igor.jpg")


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((40, 40))
        self.image.blit(hero, (0, 0))
        self.rect = Rect(x, y, 40, 40)  # прямоугольный объект

    def update(self, left, right, up, down):
        # движение
        if left:
            self.xvel = -1

        if right:
            self.xvel = 1

        if up:
            self.yvel = -1
        if down:
            self.yvel = 1
        # остновка движения
        if not (left or right):
            self.xvel = 0
        if not (up or down):
            self.yvel = 0
        # итоговая разница

        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def draw(self, screen):  # вывод на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))
