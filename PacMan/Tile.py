import pygame
import Food

class Tile(object):
    """description of class"""
    def __init__(self, type, index, left, top, game, food_type = 0):
                                              #1 - food, 2 - energiser
        
        self.game = game                                      
        self.type = type
        self.image = pygame.image.load("res\\" + type + ".gif")
        self.rect = self.image.get_rect(topleft = (left, top))
        self.is_wall = not (type == "empty")
        self.index = index
        self.food_type = food_type
        if self.food_type == 0:
            self.food = None
        if food_type == 1:
            self.food = Food.Food(left, top, game, self)
        if food_type == 2:
            self.food = Food.Energiser(left, top, game, self)
            print(self.food.rect.width)

    
    def set_food(self, food):
        if food == 1:
            self.food_type = food
            self.food = Food.Food(self.rect.x, self.rect.y, self.game, self)
        elif food == 0:
            self.food_type = food
            self.food = None
        elif food == 2:
            self.food_type = food
            self.food = Food.Energiser(self.rect.x, self.rect.y, self.game, self)

            
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.food_type != 0:
            self.food.draw(surface)



