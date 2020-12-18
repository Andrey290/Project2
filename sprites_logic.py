from settings import *
import pygame


# класс, хранящий информацию о спрайтах
class Sprites:
    def __init__(self):
        # список(зачёркнуто)словарь изображений спрайтов
        self.sprite_types = {
            "colon1": pygame.image.load("textures/sprites/colon1.png").convert_alpha()
        }
        # список самих объектов
        self.sprite_objects = [
            SpriteObject(self.sprite_types["colon1"], True, (5.1, 1.1), 0.15, 1.2)
        ]

# класс, всесторонне описывающий объект спрайта
class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.shift = shift
        self.scale = scale

    # функция, отвечающая за локацию спрайта
    def object_locate(self, player, walls):
        # шахматное расстояниие до спрайта
        dx, dy = self.x - player.x, self.y - player.y
        # расстояние до спрайта напрямую
        dist_to_sprt = math.sqrt(dx ** 2 + dy ** 2)
        # см рисунок
        theta = math.atan2(dy, dx)
        # см рисунок
        gamma = theta - player.angle
        # так надо
        if dx > 0 and 180 < math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += math.pi * 2

        # смщение срайта
        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        # убирание эффекта рыбьего глаза забей (я сам не понимаю, как это работает)
        dist_to_sprt *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        # проверка на то, что //спрайт в зоне видимости// и //его не закрывает стена//
        if 0 <= current_ray <= NUM_RAYS - 1 and dist_to_sprt < walls[current_ray][0]:
            # проекционная высота спрайта
            proj_height = int(PROJ_COEFF / dist_to_sprt * self.scale)
            # кофециент  масштабирования
            half_proj_height = proj_height // 2
            # высота спрайта
            shift = half_proj_height * self.shift

            # рассчёт дислокации спрайта на экране
            sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            # перерассчёт размеров спрайта
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            # сие идёт в рейкаст функцию  (сначала в world в двоувинге)
            return (dist_to_sprt, sprite, sprite_pos)
        return (False,)
