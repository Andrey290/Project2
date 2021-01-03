import pygame
from settings import *
from player import Player
from sprites_logic import *
from raycasting import ray_casting
import drawing
import mus

pygame.init()
pygame.display.set_caption(
    "Knights of the Net'")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface(MINIMAP_RES)

# спрайты
sprites = Sprites()
# фремя
clock = pygame.time.Clock()
# объект игрока
player = Player(sprites)
# объект класса рисование из файла рисование что непонятного то
dr = drawing.Drawing(screen, sc_map, player)
# играние музыки
mus.play()
# настройки курсора
all_sprites = pygame.sprite.Group()
cur_im = pygame.image.load("textures\cur1.png").convert()
cur = pygame.sprite.Sprite(all_sprites)
cur_im.set_colorkey(WHITE)
cur.image = cur_im
cur.rect = cur.image.get_rect()
pygame.mouse.set_visible(False)
# помехи(переделать или убрать в будущем)
mixer_flag = False

running = True
while running:
    drawing_map = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_END:
            running = not running
        if event.type == pygame.MOUSEMOTION:
            cur.rect.topleft = event.pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer_flag = not mixer_flag  # включение помехов на клавишу р

    player.movement()
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
    dr.fps(clock)
    # помехи
    dr.mixer(mixer_flag)
    # dr.mini_map(player)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
