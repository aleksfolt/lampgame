import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
window_width = 800
window_height = 600

# Создание окна
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Игра с лампочкой")

# Загрузка изображения лампочки и изменение размера
lamp_image = pygame.image.load("lamp.png")
lamp_image = pygame.transform.scale(lamp_image, (lamp_image.get_width() // 5, lamp_image.get_height() // 5))

# Позиция и скорость лампочки
lamp_x = window_width // 2 - lamp_image.get_width() // 2
lamp_y = window_height - lamp_image.get_height() - 50  # Отступ под лампочкой
lamp_speed = 4
jump_speed = 6

# Флаги для направления движения
move_left = False
move_right = False
jumping = False

# Создание горизонта
horizon_height = window_height - 100

# Загрузка фона изображения
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (window_width, window_height))

clock = pygame.time.Clock()

# Главный цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            elif event.key == pygame.K_d:
                move_right = True
            elif event.key == pygame.K_w and not jumping and lamp_y == window_height - lamp_image.get_height() - 50:
                jumping = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_d:
                move_right = False

    # Движение лампочки
    if move_left and lamp_x > 0:
        lamp_x -= lamp_speed
    elif move_right and lamp_x < window_width - lamp_image.get_width():
        lamp_x += lamp_speed

    if jumping:
        if jump_speed >= -10:
            lamp_y -= (jump_speed * abs(jump_speed)) * 0.5
            jump_speed -= 1
        else:
            jumping = False
            jump_speed = 6
    else:
        if lamp_y < window_height - lamp_image.get_height() - 50:  # Учитываем высоту лампочки
            lamp_y += lamp_speed
        else:
            lamp_y = window_height - lamp_image.get_height() - 50  # Остановка на горизонте

    # Отрисовка фона
    window.blit(background_image, (0, 0))

    # Отрисовка горизонта
    pygame.draw.rect(window, (0, 0, 0), pygame.Rect(0, horizon_height, window_width, window_height - horizon_height))

    # Отрисовка лампочки
    window.blit(lamp_image, (lamp_x, lamp_y))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты обновления
    clock.tick(60)

# Завершение игры
pygame.quit()
