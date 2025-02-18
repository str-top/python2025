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
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

# Часы для управления скоростью игры
clock = pygame.time.Clock()

# Размер блока змейки и скорость змейки
block_size = 10
snake_speed = 15

# Шрифт для отображения счета
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция для отображения счета
def display_score(score):
    value = score_font.render(f"Счет: {score}", True, yellow)
    window.blit(value, [0, 0])

# Функция для отрисовки змейки
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(window, green, [block[0], block[1], block_size, block_size])

# Функция для отображения сообщения на экране
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

# Основная функция игры
def game_loop():
    game_over = False
    game_close = False

    # Начальная позиция змейки
    x = width / 2
    y = height / 2

    # Изменение позиции змейки
    x_change = 0
    y_change = 0

    # Змейка (список блоков)
    snake_list = []
    length_of_snake = 1

    # Позиция еды
    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(blue)
            display_message("Вы проиграли! Нажмите Q-Выход или C-Играть снова", red)
            display_score(length_of_snake - 1)
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
        window.fill(black)

        # Отрисовка еды
        pygame.draw.rect(window, red, [food_x, food_y, block_size, block_size])

        # Добавление новой головы змейки
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Проверка на столкновение с собой
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Проверка на съедание еды
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Запуск игры
game_loop()
