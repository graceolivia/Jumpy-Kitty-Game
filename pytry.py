# Import and initialize the pygame library
import pygame
import math
import random

# initialize the pygame
pygame.init()

# create the screen - width, height
screen = pygame.display.set_mode((1000, 400))

# title and icon
pygame.display.set_caption("fairy escape")
icon = pygame.image.load('flower-shop.png')
background = pygame.image.load('16552.jpg')

pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('fairy.png')
playerX = 500
playerY = 300
playerX_change = 0
playerY_change = 0
# sparkle
# ready state means you can't see it
# fire means sparkle is moving
sparkleImg = pygame.image.load("sparkle.png")
sparkleX = playerX
sparkleY = playerY
sparkleX_change = 0
sparkleY_change = 10
sparkle_state = "ready"

flowerImg = []
flowerX = []
flowerY = []
flowerX_change = []
flowerY_change = []
num_of_flowers = 6

# flower
for i in range(num_of_flowers):
    flowerImg.append(pygame.image.load('flower.png'))
    flowerX.append(random.randint(10, 50))
    flowerY.append(random.randint(50, 150))
    flowerX_change.append(5)
    flowerY_change.append(20)

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score_count = font.render("Score : " + str(score), True, (0, 0, 0))
    screen.blit(score_count, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def flower(x, y, i):
    screen.blit(flowerImg[i], (x, y))


def fire_sparkle(x, y):
    global sparkle_state
    sparkle_state = "fire"
    screen.blit(sparkleImg, (x, y))


def isCollision(flowerX, flowerY, sparkleX, sparkleY):
    distance = math.sqrt((math.pow(flowerX - sparkleX, 2)) + (math.pow(flowerY - sparkleY, 2)))
    if distance < 20:
        return True
    else:
        return False


# game loop
running = True
while running:
    # this happens first
    screen.fill((229, 204, 255))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_UP:
                playerY_change = -10
            if event.key == pygame.K_DOWN:
                playerY_change = 10
            if event.key == pygame.K_SPACE:
                if sparkle_state == "ready":
                    sparkleX = playerX
                    sparkleY = playerY
                    fire_sparkle(sparkleX, sparkleY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # player movement
    if playerX >= 950:
        playerX = 950
    if playerX <= 0:
        playerX = 0
    if playerY >= 350:
        playerY = 350
    if playerY <= 0:
        playerY = 0

    # flower movement
    for i in range(num_of_flowers):
        if flowerX[i] >= 950:
            flowerX_change[i] = -5
            flowerY[i] += flowerY_change[i]
        if flowerX[i] <= 0:
            flowerX_change[i] = 5
            flowerY[i] += flowerY_change[i]
        if flowerY[i] >= 350:
            flowerY_change[i] = -20
        if flowerY[i] <= 0:
            flowerY_change[i] = 20


        # collision
        collision = isCollision(flowerX[i], flowerY[i], sparkleX, sparkleY)
        if collision:
            sparkleY = playerY
            sparkleX = playerX
            sparkle_state = "ready"
            score += 1
            print(score)
            flowerX[i] = random.randint(10, 50)
            flowerY[i] = random.randint(50, 150)

        flowerX[i] += flowerX_change[i]
        flower(flowerX[i], flowerY[i], i)

    # bullet movement
    if sparkleY <= 0:
        sparkle_state = "ready"
    if sparkle_state == "fire":
        fire_sparkle(sparkleX, sparkleY)
        sparkleY -= sparkleY_change

    playerY += playerY_change
    playerX += playerX_change

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
