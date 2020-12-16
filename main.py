import pygame
from settings import *
from player import Player
import math
from map import world_map
from raycasting import ray_casting
import drawing
import mus

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
dr = drawing.Drawing(screen, sc_map)
mus.play()

flag = False
running = True
while running:
    drawing_map = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = not running
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(1)
                flag = not flag

    player.move()
    screen.fill(BLACK)

    dr.background(player.angle)
    dr.world(player.pos, player.angle)
    dr.fps(clock)
    # dr.mini_map(player)
    dr.mixer(flag)

    pygame.display.flip()
    clock.tick(FPS)
