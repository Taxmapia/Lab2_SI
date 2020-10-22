import Constantes , pygame
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