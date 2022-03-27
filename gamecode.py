from textwrap import fill
import pygame
from pygame.event import event_name
clock = pygame.time.Clock()
pygame.init()
def moving_snake(x,y):
    movement = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            movement += 1 

screen = pygame.display.set_mode(size=(900,450))
pygame.display.set_caption('Snake: Learning Python for Kids')
snake_start = pygame.image.load('startscreen.png')
first_snake = pygame.transform.scale(snake_start, (900,450))
background = pygame.image.load('background.png')
plants = pygame.transform.scale(background, (900,450))
snake1 = pygame.image.load('snake1.png')
#snake2 = pygame.image.load('snake2.png')
snake_1 = pygame.transform.scale(snake1, (200,50))
snake_rect = snake_1.get_rect()
#snake_2 = pygame.transform.scale(snake2, (200,50))
width,height = 900,450
show = pygame.display.set_mode((width,height))
show.fill((255,255,255))
pygame.display.flip()

running = True
while running == True:
    show_number = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        show.blit(first_snake, (1,1))
        pygame.display.update()
        clock.tick(10)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_number += 1
                while show_number == 1:
                    show.blit(plants, (1,1))
                    show.blit(snake_1, (1,200))
                    pygame.display.update()
                    clock.tick(10)
            if event.key == pygame.K_LEFT:
                
