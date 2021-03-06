from settings import *
import pygame
import math
from map import collision_walls


class Player:
    def __init__(self, sprites):
        self.x, self.y = player_position
        self.sprites = sprites
        self.angle = player_angle
        self.sensivity = sensivity
        self.side = 50
        self.rect = pygame.Rect(*player_position, self.side, self.side)
        self.collision_sprites = [pygame.Rect(*obj.pos, obj.side, obj.side) for obj in self.sprites.sprite_objects if obj.blocked]
        self.collision_list = collision_walls + self.collision_sprites
    # свойство, которое возвращает позицию по x и y
    @property
    def pos(self):
        return (self.x, self.y)

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.collision_list)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.collision_list[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy



    def movement(self):
        self.key_move()
        self.rect.center = self.x, self.y
        # лично я больше люблю клавиши
        self.mouse_move()
        self.angle %= math.pi * 2

    def key_move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            dx = player_speed * cos_a
            dy = player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a
            dy = -player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = player_speed * sin_a
            dy = -player_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a
            dy = player_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_q]:
            self.angle -= angle_speed
        if keys[pygame.K_e]:
            self.angle += angle_speed

    def mouse_move(self):
        if pygame.mouse.get_focused():
            diff = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += diff * self.sensivity
