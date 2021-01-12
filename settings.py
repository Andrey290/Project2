import math
import sqlite3

con = sqlite3.connect("3d_game_settings")
cur = con.cursor()

# основные настройки
WIDTH = (cur.execute("""SELECT WIDTH FROM settings_for_3d_game""").fetchall())[0][0]  # ширина окна
HEIGHT = (cur.execute("""SELECT HEIGHT FROM settings_for_3d_game""").fetchall())[0][0]  # вышина окна
HALF_WIDTH = WIDTH // 2  # половина ширины
HALF_HEIGHT = HEIGHT // 2  # половина высоты
HEIGHT_COMP_5 = 5 * HEIGHT
HEIGHT_COMP_2 = 2 * HEIGHT
FPS = (cur.execute("""SELECT FPS FROM settings_for_3d_game""").fetchall())[0][0]  # фпс
TILE = (cur.execute("""SELECT TILE FROM settings_for_3d_game""").fetchall())[0][0]  # размер квадрата карты(толщена стенов)

# расположение доп информаци на экране
FPS_POS = (WIDTH - 65, 5)
X_POS = (WIDTH - 65, 65)

TEXTURE_WIDTH = (cur.execute("""SELECT TEXTURE_WIDTH FROM settings_for_3d_game""").fetchall())[0][0]
TEXTURE_HEIGHT = (cur.execute("""SELECT TEXTURE_HEIGHT FROM settings_for_3d_game""").fetchall())[0][0]
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

MINIMAP_SCALE = (cur.execute("""SELECT MINIMAP_SCALE FROM settings_for_3d_game""").fetchall())[0][0]
MINIMAP_RES = (WIDTH // MINIMAP_SCALE, HEIGHT // MINIMAP_SCALE)
MAP_SCALE = 3 * MINIMAP_SCALE
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MINIMAP_SCALE)

# настройки рейкастинга
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = (cur.execute("""SELECT NUM_RAYS FROM settings_for_3d_game""").fetchall())[0][0]
FAKE_RAYS = (cur.execute("""SELECT FAKE_RAYS FROM settings_for_3d_game""").fetchall())[0][0]
MAX_DEPTH = (cur.execute("""SELECT MAX_DEPTH FROM settings_for_3d_game""").fetchall())[0][0]
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))  # расстояние от игрока до экрана
PROJ_COEFF = 3 * DIST * TILE  # проекционный коеффициент (не меняй, я специально хороший подобрал)
SCALE = WIDTH // NUM_RAYS  # коеффиециент количестваува лучей в ширине экрана

# настройки игрока
player_position = (HALF_WIDTH // 2, 3 * HALF_HEIGHT // 2)  # стартовая позиция
player_angle = (cur.execute("""SELECT player_angle FROM settings_for_3d_game""").fetchall())[0][0]  # стартовый угол (в джоулях на парсек)
player_speed = (cur.execute("""SELECT player_speed FROM settings_for_3d_game""").fetchall())[0][0]  # скорасть
angle_speed = (cur.execute("""SELECT angle_speed FROM settings_for_3d_game""").fetchall())[0][0]  # скорасть паварота
sensivity = (cur.execute("""SELECT sensivity FROM settings_for_3d_game""").fetchall())[0][0]

# разные цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (200, 200, 200)
VIRIDIAN = (100, 255, 100)
# (текст, рамка, верхняя координата по y)
intro_text = [["ИГРАТЬ", None, 200],
              ["МЕНЮ НАСТРОЕК", None, 260],
              ["ВЫХОД", None, 320]]
# настройки спрайтов
CENTER_RAY = NUM_RAYS // 2 - 1



print(FPS)