import pygame
import random
import math
from pygame import mixer
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
mixer.music.load("hotel.mp3")
mixer.music.play(-1)
#titulo
pygame.display.set_caption("space invaders adakademy")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)
playerimage = pygame.image.load("space-invaders.png")
playerx = 200
playery = 800
playerxchange = 0

enemy_image =  []
enemyx =  []
enemyy =  []
enemyxchange = []
enemyychange = []
number_enemy = 8

bullet_image = pygame.image.load("bullet.png")
bulletx = 0
bullety = 800
bulletychange = 4
bullet_state = "ready"

#configuracion de enemigo
for item in range( number_enemy ):
    enemy_image.append(pygame.image.load("sharko.png")) 
    enemyx.append(random.randint(0, 736)) 
    enemyy.append(random.randint(50, 150)) 
    enemyxchange.append(0.7) 
    enemyychange.append(60) 




def player (x , y):
    screen.blit(playerimage, (x,y))

def enemy (x , y, item):
    screen.blit(enemy_image[item], (x,y))

def fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x+20, y+10))

score = 0
scorefont = pygame.font.Font("duke.ttf", 32)

textx = 10
texty = 10

def showtext(x,y):
    scoretext = scorefont.render("score: "+ str(score), True, (255,255,255))
    screen.blit(scoretext, (x,y))

def is_colition(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx-bulletx)**2 + ( enemyy - bullety)**2)


    if distance < 27:
        return True
    else:
        return False

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
                    bulletsound = mixer.Sound("disparo.mp3")
                    bulletsound.play()
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

    
        


    
    for item in range(number_enemy):
        enemyx[item] += enemyxchange[item]
        if enemyx[item] >= 736:
            enemyxchange[item] = -0.7
            enemyy[item] += enemyychange[item]

        
        elif enemyx[item] <= 0:
            enemyxchange[item] = 0.7
            enemyy[item] += enemyychange[item]

        colition =is_colition(enemyx[item], enemyy[item], bulletx, bullety)
        if colition:
            bullet_state == "ready"
            score += 1
            print(score)
            enemyx[item] =random.randint(0, 736)
            enemyy[item] =random.randint(50, 150)
        enemy(enemyx[item],enemyy[item],item)


        


    if bullety <= 0:
        bullety = 800
        bullet_state = "ready"



    if bullet_state == "fire":
        fire(bulletx, bullety)
        bullety -= bulletychange 



    player(playerx,playery)

    showtext(textx,texty)
    
   
    #actualizar la pantalla
    pygame.display.update()



