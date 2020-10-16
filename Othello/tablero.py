from .constantes import BLANCO , NEGRO , FILAS , BLOQUE_SIZE , pygame
class Tablero:
    def __init__(self):
        self.fichas_rojas = self.fichas_azules = 2 
    def Dibujar_Cuadro(self,win):
        win.fill(NEGRO)
        for fila in range(FILAS):
            for col in range(fila % 2, FILAS , 2):
                pygame.draw.rect(win,BLANCO,(fila*BLOQUE_SIZE,col*BLOQUE_SIZE,BLOQUE_SIZE,BLOQUE_SIZE))