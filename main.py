import Constantes 
import pygame

FPS = 30



WIN = pygame.display.set_mode((Constantes.WIDTH, Constantes.HEIGHT))
pygame.display.set_caption('El Mejor Othello Del Mundo')

tab_list = pygame.sprite.Group()
f_list = pygame.sprite.Group()

class Ficha(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        if color == Constantes.R:
            self.color = Constantes.R
            self.ficha_roja = Constantes.F_R.convert()
            self.ficha_roja.set_colorkey(Constantes.BLANCO)
            self.rect = self.ficha_rojo.get_rect()
        else:
            self.color = Constantes.B
            self.ficha_azul =  Constantes.F_A.convert()
            self.ficha_azul.set_colorkey(Constantes.BLANCO)
            self.rect = self.ficha_azul.get_rect()
        self.x , self.y = 0 , 0
        
        

    def Color(self):
        print(self.color)

class Casilla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Constantes.CASILLA
        self.rect = self.image.get_rect()
    def Calc_pos(self):
        print()


def Llenar_Tablero():
    WIN.fill(Constantes.NEGRO)
    for fila in range(Constantes.FILAS):
        for col in range(Constantes.COLUMNAS):
            casilla = Casilla()
            casilla.rect.x = (fila * Constantes.BLOQUE_SIZE)
            casilla.rect.y = (col * Constantes.BLOQUE_SIZE)
            tab_list.add(casilla)
def main():
    print(Constantes.BLOQUE_SIZE)
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