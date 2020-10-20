import os
from Othello.constantes import *

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('El Mejor Othello Del Mundo')

tab_list = pygame.sprite.Group()
f_list = pygame.sprite.Group()

class Casilla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("casilla.png").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()


def Llenar_Tablero():
    WIN.fill(BLANCO)
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            casilla = Casilla()
            casilla.rect.x = (fila * BLOQUE_SIZE)
            casilla.rect.y = (col * BLOQUE_SIZE)
            tab_list.add(casilla)
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        Llenar_Tablero()
        tab_list.draw(WIN)
        pygame.display.update()
    pygame.quit()


main()