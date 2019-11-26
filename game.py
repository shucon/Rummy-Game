#   priority order of suits
#    spade heart diamond club
import pygame, sys, os
import random   #to select cards
from pygame.locals import *

# game initialization
pygame.init()

# center the game application
os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption('Rummy Game')

#generating random cards for player and computer
player_card_names = []
cardlist = []
suitlist = ['spades', 'hearts', 'diamonds','clubs']
for i in range(26):
    bonus = 0
    while bonus == 0:
        num = random.randint(1,13)
        suit = suitlist[random.randint(0,3)]
        card = str(num)+"_of_"+str(suit)+".png"
        if card not in cardlist:    #   make sure card doesn't repeat
            cardlist.append(card)
            if len(player_card_names)<=12:
                player_card_names.append(card)  #   append player card names for sort function
            bonus = 1


#   loading card images
for i in range(26):
    globals()['card%s'%i] = pygame.image.load(cardlist[i]).convert()
    globals()['card%s'%i] = pygame.transform.scale(globals()['card%s'%i],(70,100))   #scale cards

#   making player and computer sets
player_cards = []
computer_cards = []
for i in range(13):
    player_cards.append(globals()['card%s'%i])
    computer_cards.append(globals()['card%s'%(i+13)])

bckg = pygame.image.load("pic.jpg").convert()   #load background image
bckg = pygame.transform.scale(bckg,(1100,600))  #scale background image

# def sort():
#     '''call this function when sort button is pressed'''
#     clubs, hearts, spades, diamonds = {}, {}, {}, {}

#     for i in range(13):
#         if "clubs" in player_card_names[i]:
#             clubs[i] = globals()['card%s'%i]
#         elif "hearts" in player_card_names[i]:
#             hearts[i] = globals()['card%s'%i]
#         elif "spades" in player_card_names[i]:
#             spades[i] = globals()['cards%s'%i]
#         else:
#             diamonds[i] = globals()['cards%s'%i]
#     #sorted_list = [clubs,hearts,spades,diamonds]
#     for i in suitlist:
#         for key, value in sorted(i.items(), key=lambda kv: kv[1]):
#         for value     
#             #print("1 Euro = %s %s" % (value,key))

#     pass

def discard():
    pass

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bckg, [0, 0])

    z=15
    for i in player_cards:
        screen.blit(i,(z,490))
        z+=80
    z=15


    pygame.display.update()
