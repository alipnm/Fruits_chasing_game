from constants import *
class Button:
    def __init__(self, width : float, height : float, text : str = ''):
        """
        @param width: width of the button you want to make.
        @param height: height of the button you want to make.
        @param text: the text of the button you want to make and its in center of button.
        @attention: The position of the rect is at the topleft of the screen by default.
        The border of the button is white and the text is also white.
        the rectangle in the middle of the button is orange.
        """
        self.rect = pygame.rect.Rect(0, 0, width, height)
        self.fill_rect = pygame.rect.Rect(6, 6, width - 12, height - 12)
        self.inside_text = GAME_FONT.render(text, True, (255,255,255))
        self.inside_rect = self.inside_text.get_rect(center=self.fill_rect.center)
    def check_click(self):
        """
        @return: bool
        it will return that is the button clicked or not.
        """
        result = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                result = True
        return result
    def draw(self):
        """
        it will draw the button on the screen.
        """
        self.fill_rect.center = self.rect.center
        self.inside_rect.center = self.fill_rect.center
        pygame.draw.rect(screen, (255,255,255), self.rect, 6)
        pygame.draw.rect(screen, (255,140,0), self.fill_rect, 0)
        screen.blit(self.inside_text, self.inside_rect)