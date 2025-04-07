import pygame
import constantes
from personaje import Personaje
from arma import Arma
from textos import DamageText
from items import Item
import os

#funciones
#funcion escalar imagen
def escalar_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image,(w*scale, h*scale))
    return nueva_imagen

#funcion contar elementos
def contar_elementos(directorio):
    return len(os.listdir(directorio))

#funcion listar nombres de elementos
def nombres_carpetas(directorio):
    return os.listdir(directorio)


pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))

pygame.display.set_caption("Choco Aventuras")

#fuentes
font = pygame.font.Font("Codificacion/fonts/Silver.ttf", 25)


#importar imagenes

#energia
corazon_vacio = pygame.image.load("Codificacion//sonido e imagenes//items//corazon//corazon_vacio.png").convert_alpha()
corazon_vacio = escalar_img(corazon_vacio, constantes.SCALA_CORAZON)
corazon_medio = pygame.image.load("Codificacion//sonido e imagenes//items//corazon//corazon_medio.png").convert_alpha()
corazon_medio = escalar_img(corazon_medio, constantes.SCALA_CORAZON)
corazon_lleno = pygame.image.load("Codificacion//sonido e imagenes//items//corazon//corazon_lleno.png").convert_alpha()
corazon_lleno = escalar_img(corazon_lleno, constantes.SCALA_CORAZON)

#personaje
animaciones =[]
for i in range(7):
    img = pygame.image.load(f"Codificacion//sonido e imagenes//personajes//personaje principal//imagen_{i}.jpg").convert_alpha()
    img = escalar_img(img, constantes.SCALA_PERSONAJE)                                         #imagen_{i}.png
    animaciones.append(img)


#enemigos
directorio_enemigos = "Codificacion//sonido e imagenes//personajes//enemigos"
tipo_enemigos = nombres_carpetas(directorio_enemigos)
animaciones_enemigos =[]
for eni in tipo_enemigos:
    lista_temp = []
    ruta_temp = f"Codificacion//sonido e imagenes//personajes//enemigos//{eni}"
    num_animaciones = contar_elementos(ruta_temp)
    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}//{eni}_{i + 1}.jpg").convert_alpha()
        img_enemigo = escalar_img(img_enemigo, constantes.SCALA_ENEMIGOS)
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)

#arma
imagen_pistola = pygame.image.load(f"Codificacion//sonido e imagenes//armas//pistola.png").convert_alpha()
imagen_pistola = escalar_img(imagen_pistola, constantes.SCALA_ARMA)

#balas
imagen_balas = pygame.image.load(f"Codificacion//sonido e imagenes//armas//balas//bullet.png").convert_alpha()
imagen_balas = escalar_img(imagen_balas, constantes.SCALA_ARMA)

#imagenes items
pocion_images = []
ruta_img = "Codificacion//sonido e imagenes//items//pocion"
num_pocion_images = contar_elementos(ruta_img)
for i in range(num_pocion_images):
    img = pygame.image.load(f"Codificacion//sonido e imagenes//items//pocion//PocionRoja_{i+1}.png")
    img = escalar_img(img, 0.50)
    pocion_images.append(img)

coin_images = []
ruta_img = "Codificacion//sonido e imagenes//items//moneda"
num_coin_images = contar_elementos(ruta_img)
for i in range(num_coin_images):
    img = pygame.image.load(f"Codificacion//sonido e imagenes//items//moneda//Coin-{i+1}.png")
    img = escalar_img(img, 0.10)
    coin_images.append(img)


def vida_jugador():
    c_mitad_dibujado = False
    for i in range(5):
        if  jugador.energia >= ((i + 1)* 20):
            ventana.blit(corazon_lleno, (5 + i * 50, 5))
        elif jugador.energia % 20 > 0 and c_mitad_dibujado == False:
            ventana.blit(corazon_medio, (5 + i * 50, 5))
            c_mitad_dibujado = True
        else:
            ventana.blit(corazon_vacio, (5 + i * 50, 5))
        

#Crear jugador clase personaje
jugador = Personaje(50, 50, animaciones, 100)

#Enemigo de la clase personaje
golemAzul = Personaje(400, 300, animaciones_enemigos[0], 100)
pesteNegra = Personaje(200, 200, animaciones_enemigos[1], 100)
golemAzul_2 = Personaje(100, 250, animaciones_enemigos[0], 100)
pesteNegra_2 = Personaje(100, 150, animaciones_enemigos[1], 100)

#Crear lista de enemigos
lista_enemigos = []
lista_enemigos.append(golemAzul)
lista_enemigos.append(golemAzul_2)
lista_enemigos.append(pesteNegra)
lista_enemigos.append(pesteNegra_2)


#crear un arma

pistola = Arma(imagen_pistola, imagen_balas)

#crear un grupo de sprites
grupo_damage_text = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group()
grupo_items = pygame.sprite.Group()

moneda = Item(350, 25, 0, coin_images)
pocion = Item(380, 55, 1, pocion_images)

grupo_items.add(moneda)
grupo_items.add(pocion)


mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = pygame.time.Clock()

run = True
while run == True:
    #que vaya a 60 fps

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

    #actualiza el estado del jugador
    jugador.update()

    #actualizar el estado de enemigos
    for ene in lista_enemigos:
        ene.update()

    #actualizar el estado del arma
    bala = pistola.update(jugador)
    if bala:
        grupo_balas.add(bala)
    for bala in grupo_balas:
        damage, pos_damage = bala.update(lista_enemigos)
        if damage:
            damage_text = DamageText(pos_damage.centerx, pos_damage.centery, str(damage), font, constantes.ROJO)
            grupo_damage_text.add(damage_text)



    #actualizar daño
    grupo_damage_text.update()

    #actualizar items
    grupo_items.update()

    #dibujar al jugador
    jugador.dibujar(ventana)

    #dibujar al jugador
    for ene in lista_enemigos:
        ene.dibujar(ventana)

    #dibujar el arma
    pistola.dibujar(ventana)

    #dibujar balas
    for bala in grupo_balas:
        bala.dibujar(ventana)

    #dibujar corazones
    vida_jugador()

    #dibujar textos
    grupo_damage_text.draw(ventana)

    #dibujar items
    grupo_items.draw(ventana)

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