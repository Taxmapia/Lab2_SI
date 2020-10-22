#Librerias y Paquetes
import Constantes , Casilla , pygame , Ficha

FPS = 60

WIN = pygame.display.set_mode((Constantes.WIDTH, Constantes.HEIGHT)) #Define una ventana como WIN
pygame.display.set_caption('El Mejor Othello Del Mundo')#Nombre de la ventana

#Listas de los sprites segun su tipo
tab_list = pygame.sprite.Group()
f_list = pygame.sprite.Group()

#Funcion que inicializa el tablero con las primeras fichas
def Llenar_Tablero():
    fila , col = 0 , 0
    for fila in range(Constantes.FILAS):
        for col in range(Constantes.COLUMNAS):
            casilla = Casilla.Casilla()
            casilla.rect.x = (fila * Constantes.BLOQUE_SIZE)
            casilla.rect.y = (col * Constantes.BLOQUE_SIZE)
            tab_list.add(casilla)
            if (fila == 2 and col == 2) or (fila == 3 and col == 3):
                ficha = Ficha.Ficha(Constantes.R)
                ficha.rect.x = (fila * Constantes.BLOQUE_SIZE)
                ficha.rect.y = (col * Constantes.BLOQUE_SIZE)
                f_list.add(ficha)
            elif (fila == 3 and col == 2) or (fila == 2 and col == 3):
                ficha = Ficha.Ficha(Constantes.B)
                ficha.rect.x = (fila * Constantes.BLOQUE_SIZE)
                ficha.rect.y = (col * Constantes.BLOQUE_SIZE)
                f_list.add(ficha)

def Agregar_Ficha(pos_x,pos_y):
    ficha = Ficha.Ficha(Constantes.R)
    ficha.rect.x = pos_x
    ficha.rect.y = pos_y
    f_list.add(ficha)

    

def main():

    run = True
    clock = pygame.time.Clock()
    Llenar_Tablero()
    tab_list.draw(WIN)

    #Ciclo del juego hasta que se cierre o se termine
    while run:
        clock.tick(FPS)
        
        #Captura de eventos (ej: apretar un boton del mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for i in tab_list:
                    if i.rect.collidepoint(pos):
                        print (str(i.rect.x) + " " + str(i.rect.y))
                        Agregar_Ficha(i.rect.x , i.rect.y)
        
        f_list.draw(WIN)
        pygame.display.update()
    pygame.quit()


main()