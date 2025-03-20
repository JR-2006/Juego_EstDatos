import pygame
import constantes

class Personaje():
    def __init__(self, x, y, image):
        self.flip = False
        self.image = image
        self.forma = pygame.Rect(0,0, constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE)
        self.forma.center = (x,y)


    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip = True
        if delta_y > 0:
            self.flip = False
            
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y


    def dibujar(self,interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        interfaz.blit(self.image, self.forma)
        #pygame.draw.rect(interfaz, constantes.COLOR_PERSONAJE, self.forma, 1)