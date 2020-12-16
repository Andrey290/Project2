import pygame
from settings import *
from raycasting import ray_casting
from map import mini_map
import random


class Drawing():
    def __init__(self, screen, sc_map):
        self.screeen = screen
        self.sc_map = sc_map
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.textures = {"3": pygame.image.load("textures/wall3.png").convert(),
                         "0": pygame.image.load("textures/empty.png").convert(),
                         "1": pygame.image.load("textures/wall1.png").convert(),
                         "2": pygame.image.load("textures/wall2.png").convert(),
                         "4": pygame.image.load("textures/wall4.png").convert(),
                         "nebo": pygame.image.load("textures/nebo.png").convert(),
                         "ms": pygame.image.load("textures/morningstar.png").convert(),
                         "vhs1": pygame.image.load("textures/vhs1.png").convert(),
                         }

    def background(self, angle):
        nebo_offset = -5 * math.degrees(angle) % WIDTH
        self.screeen.blit(self.textures["nebo"], (nebo_offset, 0))
        self.screeen.blit(self.textures["nebo"], (nebo_offset - WIDTH, 0))
        self.screeen.blit(self.textures["nebo"], (nebo_offset + WIDTH, 0))
        morning_star = self.textures["ms"]
        morning_star.set_colorkey(BLACK)
        self.screeen.blit(self.textures["ms"], (WIDTH // 4, 0))
        pygame.draw.rect(self.screeen, (255, 255, 255), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    def world(self, player_pos, player_angle):
        ray_casting(self.screeen, player_pos, player_angle, self.textures)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, (255, 0, 0))
        self.screeen.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.sc_map, (255, 0, 0), (int(map_x), int(map_y)),
                         (map_x + 12 * math.cos(player.angle), map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, (255, 0, 0), (int(map_x), int(map_y)), 5)
        for coord in mini_map:
            pygame.draw.rect(self.sc_map, (255, 0, 0), (coord[0], coord[1], MAP_TILE, MAP_TILE), 2)
        self.screeen.blit(self.sc_map, (0, (HEIGHT - HEIGHT // MAP_SCALE)))

    def mixer(self, flag):
        if flag:
            for _ in range(random.randrange(50, 250)):
                params = [("red", (255, 0, 0), random.randrange(10, 100), random.randrange(2, 5)),
                          ("green", (0, 255, 0), random.randrange(10, 200), random.randrange(1, 3)),
                          ("blue", (0, 0, 255), random.randrange(10, 200), random.randrange(1, 3)),
                          ("white", (255, 255, 255), random.randrange(10, 200), random.randrange(1, 3)),
                          ("pink", (200, 0, 200), random.randrange(10, 200), random.randrange(1, 3))]
                for color in params:
                    h = random.randrange(0, HEIGHT)
                    w = random.randrange(0, WIDTH)
                    lenth = color[2]
                    fat = color[3]
                    pygame.draw.line(self.screeen, color[1], (w, h), (w + lenth, h), fat)
