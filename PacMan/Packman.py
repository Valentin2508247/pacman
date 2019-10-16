import pygame
import GameObject
import math
import Map

class Packman(GameObject.GameObject):
    """des
    cription of class"""
    def __init__(self, x, y, direction, map, *args, **kwargs):
        s = ""
        
        #iml = []
        #iml.append(pygame.image.load("res\\pacman.gif"))
        #for i in range(1, 9):
        #    s = "res\\pacman-l " + str(i)  + ".gif"
        #    iml.append(pygame.image.load(s))

        #imr = []
        #imr.append(pygame.image.load("res\\pacman.gif"))
        #for i in range(1, 9):
        #    s = "res\\pacman-r " + str(i) + ".gif"
        #    imr.append(pygame.image.load(s))

        #imd = []
        #imd.append(pygame.image.load("res\\pacman.gif"))
        #for i in range(1, 9):
        #    s = "res\\pacman-d " + str(i)  + ".gif"
        #    imd.append(pygame.image.load(s))

        #imu = []
        #imu.append(pygame.image.load("res\\pacman.gif"))
        #for i in range(1, 9):
        #    s = "res\\pacman-u " + str(i)  + ".gif"
        #    imu.append(pygame.image.load(s))

        iml = []
        for i in range(1, 9):
            s = "res\\pacman\\pacman-l " + str(i)  + ".gif"
            iml.append(pygame.image.load(s))
            iml.append(pygame.image.load(s))
            iml.append(pygame.image.load(s))
        imr = []
        for i in range(1, 9):
            s = "res\\pacman\\pacman-r " + str(i) + ".gif"
            imr.append(pygame.image.load(s))
            imr.append(pygame.image.load(s))
            imr.append(pygame.image.load(s))
        imd = []
        for i in range(1, 9):
            s = "res\\pacman\\pacman-d " + str(i)  + ".gif"
            imd.append(pygame.image.load(s))
            imd.append(pygame.image.load(s))
            imd.append(pygame.image.load(s))
        imu = []
        for i in range(1, 9):
            s = "res\\pacman\\pacman-u " + str(i)  + ".gif"
            imu.append(pygame.image.load(s))
            imu.append(pygame.image.load(s))
            imu.append(pygame.image.load(s))
        self.cnt = 0





        self.direction = direction
        self.last_direction = direction
        #self.rect = imu[0].get_rect(topleft = (x, y))
        self.is_stopped = False

        return super().__init__(x, y, imu, imd, iml, imr, map, *args, **kwargs)

    def stop(self):
        self.is_stopped = True

    def move(self):
        self.is_stopped = False
    
    def update(self):

        if not self.is_stopped:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0   
            self.image = self.images[self.index]
            self.rect.x += self.speedx
            self.rect.y += self.speedy  

    
        
            
           
       

    def change_direction(self, direction):
        self.last_direction = direction
        dirs = []
        
        if not self.map.check_direction(direction):
            return

        #cur = self.map.find_tile_index(self)
        #if not self.map.tiles[cur - 1].is_wall:
        #    dirs.append("left")
        #if not self.map.tiles[cur + 1].is_wall:
        #    dirs.append("right")
        #if not self.map.tiles[cur - self.map.columns].is_wall:
        #    dirs.append("up")
        #if not self.map.tiles[cur + self.map.columns].is_wall:
        #    dirs.append("down")

        #if not direction in dirs:
        #    return

        if direction == "up":
            if self.speedx == 0:
                self.speedy = -math.fabs(self.speedy)
                self.speedx = 0
            else:
                self.speedy = -math.fabs(self.speedx)
                self.speedx = 0
            self.images = self.images_up

        elif direction == "down":
            if self.speedx == 0:
                self.speedy = math.fabs(self.speedy)
                self.speedx = 0
            else:
                self.speedy = math.fabs(self.speedx)
                self.speedx = 0
            self.images = self.images_down

        elif direction == "left":
            if self.speedx == 0:
                self.speedx = -math.fabs(self.speedy)
                self.speedy = 0
            else:
                self.speedx = -math.fabs(self.speedx)
                self.speedy = 0
            self.images = self.images_left

        elif direction == "right":
            if self.speedx == 0:
                self.speedx = math.fabs(self.speedy)
                self.speedy = 0
            else:
                self.speedx = math.fabs(self.speedx)
                self.speedy = 0
            self.images = self.images_right

        self.move()
        self.direction = direction



