import Constantes 
import pygame

FPS = 30



WIN = pygame.display.set_mode((Constantes.WIDTH, Constantes.HEIGHT))
pygame.display.set_caption('El Mejor Othello Del Mundo')

tab_list = pygame.sprite.Group()
f_list = pygame.sprite.Group()

class Casilla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Constantes.CASILLA.convert()
        self.image.set_colorkey(Constantes.BLANCO)
        self.rect = self.image.get_rect()


def Llenar_Tablero():
    WIN.fill(Constantes.BLANCO)
    for fila in range(Constantes.FILAS):
        for col in range(Constantes.COLUMNAS):
            casilla = Casilla()
            casilla.rect.x = (fila * Constantes.BLOQUE_SIZE)
            casilla.rect.y = (col * Constantes.BLOQUE_SIZE)
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