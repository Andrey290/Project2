from settings import *
import pygame

_ = False # ничто
matrix_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, _, _, _, _, _, _, _, _, 1],
               [1, _, _, _, _, _, _, _, _, 1],
               [1, _, _, _, _, _, _, _, _, 1],
               [1, _, _, _, _, _, _, _, _, 1],
               [_, _, _, _, _, _, _, _, _, 1],
               [1, _, _, _, 4, _, _, _, _, 1],
               [1, _, _, 3, 3, _, _, _, _, 1],
               [1, _, _, _, 2, _, _, 4, _, 1],
               [1, _, _, _, _, _, _, _, _, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = {}  # каардинады стен и их тикстурный номер на риальной карте
mini_map = set()  # координаты стен на менекарте
collision_walls = []
for j, row in enumerate(matrix_map):
    for i, char in enumerate(row):
        if char:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = 1
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = 2
            elif char == 3:
                world_map[(i * TILE, j * TILE)] = 3
            elif char == 4:
                world_map[(i * TILE, j * TILE)] = 4
