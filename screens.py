import pygame 
import keyboard
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(size=(900,450))
congrats = pygame.image.load('Congratulations!.png')
print_lesson = pygame.image.load('printlesson.png')
printpract = pygame.image.load('printpract.png')

width, height = 900, 450

show = pygame.display.set_mode((width, height))
x = 0
y = 0
show_screen = 0
running = True
while running:
    while show_screen == 0:
                show.blit(congrats, (0, 0))
                pygame.display.update()
                clock.tick(10)    
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():  
        if event.type == pygame.KEYUP:
             
            if event.key == pygame.K_RETURN:
                show_screen = 1

                while show_screen == 1:                
                    show.blit(print_lesson, (0, 0))
                    pygame.display.update()
                    clock.tick(10)
                    if event.key == pygame.K_RETURN:
                        break
                    
            show_screen = 2
            while show_screen == 2:                
                show.blit(printpract, (0, 0))
                pygame.display.update()
                clock.tick(10)
            

