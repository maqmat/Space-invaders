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
backgroundimage = pygame.image.load("ez.jpg")
#titulo
pygame.display.set_caption("space invaders adakademy")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)
playerimage = pygame.image.load("space-invaders.png")
playerx = 200
playery = 800
playerxchange = 0
#configuracion de enemigo
enemy_image = pygame.image.load("alienv2.png")
enemyx = random.randint(0, 736)
enemyy = random.randint(50, 150)
enemyxchange = 0.2
enemyychange = 30

bullet_image = pygame.image.load("bullet.png")
bulletx = 0
bullety = 800
bulletychange = 4
bullet_state = "ready"







def player (x , y):
    screen.blit(playerimage, (x,y))

def enemy (x , y):
    screen.blit(enemy_image, (x,y))

def fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x+20, y+10))
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

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletx = playerx
                fire(bulletx,bullety)


        
        


    #color de fondo rgb
    #aqui el comando de ramdom (esto lo puse pq si pero no deberia)
    rgb = (128, 128, 128 )
    screen.fill(rgb)

    screen.blit (backgroundimage, (0,0))


    #incremento de la variable x
    playerx += playerxchange

    
    if playerx <= 0:
        playerx = 0
    

    elif playerx >= 736:
        playerx = 736

    if enemyx <= 0:
        enemyx = 0
    

    elif enemyx >= 736:
        enemyx = 736
        


    

    enemyx += enemyxchange
    if enemyx >= 736:
        enemyxchange = -0.2
        enemyy += enemyychange

    
    elif enemyx <= 0:
        enemyxchange = 0.2
        enemyy += enemyychange


    if bullety <= 0:
        bullety = 800
        bullet_state = "ready"



    if bullet_state == "fire":
        fire(bulletx, bullety)
        bullety -= bulletychange 

    player(playerx,playery)
    enemy(enemyx,enemyy)
   
    #actualizar la pantalla
    pygame.display.update()



