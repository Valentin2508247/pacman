import pygame 

class Food(object):
    
    def __init__(self, x, y, game, tile, *args, **kwargs):
        self.image = pygame.image.load("res\\food.gif")
        self.rect = self.image.get_rect(topleft = (x, y))
        self.tile = tile
        self.game = game
        self.x = x + 8
        self.y = y + 8
        self.score = 10
        self.sound = "audio\\eating.ogg"

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def eat(self):
        self.game.score += self.score
        self.tile.food = None
        self.tile.food_type = 0

        

class Energiser(Food):

    #def __init__(self, x, y, game, tile, *args, **kwargs):
     #   self.image = pygame.image.load("res\\food-power.gif")
      #  self.rect = self.image.get_rect(topleft = (x, y))
       # self.tile = tile
        #self.game = game
    def __init__(self, x, y, game, tile, *args, **kwargs):
        super().__init__(x, y, game, tile, *args, **kwargs)
        self.image = pygame.image.load("res\\food-power.gif")
        self.score = 50
        self.sound = "audio\\eatpill.ogg"

