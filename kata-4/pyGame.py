import pygame, random

# Variables
screen_width = 1280
screen_height = 960

# Colors
white_color = (200, 200, 200)
light_gray = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

rectangle = pygame.Rect(10, 10, 10, 140)
ball = pygame.Rect(10, 10, 50, 50)

def move_rectangle():
    # Coge el scope de variable que estan fuera de la función
    global speed
    if rectangle.top + 50 < screen_height:
        # velocidad
        rectangle.top += 1

# Bola restart
def start_ball():
    global speed_bola_x, speed_bola_y


    if ball.left + 50 > screen_width or ball.left < 0:
        ball.top = screen_height // 2
        ball.left = screen_width // 2
    
    speed_bola_x = 3 * random.choice((1, -1))
    speed_bola_y = 3 * random.choice((1, -1))

def move_ball():
    global speed_bola_x, speed_bola_y

    if ball.top + 50 > screen_height or ball.top < 0:
        speed_bola_x = -speed_bola_x

    if ball.left < 10 and rectangle.top < ball.top < rectangle.top + 140:
        speed_bola_y = -speed_bola_y

    start_ball()

    ball.top += speed_bola_x
    ball.left += speed_bola_y

speed = 0
speed_bola_x = 3
speed_bola_y = 3
while True:
    screen.fill(white_color)

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.KEYDOWN:
            # Mirar que tecla se ha teclado
            if event.key == pygame.K_UP:
                speed = -3
            elif event.key == pygame.K_UP:
                speed = 3
        elif event.type == pygame.KEYUP:
            speed = 0

    move_rectangle()
    move_ball()

    # rectangulo por encima de la pantalla
    pygame.draw.rect(screen, white_color, rectangle)

    pygame.draw.ellipse(screen, white_color, ball)

    pygame.display.flip()
    clock.tick(60)