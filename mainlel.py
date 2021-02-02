from igrok import *
from pygame import *

WIN_WIDTH = 760
WIN_HEIGHT = 520
hero = Player(0, 230)
BACKGROUND_COLOR = "#DAA520"
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
block = pygame.image.load("block.jpg")
PLATFORM_WIDTH = 20
PLATFORM_HEIGHT = 20
timer = pygame.time.Clock()



def main():
    level = [
        " " * 2 + "-" + 32 * "-" + "-" + " " * 2,
        " " * 2 + "-" + " " * 17 + "-" * 5 + " " * 10 + "-" + " " * 2,
        " " * 2 + "-" + " " * 17 + "-" * 5 + " " * 10 + "-" + " " * 2,
        " " * 2 + "-" + " " * 17 + "-" * 5 + " " * 10 + "-" + " " * 2,
        " " * 2 + "-------    ----   -----   ----   " + "-" + " " * 2,
        " " * 2 + "-------    ----   -----   ----   " + "-" + " " * 2,
        " " * 2 + "-------    ----   -----   ----   " + "-" + " " * 2,
        " " * 2 + "-------    ----   -----   ----   " + "-" + " " * 2,
        " " * 2 + "-          ----   -----   ----   " + "-" + " " * 2,
        " " * 2 + "-          ----   -----          " + "-" + " " * 2,
        " " * 2 + "           ----   -----           " + " " * 2,
        " " * 2 + "                  -----           " + " " * 2,
        " " * 2 + "                                  " + " " * 2,
        " " * 2 + "                          ----    " + " " * 2,
        " " * 2 + "                          ----    " + " " * 2,
        " " * 2 + "----     -----    -----          " + "-" + " " * 2,
        " " * 2 + "----     -----    -----          " + "-" + " " * 2,
        " " * 2 + "----     -----    -----          " + "-" + " " * 2,
        " " * 2 + "----     -----    -----          " + "-" + " " * 2,
        " " * 2 + "----     -----    -----          " + "-" + " " * 2,
        " " * 2 + "----     -----    -----          " + "-" + " " * 2,
        " " * 2 + "----     -----    -----          " + "-" + " " * 2,
        " " * 2 + "----              -----          " + "-" + " " * 2,
        " " * 2 + "----" + " " * 14 + "-" * 5 + " " * 10 + "-" + " " * 2,
        " " * 2 + "----" + " " * 14 + "-" * 5 + " " * 10 + "-" + " " * 2,
        " " * 2 + "-" + 32 * "-" + "-" + " " * 2,
    ]
    left = right = up = down = False
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("igor")  # Пишем в шапку
    run = True

    while run:  # Основной цикл программы
        if hero.rect.x >= 700:
            level.reverse()
            hero.rect.x = 0
            hero.rect.y = 230
        timer.tick(100)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_q:
                run = False
        # коллизия
        if hero.rect.y % 20 == 0:
            if up:

                if level[(hero.rect.y - 20) // 20][hero.rect.x // 20] == '-' or level[(hero.rect.y - 20) // 20][
                    (hero.rect.x + 20) // 20] == '-' or level[(hero.rect.y - 20) // 20][
                    (hero.rect.x + 40) // 20] == '-':
                    up = False
            if down:
                if level[(hero.rect.y + 40) // 20][hero.rect.x // 20] == '-' or level[(hero.rect.y + 40) // 20][
                    (hero.rect.x + 20) // 20] == '-' or level[(hero.rect.y + 40) // 20][
                    (hero.rect.x + 40) // 20] == '-':
                    down = False
        if hero.rect.x % 20 == 0:
            if level[hero.rect.y // 20][(hero.rect.x - 20) // 20] == '-' or level[(hero.rect.y + 20) // 20][
                (hero.rect.x - 20) // 20] == '-' or level[(hero.rect.y + 40) // 20][
                (hero.rect.x - 20) // 20] == '-':
                left = False
            elif level[hero.rect.y // 20][(hero.rect.x + 40) // 20] == '-' or level[(hero.rect.y + 20) // 20][
                (hero.rect.x + 40) // 20] == '-' or level[(hero.rect.y + 40) // 20][
                (hero.rect.x + 40) // 20] == '-':
                right = False
        screen.fill(BACKGROUND_COLOR)
        x = y = 0
        # вывод уровня на экран
        for row in level:
            for col in row:
                if col == "-":
                    screen.blit(block, (x, y))
                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0
        hero.update(left, right, up, down)
        hero.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
