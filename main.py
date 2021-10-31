import pygame
import random

pygame.init()

display_width = 800
display_height = 600

yellow_color = (255, 253, 208)
black_color_1 = (100, 100, 100)
black_color_2 = (0, 0, 0)
red_color = (255, 0, 0)
green_color = (0, 255, 0)

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()

block_size = 20


font = pygame.font.SysFont("monaco", 40)


def game():
    game_over = False
    game_close = False
    game_begin = False

    x = display_width / 2
    y = display_height / 2

    delta_x = 0
    delta_y = 0

    last_key = ''
    fps = 10

    snake_list = []
    snake_length = 1

    x_food = round(random.randrange(0, display_width - block_size) / float(block_size)) * float(block_size)
    y_food = round(random.randrange(0, display_height - block_size) / float(block_size)) * float(block_size)

    while not game_over:

        while not game_begin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_begin = True
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        fps = 10
                        game_begin = True
                    if event.key == pygame.K_2:
                        fps = 20
                        game_begin = True
                    if event.key == pygame.K_3:
                        fps = 30
                        game_begin = True
                display.fill(yellow_color)
                display.blit(font.render("Выберите уровень сложности:",
                                         True, red_color), [display_width / 3.5, display_height / 2.7])
                display.blit(font.render("1 - легкий",
                                         True, red_color), [display_width / 2.5, display_height / 2.3])
                display.blit(font.render("2 - средний",
                                         True, red_color), [display_width / 2.5, display_height / 2.05])
                display.blit(font.render("3 - сложный",
                                         True, red_color), [display_width / 2.5, display_height / 1.82])
                pygame.display.update()

        while game_close == True:
            display.fill(yellow_color)
            display.blit(font.render("Вы проиграли!",
                                     True, red_color), [display_width / 2.5, display_height / 2.3])
            display.blit(font.render("(нажмите R для рестарта, esc - для выхода)",
                                     True, red_color), [display_width / 6, display_height / 2.05])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and last_key != pygame.K_RIGHT and last_key != pygame.K_LEFT:
                    delta_x = -block_size
                    delta_y = 0
                elif event.key == pygame.K_RIGHT and last_key != pygame.K_LEFT and last_key != pygame.K_RIGHT:
                    delta_x = block_size
                    delta_y = 0
                elif event.key == pygame.K_UP and last_key != pygame.K_DOWN and last_key != pygame.K_UP:
                    delta_y = -block_size
                    delta_x = 0
                elif event.key == pygame.K_DOWN and last_key != pygame.K_UP and last_key != pygame.K_DOWN:
                    delta_y = block_size
                    delta_x = 0
                last_key = event.key
        if x >= display_width or x < 0 or y >= display_height or y < 0:
            game_close = True
        x += delta_x
        y += delta_y
        display.fill(yellow_color)
        pygame.draw.rect(display, green_color, [x_food, y_food, block_size, block_size])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for el in snake_list[:-1]:
            if el == snake_Head:
                game_close = True

        for el in snake_list[0:len(snake_list)]:
            pygame.draw.rect(display, black_color_1, [el[0], el[1], block_size, block_size])
        display.blit(font.render("Счет: " + str(snake_length - 1), True, red_color), [display_width - 150, 20])
        pygame.draw.rect(display, black_color_2, [snake_list[-1][0], snake_list[-1][1], block_size, block_size])

        pygame.display.update()

        if x == x_food and y == y_food:
            x_food = round(random.randrange(0, display_width - block_size) / float(block_size)) * float(block_size)
            y_food = round(random.randrange(0, display_height - block_size) / float(block_size)) * float(block_size)
            snake_length += 1

        clock.tick(fps)

    pygame.quit()
    quit()


game()