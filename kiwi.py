from constants import *
from root import Fruit
class Kiwi(Fruit):
    def __init__(self, x: int, y: int, group: pygame.sprite.Group):
        super().__init__(x, y, group)
        self.image = pygame.image.load("assets/Kiwi.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.price = 7
    def update(self, money : int):
        return super().update(money)