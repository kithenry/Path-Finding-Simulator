import pygame

# Initialize game Window
pygame.init()


# create screen
screen = pygame.display.set_mode((1000,600))


# Window config
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Images/ufo_1.png") # some image
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load("Images/spaceship.png")
playerX = 450
playerY = 500

def player():
    screen.blit(playerImg, (playerX, playerY))


# Game loop
running = True
while running:
    
    # RGB (Red Green Blue)
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # filling the screen

    player()
    rectangle  = pygame.Rect(300,400,50,50)
    pygame.draw.rect(screen, (200,0,0),rectangle,0,3)
    pygame.display.update()


