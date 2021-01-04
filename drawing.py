import pygame
from settings import *
from raycasting import ray_casting
from map import mini_map
import random


class Drawing():
    def __init__(self, screen, sc_map, player):
        self.player = player
        self.screeen = screen
        self.sc_map = sc_map
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.textures = {4: pygame.image.load("textures/wall5.png").convert(),
                         666: pygame.image.load("textures/empty1.png").convert(),
                         1: pygame.image.load("textures/wall1.png").convert(),
                         2: pygame.image.load("textures/wall2.png").convert(),
                         "nebo": pygame.image.load("textures/nebo.png").convert(),
                         3: pygame.image.load("textures/wall3.png").convert()
                         }

    # метот отрисовки фона
    def background(self, angle):
        nebo_offset = -5 * math.degrees(angle) % WIDTH
        self.screeen.blit(self.textures["nebo"], (nebo_offset, 0))
        self.screeen.blit(self.textures["nebo"], (nebo_offset - WIDTH, 0))
        self.screeen.blit(self.textures["nebo"], (nebo_offset + WIDTH, 0))
        pygame.draw.rect(self.screeen, WHITE, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    # метод нарисовывания всего
    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda x: x[0], reverse=True):
            if obj[0]:
                #
                _, object, object_pos = obj
                self.screeen.blit(object, object_pos)

    # отрисовка дополнительной информации
    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, (255, 0, 0))
        self.screeen.blit(render, FPS_POS)
        #
        # py = str(int(self.player.y))
        # if self.player.y // TILE >= 18:
        #     render = self.font.render(py, 0, (255, 0, 0))
        #     self.screeen.blit(render, X_POS)
        # else:
        #     render = self.font.render(py, 0, (0, 255, 0))
        #     self.screeen.blit(render, X_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.sc_map, WHITE, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                              map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, (255, 0, 0), (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, WHITE, (x, y, MAP_TILE, MAP_TILE))
        self.screeen.blit(self.sc_map, MAP_POS)
