import pygame
from settings import *
from map import world_map, WORLD_WIDTH, WORLD_HEIGHT


# функция нахождения координат левого верхнего угла
def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(player, textures):
    walls = []
    x0, y0 = player.pos  # начальные координаты всех лучей
    xm, ym = mapping(x0, y0)  # координаты левого верхнего угла квадрата, в котором мы находимся в днный момент
    cur_angle = player.angle - HALF_FOV  # самый левый луч относительно игрока(текущий угол)
    # в цикле проходим по всем лучам, вычисляя их...
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)  # синус
        cos_a = math.cos(cur_angle)  # косинус

        # номер текстуры края карты (которая с Тедом Нельсоном и html)
        texture_v = 666
        texture_h = 666

        # рассмотрим пересечение с вертикалями
        if cos_a >= 0:
            x = xm + TILE  # текущая рассматриваемая вертикаль
            dx = 1
        else:
            x = xm
            dx = -1
        for i in range(0, WORLD_WIDTH, TILE):
            depth_v = (x - x0) / cos_a  # расстояние до вертикали
            yv = y0 + depth_v * sin_a  # координата y пересечения
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map: # проверка на столкновение со стеной
                texture_v = world_map[tile_v]
                break
            x += dx * TILE
        # рассмотрим пересечение с горизонталями
        if sin_a >= 0:
            y = ym + TILE  # текущая рассматриваемая горизонталь
            dy = 1
        else:
            y = ym
            dy = -1
        for i in range(0, WORLD_HEIGHT, TILE):
            depth_h = (y - y0) / sin_a # расстояние до горизонтали
            xh = x0 + depth_h * cos_a # координата y пересечения
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map: # проверка на столкновение со стеной
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        if texture_v and texture_h:
            # определяем, какая пересечение в данный момент ближе к нам
            depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
            # оффсет- смещение на текстуре
            offset = int(offset) % TILE
            depth *= math.cos(player.angle - cur_angle)  # расстояние до объекта
            depth = 0.000001 if not depth else depth
            proj_height = min(int(PROJ_COEFF / depth), HEIGHT_COMP_5)  # проекционная высота
            # создаём субповерхность с куском текстуры по нашеё формуле
            wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
            # трансформируем изображение
            wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
            wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            walls.append((depth, wall_column, wall_pos))
        cur_angle += DELTA_ANGLE  # изменяем угол рассчёта для нового угла(прибавляем дельта_угол)
    return walls
