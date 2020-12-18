import pygame
from settings import *
from map import world_map


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(player, textures):
    walls = []
    x0, y0 = player.pos
    xm, ym = mapping(x0, y0)
    cur_angle = player.angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        texture_v = "0"
        texture_h = "0"

        if cos_a >= 0:
            x = xm + TILE
            dx = 1
        else:
            x = xm
            dx = -1
        for i in range(0, WIDTH, TILE):
            depth_v = (x - x0) / cos_a
            yv = y0 + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TILE

        if sin_a >= 0:
            y = ym + TILE
            dy = 1
        else:
            y = ym
            dy = -1
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - y0) / sin_a
            xh = x0 + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        if texture_v and texture_h:
            depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
            offset = int(offset) % TILE
            depth *= math.cos(player.angle - cur_angle)
            depth = 0.00001 if not depth else depth
            proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)
            wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
            wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
            wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            walls.append((depth, wall_column, wall_pos))
        cur_angle += DELTA_ANGLE
    return walls