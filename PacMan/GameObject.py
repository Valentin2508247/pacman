import pygame

class GameObject(object):
    """base class for moving objects"""
    def __init__(self, x, y, images_up, images_down, images_left, images_right, map, *args, **kwargs):
        self.startx = x
        self.starty = y
        self.start_direction = self.direction
        
        
        self.map = map
        self.images_up = images_up
        self.images_down = images_down
        self.images_left = images_left
        self.images_right = images_right
        self.images = images_right
        self.index = 0
        self.image = self.images[self.index]
        
        if self.direction == "right":
            self.speedx = 1
            self.speedy = 0
        if self.direction == "left":
            self.speedx = -1
            self.speedy = 0
        if self.direction == "up":
            self.speedx = 0
            self.speedy = -1
        if self.direction == "down":
            self.speedx = 0
            self.speedy = 1





        self.rect = self.image.get_rect(topleft = (x, y))
        self.next_image = 1
        
        #self.tile = tile
        return super().__init__(*args, **kwargs)
      
    


    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def to_start_position(self):
        self.rect.x = self.startx
        self.rect.y = self.starty
        self.direction = self.start_direction
        self.change_direction(self.start_direction)
