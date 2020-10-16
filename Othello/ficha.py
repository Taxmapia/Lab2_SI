from .constantes import *

class Ficha(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__()
        self.f_a = pygame.image.load("imag/Ficha_Azul.png")
        self.f_r = pygame.image.load("imag/Ficha_Roja.png")
        self.rect1 = self.f_a.get_rect()
        self.rect2 = self.f_r.get_rect()
        self.f_a.set_colorkey(BLANCO)
        self.f_r.set_colorkey(BLANCO)

    def Dibujar(self,win,color):
        if color = R:
            win