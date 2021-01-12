import pygame
from settings import *
import settingsQT
from player import Player
from sprites_logic import *
from raycasting import ray_casting
import drawing
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
import sqlite3
import datetime as dt
from settingsQT import *

pygame.init()
pygame.display.set_caption(
    "3D SCENE")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface(MINIMAP_RES)

# настроечное окно
ex = StWi()
ex.hide()
# спрайты
sprites = Sprites()
# фремя
clock = pygame.time.Clock()
# объект игрока
player = Player(sprites)
# объект класса рисование из файла рисование что непонятного то
dr = drawing.Drawing(screen, sc_map, player)
# настройки курсора
all_sprites = pygame.sprite.Group()
cur_im = pygame.image.load("textures/cur1.png")
cur = pygame.sprite.Sprite(all_sprites)
cur_im.set_colorkey(WHITE)
cur_im.convert()
cur.image = cur_im
cur.rect = cur.image.get_rect()
pygame.mouse.set_visible(False)
# помехи(переделать или убрать в будущем)
pygame.mixer.music.load('music/1.mp3')
pygame.mixer.music.play(-1)
sound_coord_x, sound_coord_y = 3, 3

running = True
gameplay = 0
while running:
    if gameplay == 1:
        drawing_map = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_END]:
                gameplay = 0
            if event.type == pygame.MOUSEMOTION:
                cur.rect.topleft = event.pos
        player.movement()
        volume = 25 / ((abs(player.x - sound_coord_x) ** 2 + abs(player.y - sound_coord_y) ** 2)) ** 0.5
        pygame.mixer.music.set_volume(volume)
        screen.fill(BLACK)
        # рисование
        # рисование фона
        dr.background(player.angle)

        # получение изображения
        walls = ray_casting(player, dr.textures)
        # нарисовывание стен + спрайтов
        dr.world(walls + [obj.object_locate(player, walls) for obj in sprites.sprite_objects])
        # открисовка курсора (включать только в меню и на экранах терминалов)
        # if pygame.mouse.get_focused():
        #     all_sprites.draw(screen)
        # фпс
    elif gameplay == 0:
        pygame.mixer.music.set_volume(0)
        fon = pygame.transform.scale(pygame.image.load('textures/fon.jpg'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 60)
        for line in intro_text:
            string_rendered = font.render(line[0], True, pygame.Color('black'), line[1])
            intro_rect = string_rendered.get_rect()
            intro_rect.top = line[2]
            intro_rect.x = 250
            screen.blit(string_rendered, intro_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                cur.rect.topleft = event.pos
                for line in intro_text:
                    if 60 + line[2] > cur.rect.y > line[2] and 650 >= cur.rect.x >= 250:
                        line[1] = VIRIDIAN
                    else:
                        line[1] = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, line in enumerate(intro_text):
                    if line[1]:
                        if i == 0:
                            gameplay = 1
                        if i == 1:
                            ex.show()
                        if i == 2:
                            running = False

        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
    dr.fps(clock)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
