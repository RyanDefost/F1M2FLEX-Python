import sys
import pygame
from pygame.locals import *

# Necessary setup before you can start using pygame functionalities:
pygame.init()


KEYS_DOWN = []

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 30

BG_COLOUR = [0, 0, 0]
IS_RUNNING = True


class blauwdruk:
    
    hp = 10
    lives = 5
    speed = 10
    item = None

    def __init__(self, lives):

        self.lives = lives
        self.speed = speed

    def walk(self):
        print("Het Character loopt met een snelheid van:", self.speed)
#---------------------------------------------------------

#Tests in interface of het werkt:
testPlayer = blauwdruk
print("blauwdruk.lives: ", blauwdruk.lives)


class player(blauwdruk):

    money = 15
    points = 0

    def __init__(self):
        super().__init__

        self.lives = 30
        self.speed = 20
    
    def walk(self):
        print("Mario loopt heel anders, maar wel met de snelheid", self.speed)

    def jump(self):
        print("Mario springt")
#---------------------------------------------------------    
#Tests in interface of het werkt:
player1 = player()

print("player1 lives:", player1.lives)
print("player1 speed:", player1.speed)






playerSprite = pygame.image.load("../Art/spr_Player.png")
playerRect = playerSprite.get_rect()  

playerSpeed = player1.speed


while IS_RUNNING:


    # ------------------------------------------------
    # INPUT REGISTRATION:
    # ------------------------------------------------
    KEYS_DOWN = pygame.key.get_pressed()


    # ------------------------------------------------
    # EVENT HANDLING:
    # ------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    # ------------------------------------------------
    # UPDATE GAME LOGIC:
    # ------------------------------------------------
    if (KEYS_DOWN[K_UP]):
        playerRect.y -= playerSpeed
    elif (KEYS_DOWN[K_DOWN]):
        playerRect.y += playerSpeed

    if (KEYS_DOWN[K_LEFT]):
        playerRect.x -= playerSpeed
    elif (KEYS_DOWN[K_RIGHT]):
        playerRect.x += playerSpeed
    

    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    # First clear the screen with a background color.
    # If you don't, you'll draw on top of what was previously drawn. See for yourself by removing/commenting this line... :)
    SCREEN.fill(BG_COLOUR)

    # Then draw sprites on the current location:
    SCREEN.blit(playerSprite, playerRect)
    
    # Finally refresh the entire screen of this application window:
    pygame.display.flip()


    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
