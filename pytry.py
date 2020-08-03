# Import and initialize the pygame library
import pygame
import random

#initialize the pygame
pygame.init()

#create the screen - width, height
screen = pygame.display.set_mode((1000, 400))

#title and icon
pygame.display.set_caption("fairy escape")
icon = pygame.image.load('flower-shop.png')
background = pygame.image.load('16552.jpg')

pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('fairy.png')
playerX = 500
playerY = 300

#sparkle
sparkleImg = pygame.image.load("sparkle.png")
sparkleX = playerX
sparkleY = playerY
sparkleX_change = 0
sparkleY_change = 5
sparkle_state = "ready"

#flower
flowerX = 0
flowerY = 0
flowerX_change = 0
flowerY_change = 0
#ready state means you can't see it
# fire means sparkle is moving



flowerImg = pygame.image.load('flower.png')
flowerX = random.randint(10, 50)
flowerY = random.randint(50, 350)
flowerX_change = 5
flowerY_change = 20

def player(x, y):
    screen.blit(playerImg, (x, y))

def flower(x, y):
    screen.blit(flowerImg, (x, y))

def fire_sparkle(x, y):
    global sparkle_state
    sparkle_state = "fire"
    screen.blit(sparkleImg, (x, y))


#game loop
running = True
while running:
    #this happens first
    screen.fill((229, 204, 255))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            running = False

    #if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 10
        if event.key == pygame.K_RIGHT:
            playerX += 10
        if event.key == pygame.K_UP:
            playerY -= 10
        if event.key == pygame.K_DOWN:
            playerY += 10
        if event.key == pygame.K_SPACE:
            if sparkle_state == "ready":
                fire_sparkle(playerX, playerY)


    #player movement
    if playerX >= 950:
        playerX = 950
    if playerX <= 0:
        playerX = 0
    if playerY >= 350:
        playerY = 350
    if playerY <= 0:
        playerY = 0

    #flower movement

    if flowerX >= 950:
        flowerX_change = -5
        flowerY += flowerY_change
    if flowerX <= 0:
        flowerX_change = 5
        flowerY += flowerY_change
    if flowerY >= 350:
        flowerY_change = -20
    if flowerY <= 0:
        flowerY_change = 20
        playerY = 0

    #bullet movement
    if sparkle_state == "fire":
        fire_sparkle(sparkleX, sparkleY)
        sparkleY -= sparkleY_change
        if sparkleY <= 0:
            sparkle_state = "ready"
            sparkleX = playerX
            sparkleY = playerY


    player(playerX, playerY)
    flower(flowerX, flowerY)

    flowerX += flowerX_change


    pygame.display.update()