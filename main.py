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

sprites = Sprites()
clock = pygame.time.Clock()
player = Player()
dr = drawing.Drawing(screen, sc_map, player)
mus.play()
pygame.mouse.set_visible(False)
mixer_flag = False
running = True

while running:
    drawing_map = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = not running
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer_flag = not mixer_flag

    player.move()
    screen.fill(BLACK)

    dr.background(player.angle)
    walls = ray_casting(player, dr.textures)
    dr.world(walls + [obj.object_locate(player, walls) for obj in sprites.sprite_objects])
    dr.fps(clock)
    # dr.mini_map(player)
    dr.mixer(mixer_flag)

    pygame.display.flip()
    clock.tick(FPS)
