from Othello.constantes import *
from Othello.tablero import Tablero
import Othello.ficha

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('El Mejor Othello Del Mundo')

f_list = pygame.sprite.Group()

def main():
    run = True
    clock = pygame.time.Clock()
    tablero = Tablero()
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        tablero.Dibujar_Cuadro(WIN)
        pygame.display.update()
    pygame.quit()


main()