import pygame
from settings import *
from player import Player
from sprites_logic import *
from raycasting import ray_casting
import drawing
import mus

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))

# спрайты
sprites = Sprites()
# фремя
clock = pygame.time.Clock()
# объект игрока
player = Player()
# объект класса рисование из файла рисование что непонятного то
dr = drawing.Drawing(screen, sc_map, player)
# играние музыки
mus.play()
# убирание курсора
pygame.mouse.set_visible(False)
# помехи(переделать или убрать в будущем)
mixer_flag = False

running = True
while running:
    drawing_map = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = not running
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer_flag = not mixer_flag # включение помехов на клавишу р

    player.move()
    screen.fill(BLACK)

    # рисование
    # рисование фона
    dr.background(player.angle)

    # получение изображения
    walls = ray_casting(player, dr.textures)
    # нарисовывание стен + спрайтов
    dr.world(walls + [obj.object_locate(player, walls) for obj in sprites.sprite_objects])
    # фпс
    dr.fps(clock)
    # помехи
    dr.mixer(mixer_flag)

    pygame.display.flip()
    clock.tick(FPS)
