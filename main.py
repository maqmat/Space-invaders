import pygame
import random
#iniciar pygame
pygame.init()
#tamaño de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 900
#zize variable
ZIZE = ( SCREEN_WIDTH, SCREEN_HEIGTH )
#idsplay window
screen = pygame.display.set_mode(ZIZE)
#titulo
pygame.display.set_caption("space invaders adakademy")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)
playerimage = pygame.image.load("space-invaders.png")
playerx = 200
playery = 800
playerxchange = 0

def player (x , y):
    screen.blit(playerimage, (x,y))
#hacer que la pantalla se quede abierta
running = True
"""c1 = int(random.randint(1, 255))
c2 = int(random.randint(1, 255))
c3 = int(random.randint(1, 255))"""
while running:
    #playerx += 0.1
    #print(playerx)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange = -0.5

            if event.key == pygame.K_RIGHT:
                playerxchange = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerxchange == 0
        


    #color de fondo rgb
    #aqui el comando de ramdom (esto lo puse pq si pero no deberia)
    rgb = (128, 128, 128 )
    screen.fill(rgb)
    #incremento de la variable x
    playerx += playerxchange

    
    if playerx <= 0:
        playerx = 0
    

    elif playerx >= 736:
        playerx = 736
    

    player(playerx,playery)
   
    #actualizar la pantalla
    pygame.display.update()



