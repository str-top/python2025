import pygame
import time
import random

# Инициализация pygame
pygame.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры окна
width = 600
height = 400

# Создание окна
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

# Часы для управления скоростью игры
clock = pygame.time.Clock()

# Размер блока змейки и скорость
block_size = 10
snake_speed = 15

# Шрифт для отображения счета
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция для отображения счета
def display_score(score):
    value = score_font.render("Счет: " + str(score), True, yellow)
    game_window.blit(value, [0, 0])

# Функция для отрисовки змейки
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, green, [block[0], block[1], block_size, block_size])

# Функция для отображения сообщения на экране
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [width / 6, height / 3])

# Основной игровой цикл
def game_loop():
    game_over = False
    game_close = False

    # Начальная позиция змейки
    x = width / 2
    y = height / 2

    # Изменение позиции
    x_change = 0
    y_change = 0

    # Змейка и ее длина
    snake_list = []
    snake_length = 1

    # Позиция еды
    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_window.fill(blue)
            display_message("Ты проиграл! Нажми Q-Выйти или C-Играть снова", red)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        # Проверка на выход за границы экрана
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        game_window.fill(black)

        # Отрисовка еды
        pygame.draw.rect(game_window, red, [food_x, food_y, block_size, block_size])

        # Голова змейки
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Проверка на столкновение с собой
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Если змейка съела еду
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Запуск игры
game_loop()

