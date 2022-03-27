from textwrap import fill
import keyboard
import pygame
import sys
from pygame.event import event_name
clock = pygame.time.Clock()
pygame.init()

#def functions and variables for moving snake
def moving_snake(x,y):
    movement = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            movement += 1 

screen = pygame.display.set_mode(size=(900,450))
pygame.display.set_caption('Snake: Learning Python for Kids')
snake_start = pygame.image.load('startscreen.png')
apple = pygame.image.load('apple.png')
apple = pygame.transform.scale(apple, (100,100))
first_snake = pygame.transform.scale(snake_start, (900,450))
background = pygame.image.load('background.png')
background2 = pygame.image.load('background2.png')
background3 = pygame.image.load('background3.png')
plants = pygame.transform.scale(background, (900,450))
snake1 = pygame.image.load('snake1.png')
plants2 = pygame.transform.scale(background2, (900,450))
plants3 = pygame.transform.scale(background3, (900,450))
#snake2 = pygame.image.load('snake2.png')
snake_1 = pygame.transform.scale(snake1, (200,50))
snake_rect = snake_1.get_rect()
#snake_2 = pygame.transform.scale(snake2, (200,50))
width,height = 900,450
show = pygame.display.set_mode((width,height))
show.fill((255,255,255))
pygame.display.flip()

def controls_2(x,y):
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(10, 10, 140, 32)
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
        if user_text == "print(\'up\')" or user_text == "print(\'down\')" or user_text == "print(\'left\')" or user_text == "print(\'right\')" or user_text == "print(\"up\")" or user_text == "print(\"down\")" or user_text == "print(\"left\")" or user_text == "print(\"right\")":
            return user_text
  
def snake_update(first_snake, plant, snake_1,hori_p, verti_p, apple, pos_x, pos_y):
    if show_number == 0:
        show.blit(first_snake, (1,1))
        pygame.display.update()
    if show_number == 1:
        show.blit(plant, (1,1))
        show.blit(apple, (pos_x, pos_y))
        show.blit(snake_1, (hori_p,verti_p))
        pygame.display.update()
        clock.tick(10)

def eat(pos_y, pos_x, x, y):
    if x <= (pos_x-100) and x >= (pos_x-200):
        if y == pos_y:
                return True 
def controls_3(x,y):
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(10, 10, 140, 32)
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
        front_string = user_text[:7]
        back_string = user_text[-2:]
        front_int = user_text[:6]
        back_int = user_text[-1:]
        mid_int = user_text[6:-1]
        if back_string == "\')" or back_string == "\")":
            if front_string == "print(\'":
                return "string"
        elif back_int == ")" and front_int == "print(":
            try: 
                int(mid_int)
                return "int"
            except:
                c=0

def lesson3(lesson3_1, lesson3_2, lesson3_3,lesson3_4,lesson3_5):
        if show_screen == 7:
            show.blit(lesson3_1, (0, 0))
            pygame.display.update()
            clock.tick(10) 
        if show_screen == 8:                
            show.blit(lesson3_2, (0, 0))
            pygame.display.update()
            clock.tick(10)
        if show_screen == 9:                
            show.blit(lesson3_3, (0, 0))
            pygame.display.update()
            clock.tick(10)
        if show_screen == 10:
            show.blit(lesson3_4, (0, 0))
            pygame.display.update()
            clock.tick(10)
        if show_screen == 11:
            show.blit(lesson3_5, (0, 0))
            pygame.display.update()
            clock.tick(10)
        if show_screen == 12:
            show.blit(lesson3_6, (0, 0))
            pygame.display.update()
            clock.tick(10)


def test3():
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(350, 400, 140, 32)
    color_passive = pygame.Color('black')
    color = color_passive

    active = False

    for event in pygame.event.get():
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
                    if user_text == "20":
                        # show.blit(correct, (0, 0))
                        pygame.display.update()
                        clock.tick(10)
                        input_rect = pygame.Rect(-500, 0, 0, 0)
                        text_surface = base_font.render(user_text, True, (100,100,100))
                        pygame.display.flip()
                        show.blit(certificate, (0, 0))
                        pygame.display.update()
                    else:
                        show.blit(try_again, (-10, 0))
                        pygame.display.flip()
                        clock.tick(10)
                while event.key == pygame.K_ESCAPE:
                            pygame.quit(); sys.exit()


def str_int_game(x,y,snake_1): 
  
    running_2 = True
    pos_x, pos_y = 525, 130
    snake_1 = pygame.transform.flip(snake_1, True, False)
    while running_2 == True:   
        snake_update(first_snake, plants3, snake_1,x,y,apple,pos_x, pos_y) 
        move1 = controls_3(x,y)
        if move1 == "string":
            y=150
            snake_update(first_snake, plants3, snake_1,x,y,apple,pos_x, pos_y)
        if move1 == "int":
            x_change = 200 
            x = 350
            snake_update(first_snake, plants3, snake_1,x,y,apple,pos_x, pos_y)
            next = False
        if x <= (pos_x-100) and x >= (pos_x-200):
            if y <= (pos_y+50) and y <= (pos_y+50):
                show.blit(lesson3_1, (0, 0))
                pygame.display.update()
                clock.tick(10) 
                show_screen = 7
                running = True
                while running:
                    for event in pygame.event.get(): 
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                show_screen += 1
                            if event.key == pygame.K_LEFT:
                                show_screen -= 1
                    if show_screen == 7:
                        show.blit(lesson3_1, (0, 0))
                        pygame.display.update()
                        clock.tick(10) 
                    if show_screen == 8:                
                        show.blit(lesson3_2, (0, 0))
                        pygame.display.update()
                        clock.tick(10)
                    if show_screen == 9:                
                        show.blit(lesson3_3, (0, 0))
                        pygame.display.update()
                        clock.tick(10)
                    if show_screen == 10:
                        show.blit(lesson3_4, (0, 0))
                        pygame.display.update()
                        clock.tick(10)
                    if show_screen == 11:
                        show.blit(lesson3_5, (0, 0))
                        pygame.display.update()
                        clock.tick(10)
                    if show_screen == 12:
                        show.blit(lesson3_6, (0, 0))
                        pygame.display.update()
                        clock.tick(10)
                        test3()

    
#moving snake w/ print functions
#MAIN 
def print_game(snake_1,x,y,pos_x, pos_y,lesson2_1, lesson2_2, lesson2_3):
    
    
            
    def test2():
        running=True
        # show=0
        while running == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        show.blit(lesson2_6, (0,0))
                        pygame.display.update()
                        clock.tick(10)
                    if event.key == pygame.K_2:
                        show.blit(lesson2_5, (0,0))
                        pygame.display.update()
                        clock.tick(10)
                    if event.key == pygame.K_RIGHT:
                        str_int_game(x,y,snake_1)
                        running = False
                        break

        
    def lesson2(lesson2_1, lesson2_2, lesson2_3,lesson2_5,lesson2_6):
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
        if show_screen == 6:
            show.blit(lesson2_4, (0, 0))
            pygame.display.update()
            clock.tick(10)
            test2()

    running_2 = True
    pos_x, pos_y = 150, 350
    snake_1 = pygame.transform.flip(snake_1, True, False)
    while running_2 == True:   
        snake_update(first_snake, plants2, snake_1,x,y,apple,pos_x, pos_y) 
        move = controls_2(x,y)

        if move == "print(\'up\')" or move == "print(\"up\")":
            y_change = -50 
            y += y_change 
            snake_update(first_snake, plants2, snake_1,x,y,apple,pos_x, pos_y)

        if move == "print(\'down\')" or move == "print(\"down\")":
            y_change = +50  
            y += y_change 
            snake_update(first_snake, plants2, snake_1,x,y,apple,pos_x, pos_y) 

        if move == "print(\'left\')" or move == "print(\"left\")"  :
            x_change = -200   
            x += x_change           
            snake_update(first_snake, plants2, snake_1,x,y,apple,pos_x, pos_y)
        
        if move == "print(\'right\')" or move == "print(\"right\")":
            x_change = +100    
            x += x_change           
            snake_update(first_snake, plants2, snake_1,x,y,apple,pos_x, pos_y)
        if x <= (pos_x) and x >= (pos_x-200):
            if y == pos_y:
                show_screen = 3
                running = True
                while running:
                    for event in pygame.event.get(): 
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                show_screen += 1
                            if event.key == pygame.K_LEFT:
                                show_screen -= 1
                    lesson2(lesson2_1, lesson2_2, lesson2_3,lesson2_5,lesson2_6)
    
        
            
        

# def func and variables for lessons
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
lesson2_4 = pygame.image.load('snakelesson7.png')
lesson2_5 = pygame.image.load('snakelesson8.png')
lesson2_6 = pygame.image.load('snakelesson9.png')
lesson3_1 = pygame.image.load('snakelesson10.png')
lesson3_2 = pygame.image.load('snakelesson11.png')
lesson3_3 = pygame.image.load('snakelesson12.png')
lesson3_4 = pygame.image.load('snakelesson13.png')
lesson3_5 = pygame.image.load('snakelesson14.png')
lesson3_6 = pygame.image.load('snakelesson15.png')
certificate = pygame.image.load('certificate.png')
width, height = 900, 450

def test():
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    input_rect = pygame.Rect(350, 300, 140, 32)
    color_passive = pygame.Color('black')
    color = color_passive

    active = False

    for event in pygame.event.get():
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
                    if user_text == "print(\'Python is a snake!\')" or user_text == 'print(\"Python is a snake!\")':
                        # show.blit(correct, (0, 0))
                        pygame.display.update()
                        clock.tick(10)
                        input_rect = pygame.Rect(-500, 0, 0, 0)
                        text_surface = base_font.render(user_text, True, (100,100,100))
                        pygame.display.flip()
                        print_game(snake_1,x,y,pos_x, pos_y,lesson2_1, lesson2_2, lesson2_3)
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


        


#moving snake w/ arrow keys

pos_x, pos_y = 750, 350
x=0
y=200
x_change = 0
y_change =0
running = True
show_number = 0
while running == True:    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_number = 1
            if event.key == pygame.K_RIGHT:
                x_change = 50
            if event.key == pygame.K_LEFT:
                x_change = -50    
            if event.key == pygame.K_UP:
                y_change = -50
            if event.key == pygame.K_DOWN:
                y_change = +50
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x += x_change 
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y += y_change   
    snake_update(first_snake, plants, snake_1,x,y,apple,pos_x, pos_y)
    if eat(pos_y, pos_x, x, y):
        running = False
        break
 
 #first lesson
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
    