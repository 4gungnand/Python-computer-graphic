import pygame
import random

pygame.init()

screen_width = 535
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animasi Anak Panah")

background = pygame.image.load("background.png")
background_rect = background.get_rect()
#
background_x = random.randint(0, screen_width - background_rect.width)
background_y = random.randint(0, screen_height - background_rect.height)

arrow_x = 0
arrow_y = 250

arrow_speed = 1

arrow_img = pygame.image.load("arrow.png")


def draw_arrow(x, y):
    screen.blit(arrow_img, (x, y))


running = True
while running:
    screen.fill("white")
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    arrow_x += arrow_speed

    if background_x + background_rect.width < 0:
        background_x = screen_width

    if arrow_x > screen_width:
        arrow_x = 0

    draw_arrow(arrow_x, arrow_y)
    pygame.time.delay(10)
    pygame.display.update()

pygame.quit()