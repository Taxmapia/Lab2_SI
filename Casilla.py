import Constantes , pygame

class Casilla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Constantes.CASILLA
        self.rect = self.image.get_rect()
    