from constants import *
from root import Fruit
class Cherry(Fruit):
    def __init__(self, x: int, y: int, group: pygame.sprite.Group):
        super().__init__(x, y, group)
        self.image = pygame.image.load("assets/Cherry.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.price = 4
    def update(self, money : int):
        return super().update(money)