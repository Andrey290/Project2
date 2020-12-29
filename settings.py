import math

# основные настройки
WIDTH = 1200  # ширина окна
HEIGHT = 800  # вышина окна
HALF_WIDTH = WIDTH // 2  # половина ширины
HALF_HEIGHT = HEIGHT // 2  # половина высоты
FPS = 120  # фпс
TILE = 100  # размер квадрата карты(толщена стенов)

# расположение доп информаци на экране
FPS_POS = (WIDTH - 65, 5)
X_POS = (WIDTH - 65, 65)

TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE

# настройки рейкастинга
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 3600
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))  # расстояние от игрока до экрана
PROJ_COEFF = 3 * DIST * TILE  # проекционный коеффициент (не меняй, я специально хороший подобрал)
SCALE = WIDTH // NUM_RAYS  # коеффиециент количестваува лучей в ширине экрана

# настройки игрока
player_position = (HALF_WIDTH // 2, 3 * HALF_HEIGHT // 2)  # стартовая позиция
player_angle = 0  # стартовый угол (в джоулях на парсек)
player_speed = 2  # скорасть
angle_speed = 0.02  # скорасть паварота

# разные цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# настройки спрайтов
CENTER_RAY = NUM_RAYS // 2 - 1
