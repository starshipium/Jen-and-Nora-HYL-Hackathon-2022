import pygame 
import sys
import keyboard
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(size=(900,450))
congrats = pygame.image.load('Congratulations!.png')
print_lesson = pygame.image.load('printlesson.png')
printpract = pygame.image.load('printpract.png')

width, height = 900, 450

def test():
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(450, 200, 140, 32)
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

def comic(congrats, print_lesson, printpract):
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


    

show = pygame.display.set_mode((width, height))

show_screen = 0
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if event.type == pygame.K_RETURN:
            show_screen += 1
    comic(congrats, print_lesson, printpract)

pygame.quit()




    # while show_screen == 0:
    #             show.blit(congrats, (0, 0))
    #             pygame.display.update()
    #             clock.tick(10)    
    # keys = pygame.key.get_pressed()
     
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_RETURN:
    #             show_screen = 1

    #         if show_screen == 1:                
    #             show.blit(print_lesson, (0, 0))
    #             pygame.display.update()
    #             clock.tick(10)
    #             if event.key == pygame.K_RETURN:
    #                 break
                    
    #         show_screen = 2
    #         while show_screen == 2:                
    #             show.blit(printpract, (0, 0))
    #             pygame.display.update()
    #             clock.tick(10)
            

