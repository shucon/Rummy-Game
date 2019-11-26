#   priority order of suits
#    spade heart diamond club
import pygame, sys, os
import random   #to select cards
from pygame.locals import *
import math

# game initialization
pygame.init()

# center the game application
os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption('Rummy Game')

card_images = []
#generating random cards for player and computer
cardlist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
suitlist = ['spades', 'hearts', 'diamonds','clubs']
allCards = {}
for i in suitlist:
    for j in cardlist:
        allCards[str(j) +"_of_"+i] = 0
opponent_cards = []
player_cards = []
open_deck = []
flag = 0
while flag == 0:
    num = random.randint(1,13)
    suit = suitlist[random.randint(0,3)]
    card = str(num)+"_of_"+str(suit)
    if allCards[card] == 0:    #   make sure card doesn't repeat
        allCards[card] = 1
        open_deck.append(card)
        flag = 1

for i in range(13):
    flag = 0
    while flag == 0:
        num = random.randint(1,13)
        suit = suitlist[random.randint(0,3)]
        card = str(num)+"_of_"+str(suit)
        if allCards[card] == 0:    #   make sure card doesn't repeat
            allCards[card] = 1
            player_cards.append(card)
            flag = 1

for i in range(13):
    flag = 0
    while flag == 0:
        num = random.randint(1,13)
        suit = suitlist[random.randint(0,3)]
        card = str(num)+"_of_"+str(suit)
        if allCards[card] == 0:    #   make sure card doesn't repeat
            allCards[card] = 1
            opponent_cards.append(card)
            flag = 1


#   loading card images
for i in player_cards:
    tmp = pygame.image.load(i+".png").convert()
    tmp = pygame.transform.scale(tmp,(70,100))   #scale cards
    card_images.append(tmp)

bckg = pygame.image.load("pic.jpg").convert()   #load background image
bckg = pygame.transform.scale(bckg,(1100,600))  #scale background image

closed_deck = pygame.image.load("card_back.jpeg").convert()   #load background image
closed_deck = pygame.transform.scale(closed_deck,(70,100))  #scale background image


FPS = 30
fpsClock = pygame.time.Clock()
z=15
card_positions = []
# Initialize card positions
mouse_positions = []
for i in player_cards:
    card_positions.append([z,490])
    mouse_positions.append([-1,-1])
    z+=80
closed_deck_flag = 0

def add_card():
    flag = 0
    card = ""
    while flag == 0:
        num = random.randint(1,13)
        suit = suitlist[random.randint(0,3)]
        card = str(num)+"_of_"+str(suit)
        if allCards[card] == 0:    #   make sure card doesn't repeat
            allCards[card] = 1
            player_cards.append(card)
            flag = 1
    tmp = pygame.image.load(card+".png").convert()
    tmp = pygame.transform.scale(tmp,(70,100))   #scale cards
    card_images.append(tmp)
    mouse_positions.append([-1,-1])
    distance = 1045/len(player_cards)
    z=15
    card_positions.clear()
    # Initialize card positions
    mouse_positions.clear()
    for i in player_cards:
        card_positions.append([z,490])
        mouse_positions.append([-1,-1])
        z+=math.floor(distance)
    closed_deck_flag = 0

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bckg, [0, 0])
    screen.blit(closed_deck, [100, 200])
    mouse_pos = pygame.mouse.get_pos()
    if (closed_deck_flag == 1 and pygame.mouse.get_pressed()[0] == 0):
        closed_deck_flag = 0
    if ((mouse_pos[0] > 100 and mouse_pos[0] < 170) and (mouse_pos[1] > 200 and mouse_pos[0] < 300)\
                and pygame.mouse.get_pressed()[0] == 1 and closed_deck_flag == 0):    #Left click
        closed_deck_flag = 1
        add_card()
    # Update card positions
    for i in range(len(player_cards)):
        # If mouse in card bound 
        if ((mouse_pos[0] > card_positions[i][0] and mouse_pos[0] < card_positions[i][0]+70) and (mouse_pos[1] > card_positions[i][1] and mouse_pos[0] < card_positions[i][1]+100)\
                and pygame.mouse.get_pressed()[0] == 1):    #Left click
            if (mouse_positions[i] == [-1,-1]):
                mouse_positions[i] = mouse_pos
            else:
                tmp = mouse_pos[0] - mouse_positions[i][0]
                card_positions[i][0] += tmp
                tmp = mouse_pos[1] - mouse_positions[i][1]
                card_positions[i][1] += tmp
                mouse_positions[i] = mouse_pos
        
        if (pygame.mouse.get_pressed()[0] == 0):
            card_positions[i][1] = 490

        screen.blit(card_images[i],card_positions[i])

    pygame.display.update()
    fpsClock.tick(FPS)