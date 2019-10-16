import pygame

class Button(object):
    
    def __init__(self, x, y, text, font_size, clicked, rgb = (170, 19, 181),*args, **kwargs):

        self.clicked = clicked 
        self.text = text
        self.font_size = font_size
        f1 = pygame.font.SysFont(None, self.font_size)
        #self.image = f1.render(text, 1, (235, 245, 20))
        self.rgb = rgb
        self.image = f1.render(text, 1, self.rgb)
        self.rect = self.image.get_rect(topleft = (x, y))
    
    def _():
        a = 1

    def set_text(self, text):
        self.text = text
        f1 = pygame.font.SysFont(None, self.font_size)
        self.image = f1.render(text, 1, self.rgb)
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class ImageButton(object):
    
    def _(self):
        a = 1
    
    def __init__(self, x, y, filename, clicked, info = "", info2 = 0, *args, **kwargs):

        self.clicked = clicked 
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.info = info
        self.info2 = info2

    def draw(self, surface):
        surface.blit(self.image, self.rect)