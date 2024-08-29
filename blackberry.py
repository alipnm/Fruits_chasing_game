from pygame.sprite import Group
from constants import *
from root import Fruit
class Blackberry(Fruit):
    def __init__(self, x: int, y: int, group: Group):
        super().__init__(x, y, group)
        self.image = pygame.image.load("assets/Blackberry.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.price = 8
    def update(self, money : int):
        return super().update(money)