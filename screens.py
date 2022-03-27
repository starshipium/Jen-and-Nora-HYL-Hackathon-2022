from tracemalloc import stop
from turtle import end_fill
import pygame 
import sys
import keyboard
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(size=(900,450))
congrats = pygame.image.load('snakelesson1.png')
print_lesson = pygame.image.load('snakelesson2.png')
printpract = pygame.image.load('snakelesson3.png')
tryagain= pygame.image.load('tryagain.png')
try_again= pygame.transform.scale(tryagain, (200,100))
correct = pygame.image.load('check.png')
lesson2_1 = pygame.image.load('snakelesson4.png')
lesson2_2 = pygame.image.load('snakelesson5.png')
lesson2_3 = pygame.image.load('snakelesson6.png')
width, height = 900, 450

def test():
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(350, 300, 140, 32)
    # color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('black')
    color = color_passive

    active = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:

                    user_text = user_text[:-1]
    
                else:
                    user_text += event.unicode
        if active:
            color = color_passive

        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()
        clock.tick(60)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if user_text == "print(\"Python is a snake!\")":
                    show.blit(correct, (0, 0))
                    pygame.display.update()
                    clock.tick(10)
                    input_rect = pygame.Rect(0, 0, 0, 0)
                    text_surface = base_font.render(user_text, True, (100,100,100))
                    pygame.display.flip()
            else:
                show.blit(try_again, (-10, 0))
                pygame.display.flip()
                clock.tick(10)


def lesson1(congrats, print_lesson, printpract):
    if show_screen == 0:
        show.blit(congrats, (0, 0))
        pygame.display.update()
        clock.tick(10) 
    if show_screen == 1:                
        show.blit(print_lesson, (0, 0))
        pygame.display.update()
        clock.tick(10)
    if show_screen == 2:                
        show.blit(printpract, (0, 0))
        pygame.display.update()
        clock.tick(10)
        test()
        
def lesson2(lesson2_1, lesson2_2, lesson2_3):
    if show_screen == 3:
        show.blit(lesson2_1, (0, 0))
        pygame.display.update()
        clock.tick(10) 
    if show_screen == 4:                
        show.blit(lesson2_2, (0, 0))
        pygame.display.update()
        clock.tick(10)
    if show_screen == 5:                
        show.blit(lesson2_3, (0, 0))
        pygame.display.update()
        clock.tick(10)


    
show_screen = 0
show = pygame.display.set_mode((width, height))


running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                show_screen += 1
            if event.key == pygame.K_LEFT:
                show_screen -= 1
    lesson1(congrats, print_lesson, printpract)
    lesson2(lesson2_1, lesson2_2, lesson2_3)
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                show_screen += 1
            if event.key == pygame.K_LEFT:
                show_screen -= 1
    

pygame.quit()




