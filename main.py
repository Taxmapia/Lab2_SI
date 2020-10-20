import Constantes 
import pygame

FPS = 60


WIN = pygame.display.set_mode((Constantes.WIDTH, Constantes.HEIGHT))
pygame.display.set_caption('El Mejor Othello Del Mundo')

tab_list = pygame.sprite.Group()
f_list = pygame.sprite.Group()

class Ficha(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        if color == Constantes.R:
            self.color = Constantes.R
            self.image = Constantes.F_R
            self.image.set_colorkey(Constantes.BLANCO)
            self.rect = self.image.get_rect()
        else:
            self.color = Constantes.B
            self.image =  Constantes.F_A
            self.image.set_colorkey(Constantes.BLANCO)
            self.rect = self.image.get_rect()
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
            if (fila == 2 and col == 2) or (fila == 3 and col == 3):
                ficha = Ficha(Constantes.R)
                ficha.rect.x = (fila * Constantes.BLOQUE_SIZE)
                ficha.rect.y = (col * Constantes.BLOQUE_SIZE)
                f_list.add(ficha)
            elif (fila == 3 and col == 2) or (fila == 2 and col == 3):
                ficha = Ficha(Constantes.B)
                ficha.rect.x = (fila * Constantes.BLOQUE_SIZE)
                ficha.rect.y = (col * Constantes.BLOQUE_SIZE)
                f_list.add(ficha)

def main():
    print(Constantes.BLOQUE_SIZE)
    run = True
    clock = pygame.time.Clock()
    Llenar_Tablero()
    tab_list.draw(WIN)
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        f_list.draw(WIN)
        pygame.display.update()
        print("Hola")
    pygame.quit()


main()