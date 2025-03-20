import pygame
import constantes
from personaje import Personaje

pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))

pygame.display.set_caption("Choco Aventuras")

player_image = pygame.image.load("Trabajo Final//sonido e imagenes//caminar//imagen 1.jpg")
#player_image = pygame.transform.scale(player_image,(player_image.get.width()*constantes.SCALA_PERSONAJE,player_image.get_height()*constantes.SCALA_PERSONAJE))

jugador = Personaje(50, 50, player_image)

mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.Clock()

run = True
while run == True:

    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)

    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD

    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD

    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD

    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD


    jugador.movimiento(delta_x, delta_y)


    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True      


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False      



    pygame.display.update()

pygame.quit()


