from constants import *
from root import Fruit
class Apple(Fruit):
    def __init__(self, x: int, y: int, group: pygame.sprite.Group):
        super().__init__(x, y, group)
    def update(self, money : int):
        return super().update(money)