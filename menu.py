import pygame, sys, os
import random   #to select cards
from pygame.locals import *

# game initialization
pygame.init()

# screen dimensions
screen_width = 1100
screen_height = 600

# center the game application
os.environ['SDL_VIDEO_CENTERED'] = '1'

#colors
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)

# text renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

#font
font = "Retro.ttf"

# game framerate
clock = pygame.time.Clock()
FPS = 30

# main menu
def main_menu():

    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        print("Start")
                    if selected=="quit":
                        pygame.quit()
                        quit()

    # main menu UI
    screen.fill(blue)
    title = text_format("Rummy Game", font, 90, black)
    if selected=="start":
        text_start = text_format("START", font, 75, yellow)
    else:
        text_start = text_format("START", font, 75, white)
    if selected=="quit":
        text_quit = text_format("QUIT", font, 75, yellow)
    else:
        text_quit = text_format("QUIT", font, 75, white)

    title_rect = title.get_rect()
    start_rect = text_start.get_rect()
    quit_rect = text_quit.get_rect()

    # main menu text
    screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
    screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
    screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
    pygame.display.update()
    clock.tick(FPS)
    pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")

# initialize menu
main_menu()
pygame.quit()
quit()