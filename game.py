#   priority order of suits
#    spade heart diamond club
import pygame, sys, os
import random   #to select cards
from pygame.locals import *
import math, time

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

left_cards_closed_deck = []
for key,value in allCards.items():
    if value == 0:
        left_cards_closed_deck.append(key)

#   loading card images
for i in player_cards:
    tmp = pygame.image.load(i+".png").convert()
    tmp = pygame.transform.scale(tmp,(70,100))   #scale cards
    card_images.append(tmp)

bckg = pygame.image.load("pic.jpg").convert()   #load background image
bckg = pygame.transform.scale(bckg,(1100,600))  #scale background image

closed_deck = pygame.image.load("card_back.jpeg").convert()   #load background image
closed_deck = pygame.transform.scale(closed_deck,(70,100))  #scale background image'

open_deck_img = pygame.image.load(open_deck[0]+".png").convert()   #load background image
open_deck_img = pygame.transform.scale(open_deck_img,(70,100))  #scale background image

finish_slot = pygame.image.load("joker.png").convert()   #load background image
finish_slot = pygame.transform.scale(finish_slot,(70,100))  #scale background image

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

def add_card_frm_closed_deck():
    card = ""
    num = random.randint(1,len(left_cards_closed_deck))
    card = left_cards_closed_deck[num-1]
    player_cards.append(card)
    del left_cards_closed_deck[num-1]

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

def add_card_frm_open_deck():
    global open_deck_img
    card_images.append(open_deck_img)
    player_cards.append(open_deck[-1])
    open_deck.pop()
    if (len(open_deck) == 0):
        open_deck_img = pygame.image.load("joker.png").convert()   #load background image
        open_deck_img = pygame.transform.scale(open_deck_img,(70,100))  #scale background image
    else:
        open_deck_img = pygame.image.load(open_deck[-1]+".png").convert()   #load background image
        open_deck_img = pygame.transform.scale(open_deck_img,(70,100))  #scale background image
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

add_card_status = 0
update_card_pos = 0
def cpu_play():
    card = ""
    num = random.randint(1,2)
    # Pick from closed set
    if num == 1 and len(left_cards_closed_deck):
        num = random.randint(1,len(left_cards_closed_deck))
        card = left_cards_closed_deck[num-1]
        opponent_cards.append(card)
        del left_cards_closed_deck[num-1]
    # Pick from open set
    else:
        global open_deck_img
        opponent_cards.append(open_deck[-1])
        open_deck.pop()
        if (len(open_deck) == 0):
            open_deck_img = pygame.image.load("joker.png").convert()   #load background image
            open_deck_img = pygame.transform.scale(open_deck_img,(70,100))  #scale background image
        else:
            open_deck_img = pygame.image.load(open_deck[-1]+".png").convert()   #load background image
            open_deck_img = pygame.transform.scale(open_deck_img,(70,100))  #scale background image
    
    # move a card from opponent set to open set
    num = random.randint(1,14)
    open_deck.append(opponent_cards[num-1])
    del opponent_cards[num-1]
    open_deck_img = pygame.image.load(open_deck[-1]+".png").convert()   #load background image
    open_deck_img = pygame.transform.scale(open_deck_img,(70,100))  #scale background image

cpu_chance = 0
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bckg, [0, 0])
    if len(left_cards_closed_deck) != 0:
        screen.blit(closed_deck, [100, 200])
    else:
        screen.blit(finish_slot, [100, 200])
    screen.blit(open_deck_img, [500, 200])
    screen.blit(finish_slot, [900, 200])
    mouse_pos = pygame.mouse.get_pos()
    
    # Add card from closed deck
    if ((mouse_pos[0] > 100 and mouse_pos[0] < 170) and (mouse_pos[1] > 200 and mouse_pos[1] < 300)\
                and pygame.mouse.get_pressed()[0] == 1 and add_card_status == 0\
                    and update_card_pos == 0 and len(left_cards_closed_deck)):    #Left click
        closed_deck_flag = 1
        add_card_frm_closed_deck()
        add_card_status = 1

    # Add card from open deck
    if ((mouse_pos[0] > 500 and mouse_pos[0] < 570) and (mouse_pos[1] > 200 and mouse_pos[1] < 300)\
                and pygame.mouse.get_pressed()[0] == 1 and add_card_status == 0\
                    and update_card_pos == 0):    #Left click
        add_card_frm_open_deck()
        add_card_status = 1
    
    # Delete card positions
    if (add_card_status == 1 and pygame.mouse.get_pressed()[0] == 1 and update_card_pos == 0):
        for i in range(len(player_cards)):
            # If mouse in card bound 
            if ((mouse_pos[0] > card_positions[i][0] and mouse_pos[0] < card_positions[i][0]+70) and\
                     (mouse_pos[1] > card_positions[i][1] and mouse_pos[1] < card_positions[i][1]+100)):    #Left click
                add_card_status = 0
                open_deck.append(player_cards[i])
                del player_cards[i]
                del card_positions[i]
                del mouse_positions[i]
                open_deck_img = card_images[i]
                del card_images[i]
                # CPU completes it's turn
                cpu_chance = 1
                break

    # Update card positions
    for i in range(len(player_cards)):
        # If mouse in card bound 
        if ((mouse_pos[0] > card_positions[i][0] and mouse_pos[0] < card_positions[i][0]+70) and (mouse_pos[1] > card_positions[i][1] and mouse_pos[1] < card_positions[i][1]+100)\
                and pygame.mouse.get_pressed()[0] == 1):    #Left click
            update_card_pos = 1
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
            update_card_pos = 0

        screen.blit(card_images[i],card_positions[i])

        z = 15
        for i in range(13):
            screen.blit(closed_deck,[z,10])
            z += 80

    pygame.display.update()
    fpsClock.tick(FPS)

    # Hacky fix
    if cpu_chance:
        cpu_chance += 1
        if cpu_chance == 32:
            # time.sleep(2)
            cpu_play()
            cpu_chance = 0