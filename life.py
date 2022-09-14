import pygame
import random
import time
import sys

RECT_X = random.randrange(800)
RECT_Y = random.randrange(500)
RECT_W = 300
RECT_H = 300

# PyGame Screen
pygame.init()
screen = pygame.display.set_mode([800, 500])

# Render cells to screen
def render():
    screen.fill((0,0,0))      
    
    pygame.draw.rect(screen, (255,0,0), (RECT_X, RECT_Y, RECT_W, RECT_H))

    pygame.display.flip()
    # time.sleep(1)
   
def onclick(pos):
    global RECT_X
    global RECT_Y
    global RECT_W
    global RECT_H

    valorX = pos[0] 
    valorY = pos[1]
    
    print(pos)
    print('X:',valorX, 'Y:', valorY)
    print ('Tamanho',RECT_W, RECT_H)

    if (valorX > RECT_X and valorX < RECT_X + RECT_W and valorY > RECT_Y and valorY < RECT_Y + RECT_W): #400 representa ValorX + Rect_W
        mensagem()
        RECT_X = random.randrange(750)
        RECT_Y = random.randrange(450)
        RECT_W -= 15
        RECT_H -= 15
    else:
        print('pretin')
        print('-------')    

    # print('sec: ')
    # timerzin()
        

# def timer():
#     global tempo
#     tempo += 1
#     print(tempo)

# def timerzin():

#     for i in range(0, 30):
#         sys.stdout.write("\r{}".format(i))
#         sys.stdout.flush()
#         time.sleep(1)
#     print ("\nFim")

def mensagem():
    print('vermelin')
    print('--------')


def draw_rect(x, y):
    # Draw stuff here                      x/y/w/h
    pygame.draw.rect(screen, (255,0,0), (x,y,55,55))

# Main program
def main():
    running = True
    while running:
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                onclick(pos)
            if event.type == pygame.QUIT:
                running = False
        render()
    pygame.quit()
main()