from settings import *
import pygame
from collections import deque
from raycasting import *


# класс, хранящий информацию о спрайтах
class Sprites:
    def __init__(self):
        # словарь словарей со спрайтами
        self.sprite_params = {
            "sprite_fire": {
                "sprite": pygame.image.load("textures/sprites/fire/base/fire.png").convert_alpha(),
                "viewing_angles": None,
                "shift": 1.8,
                "scale": 0.4,
                "animation": deque(
                    [pygame.image.load(f"textures/sprites/fire/anim/{i}.png").convert_alpha() for i in range(10)]),
                "animation_dist": 1000,
                "animation_speed": 10,
                "blocked": False,
                "flag": "not_door"
            },
            "sprite_colon": {
                "sprite": pygame.image.load("textures/sprites/colons/base/colon.png").convert_alpha(),
                "viewing_angles": None,
                "shift": 0,
                "scale": 1.5,
                "animation": deque(
                    [pygame.image.load(f"textures/sprites/fire/anim/{i}.png").convert_alpha() for i in range(0)]),
                "animation_dist": 1000,
                "animation_speed": 10,
                "blocked": True,
                "flag": "not_door"
            },
            "sprite_comp": {
                "sprite": [pygame.image.load(f"textures/sprites/computors/angled/{i}2.png").convert_alpha() for i in
                           range(8)],
                "viewing_angles": True,
                "shift": 0.6,
                "scale": 0.8,
                "animation": deque(
                    [pygame.image.load(f"textures/sprites/fire/anim/{i}.png").convert_alpha() for i in range(0)]),
                "animation_dist": 1000,
                "animation_speed": 10,
                "blocked": True,
                "flag": "not_door"
            },
            "sprite_eye": {
                "sprite": pygame.image.load("textures/sprites/eye/base/0.png").convert_alpha(),
                "viewing_angles": None,
                "shift": 0.2,
                "scale": 1,
                "animation": deque(
                    [pygame.image.load(f"textures/sprites/eye/anim/0{i}.png").convert_alpha() for i in range(12)]),
                "animation_dist": 1000,
                "animation_speed": 10,
                "blocked": True,
                "flag": "not_door"
            }
        }

        # список самих объектов
        # (параметры, (x, y))
        self.sprite_objects = [
            SpriteObject(self.sprite_params["sprite_comp"], (3, 4)),
            SpriteObject(self.sprite_params["sprite_comp"], (2, 4)),
            SpriteObject(self.sprite_params["sprite_comp"], (3, 3)),
            SpriteObject(self.sprite_params["sprite_comp"], (2, 3)),
            SpriteObject(self.sprite_params["sprite_comp"], (3, 5)),
            SpriteObject(self.sprite_params["sprite_comp"], (2, 5)),
            SpriteObject(self.sprite_params["sprite_eye"], (1.3, 1.3)),

        ]

    # класс, всесторонне описывающий объект спрайта


class SpriteObject:
    def __init__(self, parameters, pos):
        self.object = parameters['sprite']
        self.viewing_angles = parameters['viewing_angles']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation']
        self.animation_dist = parameters['animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.animation_count = 0
        self.blocked = parameters['blocked']
        self.side = 30
        self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.pos = self.x - self.side // 2, self.y - self.side // 2

        if self.viewing_angles:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(-23, 316, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    # функция, отвечающая за локацию спрайта
    def object_locate(self, player, walls):
        fake_walls0 = [walls[0] for _ in range(FAKE_RAYS)]
        fake_walls1 = [walls[-1] for _ in range(FAKE_RAYS)]
        fake_walls = fake_walls0 + walls + fake_walls1

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
        theta -= 1.4 * gamma

        # смщение срайта
        delta_rays = int(gamma / DELTA_ANGLE)
        current_ray = CENTER_RAY + delta_rays
        # убирание эффекта рыбьего глаза забей (я сам не понимаю, как это работает)
        dist_to_sprt *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        fake_ray = current_ray + FAKE_RAYS
        # проверка на то, что //спрайт в зоне видимости// и //его не закрывает стена//
        if 0 <= fake_ray <= NUM_RAYS - 1 + 2 * FAKE_RAYS and dist_to_sprt < fake_walls[fake_ray][0]:
            # проекционная высота спрайта
            if dist_to_sprt * self.scale:
                proj_height = min(int(PROJ_COEFF / dist_to_sprt * self.scale),2 * HEIGHT)
            else:
                proj_height = 2 * HEIGHT
            # кофециент  масштабирования
            half_proj_height = proj_height // 2
            # высота спрайта
            shift = half_proj_height * self.shift

            # алгоритм выбора правильного спрайта в зависимости от угла
            if self.viewing_angles:
                if theta < 0:
                    theta += math.pi * 2
                theta = 360 - int(math.degrees(theta))

                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            sprite_object = self.object
            if self.animation and dist_to_sprt < self.animation_dist:
                sprite_object = self.animation[0]
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1
                else:
                    self.animation.rotate()
                    self.animation_count = 0

            # рассчёт дислокации спрайта на экране
            sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            # перерассчёт размеров спрайта
            sprite = pygame.transform.scale(sprite_object, (proj_height, proj_height))
            # сие идёт в рейкаст функцию  (сначала в world в двоувинге)
            return (dist_to_sprt, sprite, sprite_pos)

        return [0]
