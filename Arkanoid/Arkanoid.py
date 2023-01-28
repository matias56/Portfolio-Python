import pygame
from pygame import*
from pygame.locals import*
import random

class pelotaA:
    def __init__(self,ventana, x, y):
        
        self.ventana = ventana
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255), (self.x, self.y, 10, 10))
    def movimiento(self):
        self.x+=self.vx
        self.y+=self.vy
    

   

class Raqueta:
    def __init__(self, ventana):
        self.tamaño = 80
        self.x = 600/2 - self.tamaño/2
        self.y = 380
        self.centro = self.x + self.tamaño/2
        self.ventana = ventana
        self.izq = False
        self.der = False
    def movimiento(self):
        if self.izq:
            self.x -= 10
        if self.der:
            self.x += 10
        self.x = 0 if self.x < 0 else 600 - self.tamaño if self.x + self.tamaño > 600 else self.x
        self.centro = self.x + self.tamaño / 2

    def dibujar(self):
        pygame.draw.rect(self.ventana, (255, 255, 255),
                         (self.x, self.y, self.tamaño, 10))


class Bloques:
    def __init__(self, ventana):
        self.ventana = ventana
        self.tablero = [[4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
                        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
                        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def dibujar(self):
        for i in range(4):
            for j in range(10):
                if self.tablero[i][j] != 0:
                    if self.tablero[i][j] == 4:
                        color = (255, 255, 255)
                    elif self.tablero[i][j] == 3:
                        color = (55, 255, 255)
                    elif self.tablero[i][j] == 2:
                        color = (55, 55, 255)
                    elif self.tablero[i][j] == 1:
                        color = (255, 55, 255)
                    pygame.draw.rect(self.ventana, color,
                                     (j*60, i*10 + 35, 59, 9))

def reiniciar(ventana):
     ventana.fill((0, 0, 0))
     bola.dibujar()
     r1.dibujar()
     tablero.dibujar()


def rebotar():
    if bola.y < 3*10+35+9:
        for i in range(4):
            for j in range(10):
                if tablero.tablero[i][j] != 0:
                    if ((j*60 < bola.x < j*60 + 59) or (j*60 < bola.x + 10 < j*60 + 59)) and ((i * 10 + 35 < bola.y < i * 10 + 35 + 9) or (i * 10 + 35 < bola.y + 10 < i * 10 + 35 + 9)):
                        tablero.tablero[i][j] = 0
                        bola.vy *= -1

def main():
    global bola, font, r1, tablero
    ventana = pygame.display.set_mode((600, 400))
    ventana.fill((0, 0, 0))
    bola = pelotaA(ventana, 50, 100)
    bola.vx = 5
    bola.vy = 2
    pygame.init()
    pygame.display.set_caption("Mi Juego de Arkanoid")
    jugando = True
    r1 = Raqueta(ventana)
    tablero = Bloques(ventana)
    clock = pygame.time.Clock()
    while jugando:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    r1.izq = True
                if event.key == pygame.K_RIGHT:
                    r1.der = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    r1.izq = False
                if event.key == pygame.K_RIGHT:
                    r1.der = False
        bola.movimiento()
        r1.movimiento()
        rebotar()
        if bola.x >= 590:
            bola.vx *= -1
            bola.x = 590
           
        if bola.x <= 0:
            bola.vx *= -1
            bola.x = 0
           
        if bola.y + 10 > r1.y:
            if (r1.x < bola.x < r1.x + r1.tamaño) or (r1.x < bola.x + 10 < r1.x + r1.tamaño):
                porcentaje = (bola.x - r1.centro) / (r1.tamaño / 2)
                bola.vx += porcentaje*10
                bola.vx = -10 if bola.vx < -10 else 10 if bola.vx > 10 else bola.vx
                bola.vy *= -1
                bola.y = r1.y - 10
                
            elif bola.y > 400:
                bola.y = 100
        if bola.y <= 0:
            bola.vy *= -1
            bola.y = 0
            
        reiniciar(ventana)
        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
    pygame.quit()
