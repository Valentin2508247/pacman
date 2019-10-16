import pygame
import GameObject
import math
import random
from abc import ABCMeta, abstractmethod


class Blinky(GameObject.GameObject):
    """description of class"""

    def __init__(self, x, y, direction, map, *args, **kwargs):
        s = ""
        
        iml = []
        for i in range(0, 7):
            s = "res\\blinky\\ghost-red-l " + str(i)  + ".gif"
            iml.append(pygame.image.load(s))

        imr = []
        for i in range(0, 7):
            s = "res\\blinky\\ghost-red-r " + str(i) + ".gif"
            imr.append(pygame.image.load(s))

        imd = []
        for i in range(0, 7):
            s = "res\\blinky\\ghost-red-d " + str(i)  + ".gif"
            imd.append(pygame.image.load(s))

        imu = []
        for i in range(0, 7):
            s = "res\\blinky\\ghost-red-u " + str(i)  + ".gif"
            imu.append(pygame.image.load(s))

        ###fear
        self.fearl = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-l " + str(i)  + ".gif"
            self.fearl.append(pygame.image.load(s))

        self.fearr = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-r " + str(i) + ".gif"
            self.fearr.append(pygame.image.load(s))

        self.feard = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-d " + str(i)  + ".gif"
            self.feard.append(pygame.image.load(s))

        self.fearu = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-u " + str(i)  + ".gif"
            self.fearu.append(pygame.image.load(s))
        
        ###

        self.direction = direction

        self.state_fear = StateFear(self)
        self.state_chase = StateBlinkyChase(self)
        self.state_run = StateBlinkyRun(self)
        #self.state = self.state_fear
        self.state = self.state_chase
        #self.state = self.state_run
        #self.rect = imu[0].get_rect(topleft = (x, y))
        return super().__init__(x, y, imu, imd, iml, imr, map, *args, **kwargs)

    def update(self):
        self.index += self.next_image
        if self.index == len(self.images) or self.index == -1:
            self.next_image = 0 - self.next_image
            self.index += self.next_image
        
        self.image = self.images[self.index]
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def change_direction(self, direction):
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

        self.direction = direction

    def swap_images(self):
        u = self.images_up
        d = self.images_down
        l = self.images_left
        r = self.images_right
        
        self.images_up = self.fearu
        self.images_down = self.feard
        self.images_left = self.fearl
        self.images_right = self.fearr

        self.feard = d
        self.fearu = u
        self.fearl = l
        self.fearr = r

class Pinky(GameObject.GameObject):
    """description of class"""

    def __init__(self, x, y, direction, map, *args, **kwargs):
        s = ""
        
        iml = []
        for i in range(0, 7):
            s = "res\\pinky\\ghost-red-l " + str(i)  + ".gif"
            iml.append(pygame.image.load(s))

        imr = []
        for i in range(0, 7):
            s = "res\\pinky\\ghost-red-r " + str(i) + ".gif"
            imr.append(pygame.image.load(s))

        imd = []
        for i in range(0, 7):
            s = "res\\pinky\\ghost-red-d " + str(i)  + ".gif"
            imd.append(pygame.image.load(s))

        imu = []
        for i in range(0, 7):
            s = "res\\pinky\\ghost-red-u " + str(i)  + ".gif"
            imu.append(pygame.image.load(s))


        ###fear
        self.fearl = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-l " + str(i)  + ".gif"
            self.fearl.append(pygame.image.load(s))

        self.fearr = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-r " + str(i) + ".gif"
            self.fearr.append(pygame.image.load(s))

        self.feard = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-d " + str(i)  + ".gif"
            self.feard.append(pygame.image.load(s))

        self.fearu = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-u " + str(i)  + ".gif"
            self.fearu.append(pygame.image.load(s))

        ###

        self.direction = direction
        self.state_fear = StateFear(self)
        self.state_chase = StatePinkyChase(self)
        self.state_run = StatePinkyRun(self)
        #self.state = self.state_fear
        self.state = self.state_chase
        #self.state = self.state_run
        #self.rect = imu[0].get_rect(topleft = (x, y))
        return super().__init__(x, y, imu, imd, iml, imr, map, *args, **kwargs)

    def update(self):
        self.index += self.next_image
        if self.index == len(self.images) or self.index == -1:
            self.next_image = 0 - self.next_image
            self.index += self.next_image
        
        self.image = self.images[self.index]
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def change_direction(self, direction):
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

        self.direction = direction

    def swap_images(self):
        u = self.images_up
        d = self.images_down
        l = self.images_left
        r = self.images_right
        
        self.images_up = self.fearu
        self.images_down = self.feard
        self.images_left = self.fearl
        self.images_right = self.fearr

        self.feard = d
        self.fearu = u
        self.fearl = l
        self.fearr = r

class Inky(GameObject.GameObject):
    """description of class"""

    def __init__(self, x, y, direction, map, *args, **kwargs):
        s = ""
        
        iml = []
        for i in range(0, 7):
            s = "res\\inky\\ghost-red-l " + str(i)  + ".gif"
            iml.append(pygame.image.load(s))

        imr = []
        for i in range(0, 7):
            s = "res\\inky\\ghost-red-r " + str(i) + ".gif"
            imr.append(pygame.image.load(s))

        imd = []
        for i in range(0, 7):
            s = "res\\inky\\ghost-red-d " + str(i)  + ".gif"
            imd.append(pygame.image.load(s))

        imu = []
        for i in range(0, 7):
            s = "res\\inky\\ghost-red-u " + str(i)  + ".gif"
            imu.append(pygame.image.load(s))


        ###fear
        self.fearl = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-l " + str(i)  + ".gif"
            self.fearl.append(pygame.image.load(s))

        self.fearr = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-r " + str(i) + ".gif"
            self.fearr.append(pygame.image.load(s))

        self.feard = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-d " + str(i)  + ".gif"
            self.feard.append(pygame.image.load(s))

        self.fearu = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-u " + str(i)  + ".gif"
            self.fearu.append(pygame.image.load(s))
        
        ###

        self.direction = direction
        self.state_fear = StateFear(self)
        self.state_chase = StateInkyChase(self)
        self.state_run = StateInkyRun(self)
        #self.state = self.state_fear
        self.state = self.state_chase
        #self.state = self.state_run
        #self.rect = imu[0].get_rect(topleft = (x, y))
        return super().__init__(x, y, imu, imd, iml, imr, map, *args, **kwargs)

    def update(self):
        self.index += self.next_image
        if self.index == len(self.images) or self.index == -1:
            self.next_image = 0 - self.next_image
            self.index += self.next_image
        
        self.image = self.images[self.index]
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def change_direction(self, direction):
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

        self.direction = direction

    def swap_images(self):
        u = self.images_up
        d = self.images_down
        l = self.images_left
        r = self.images_right
        
        self.images_up = self.fearu
        self.images_down = self.feard
        self.images_left = self.fearl
        self.images_right = self.fearr

        self.feard = d
        self.fearu = u
        self.fearl = l
        self.fearr = r

class Clyde(GameObject.GameObject):
    """description of class"""

    def __init__(self, x, y, direction, map, *args, **kwargs):
        s = ""
        
        iml = []
        for i in range(0, 7):
            s = "res\\clyde\\ghost-red-l " + str(i)  + ".gif"
            iml.append(pygame.image.load(s))

        imr = []
        for i in range(0, 7):
            s = "res\\clyde\\ghost-red-r " + str(i) + ".gif"
            imr.append(pygame.image.load(s))

        imd = []
        for i in range(0, 7):
            s = "res\\clyde\\ghost-red-d " + str(i)  + ".gif"
            imd.append(pygame.image.load(s))

        imu = []
        for i in range(0, 7):
            s = "res\\clyde\\ghost-red-u " + str(i)  + ".gif"
            imu.append(pygame.image.load(s))


        ###fear
        self.fearl = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-l " + str(i)  + ".gif"
            self.fearl.append(pygame.image.load(s))

        self.fearr = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-r " + str(i) + ".gif"
            self.fearr.append(pygame.image.load(s))

        self.feard = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-d " + str(i)  + ".gif"
            self.feard.append(pygame.image.load(s))

        self.fearu = []
        for i in range(0, 7):
            s = "res\\scared\\ghost-red-u " + str(i)  + ".gif"
            self.fearu.append(pygame.image.load(s))
        
        ###

        self.direction = direction
        self.state_fear = StateFear(self)
        self.state_chase = StateClydeChase(self)
        self.state_run = StateClydeRun(self)
        #self.state = self.state_fear
        self.state = self.state_chase
        #self.state = self.state_run
        #self.rect = imu[0].get_rect(topleft = (x, y))
        return super().__init__(x, y, imu, imd, iml, imr, map, *args, **kwargs)

    def update(self):
        self.index += self.next_image
        if self.index == len(self.images) or self.index == -1:
            self.next_image = 0 - self.next_image
            self.index += self.next_image
        
        self.image = self.images[self.index]
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def change_direction(self, direction):
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

        self.direction = direction

    def swap_images(self):
        u = self.images_up
        d = self.images_down
        l = self.images_left
        r = self.images_right
        
        self.images_up = self.fearu
        self.images_down = self.feard
        self.images_left = self.fearl
        self.images_right = self.fearr

        self.feard = d
        self.fearu = u
        self.fearl = l
        self.fearr = r


class State(metaclass=ABCMeta):
    @abstractmethod
    def make_decision(self, _map, tile) -> None:
        pass

class StateFear(State):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        self.last_tile = -1
        return super().__init__(*args, **kwargs)

    def make_decision(self, _map, tile):
        moves = []
        index = _map.find_tile_index(self.owner)
        if index == self.last_tile:
            return
        self.last_tile = index
        if not _map.tiles[tile + 1].is_wall:
            moves.append("right")
        if not _map.tiles[tile - 1].is_wall:
            moves.append("left")
        if not _map.tiles[tile - _map.columns].is_wall:
            moves.append("up")
        if not _map.tiles[tile + _map.columns].is_wall:
            moves.append("down")
        if self.owner.direction == "up":
            if "down" in moves:
                moves.remove("down")
        elif self.owner.direction == "down":
            if "up" in moves:
                moves.remove("up")
        elif self.owner.direction == "left":
            if "right" in moves:
                moves.remove("right")
        elif self.owner.direction == "right":
            if "left" in moves:
                moves.remove("left")
        random.shuffle(moves)
        self.owner.change_direction(moves[0])
        

class StateBlinkyChase(State):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        self.last_tile = -1
        return super().__init__(*args, **kwargs)

    def make_decision(self, _map, tile):
        index = _map.find_tile_index(self.owner)
        if index == self.last_tile:
            return
        aim = self.owner.map.find_tile_index(self.owner.map.pacman)
        pos = self.owner.map.find_tile_index(self.owner)
        D = self.owner.map.D
        left = D[pos - 1][aim]
        right = D[pos + 1][aim]
        direction = self.owner.direction
        up = D[pos - self.owner.map.columns][aim]
        down = D[pos + self.owner.map.columns][aim]
        #print("aim", aim, "pos", pos, "left", left, "right", right, "up", up, "down", down)
        move = [left, right, up, down]
        move = sorted(move)
        for i in range(0, 4):
            if move[i] != -1:
                if move[i] == left:
                    if direction != "right":
                        self.owner.change_direction("left")
                        break;
                if move[i] == right:
                    if direction != "left":
                        self.owner.change_direction("right")
                        break;
                if move[i] == up:
                    if direction != "down":
                        self.owner.change_direction("up")
                        break;
                if move[i] == down:
                    if direction != "up":
                        self.owner.change_direction("down")
                        break;



class StatePinkyChase(State):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        self.last_tile = -1
        return super().__init__(*args, **kwargs)

    def make_decision(self, _map, tile):
        index = _map.find_tile_index(self.owner)
        if index == self.last_tile:
            return
        map = self.owner.map
        aim = self.owner.map.find_tile_index(self.owner.map.pacman)
        row = aim // map.columns
        column = aim % map.columns
        dir_pacman = self.owner.map.pacman.direction
        
        bound = 8
        add = 0
        
        if dir_pacman == "left":
            add = -1
            if column < 8:
                bound = column
        if dir_pacman == "right":
            add = 1
            if column > map.columns - 8 - 1:
                bound = map.columns - column
        if dir_pacman == "down":
            add = map.columns
            if row > map.rows - 8 - 1:
                bound = map.rows - row
        if dir_pacman == "up":
           add = -map.columns
           if row < 8:
                bound = row
        
        temp = aim
        for i in range(0, bound):
            temp += add
            if temp < self.owner.map.columns * self.owner.map.rows and not map.tiles[temp].is_wall:
                aim = temp


        if aim > 0 and aim < self.owner.map.columns * self.owner.map.rows and not self.owner.map.tiles[aim].is_wall:
            pos = self.owner.map.find_tile_index(self.owner)
            D = self.owner.map.D
            left = D[pos - 1][aim]
            right = D[pos + 1][aim]
            direction = self.owner.direction
            up = D[pos - self.owner.map.columns][aim]
            down = D[pos + self.owner.map.columns][aim]
            #print("aim", aim, "pos", pos, "left", left, "right", right, "up", up, "down", down)
            move = [left, right, up, down]
            move = sorted(move)
            for i in range(0, 4):
                if move[i] != -1:
                    if move[i] == left:
                        if direction != "right":
                            self.owner.change_direction("left")
                            break;
                    if move[i] == right:
                        if direction != "left":
                            self.owner.change_direction("right")
                            break;
                    if move[i] == up:
                        if direction != "down":
                            self.owner.change_direction("up")
                            break;
                    if move[i] == down:
                        if direction != "up":
                            self.owner.change_direction("down")
                            break;
        else:
            self.owner.state_fear.make_decision(_map, tile)

class StateInkyChase(State):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        self.last_tile = -1
        return super().__init__(*args, **kwargs)

    def make_decision(self, _map, tile):
        index = _map.find_tile_index(self.owner)
        if index == self.last_tile:
            return
        map = self.owner.map
        aim = self.owner.map.find_tile_index(self.owner.map.pacman)
        row = aim // map.columns
        column = aim % map.columns
        dir_pacman = self.owner.map.pacman.direction
        
        bound = 8
        add = 0
        
        if dir_pacman == "left":
            add = 1
            if column > map.columns - 8 - 1:
                bound = map.columns - column
        if dir_pacman == "right":
            add = -1
            if column < 8:
                bound = column
        if dir_pacman == "up":
            add = map.columns
            if row > map.rows - 8 - 1:
                bound = map.rows - row
        if dir_pacman == "down":
           add = -map.columns
           if row < 8:
                bound = row
        
        temp = aim
        for i in range(0, bound):
            temp += add
            if temp < self.owner.map.columns * self.owner.map.rows and not map.tiles[temp].is_wall:
                aim = temp


        if aim > 0 and aim < self.owner.map.columns * self.owner.map.rows and not self.owner.map.tiles[aim].is_wall:
            pos = self.owner.map.find_tile_index(self.owner)
            D = self.owner.map.D
            left = D[pos - 1][aim]
            right = D[pos + 1][aim]
            direction = self.owner.direction
            up = D[pos - self.owner.map.columns][aim]
            down = D[pos + self.owner.map.columns][aim]
            #print("aim", aim, "pos", pos, "left", left, "right", right, "up", up, "down", down)
            move = [left, right, up, down]
            move = sorted(move)
            for i in range(0, 4):
                if move[i] != -1:
                    if move[i] == left:
                        if direction != "right":
                            self.owner.change_direction("left")
                            break;
                    if move[i] == right:
                        if direction != "left":
                            self.owner.change_direction("right")
                            break;
                    if move[i] == up:
                        if direction != "down":
                            self.owner.change_direction("up")
                            break;
                    if move[i] == down:
                        if direction != "up":
                            self.owner.change_direction("down")
                            break;
        else:
            self.owner.state_fear.make_decision(_map, tile)


class StateClydeChase(State):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        self.last_tile = -1
        return super().__init__(*args, **kwargs)

    def make_decision(self, _map, tile):
        index = _map.find_tile_index(self.owner)
        if index == self.last_tile:
            return
        aim = self.owner.map.find_tile_index(self.owner.map.pacman)
        pos = self.owner.map.find_tile_index(self.owner)
       
        D = self.owner.map.D

        if D[pos][aim] <  8:
            aim = 871
        left = D[pos - 1][aim]
        right = D[pos + 1][aim]
        direction = self.owner.direction
        up = D[pos - self.owner.map.columns][aim]
        down = D[pos + self.owner.map.columns][aim]
        #print("aim", aim, "pos", pos, "left", left, "right", right, "up", up, "down", down)
        move = [left, right, up, down]
        move = sorted(move)
        for i in range(0, 4):
            if move[i] != -1:
                if move[i] == left:
                    if direction != "right":
                        self.owner.change_direction("left")
                        break;
                if move[i] == right:
                    if direction != "left":
                        self.owner.change_direction("right")
                        break;
                if move[i] == up:
                    if direction != "down":
                        self.owner.change_direction("up")
                        break;
                if move[i] == down:
                    if direction != "up":
                        self.owner.change_direction("down")
                        break;


#remade
class StateBlinkyRun(State):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        self.last_tile = -1
        return super().__init__(*args, **kwargs)

    def make_decision(self, _map, tile):
        #print("make decidion")
        index = _map.find_tile_index(self.owner)
        if index == self.last_tile:
            return
        aim = 56
        pos = self.owner.map.find_tile_index(self.owner)
        D = self.owner.map.D
        left = D[pos - 1][aim]
        right = D[pos + 1][aim]
        direction = self.owner.direction
        up = D[pos - self.owner.map.columns][aim]
        down = D[pos + self.owner.map.columns][aim]
        #print("aim", aim, "pos", pos, "left", left, "right", right, "up", up, "down", down)
        move = [left, right, up, down]
        move = sorted(move)
        for i in range(0, 4):
            if move[i] != -1:
                if move[i] == left:
                    if direction != "right":
                        self.owner.change_direction("left")
                        break;
                if move[i] == right:
                    if direction != "left":
                        self.owner.change_direction("right")
                        break;
                if move[i] == up:
                    if direction != "down":
                        self.owner.change_direction("up")
                        break;
                if move[i] == down:
                    if direction != "up":
                        self.owner.change_direction("down")
                        break;

class StatePinkyRun(State):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        self.last_tile = -1
        return super().__init__(*args, **kwargs)

    def make_decision(self, _map, tile):
        #print("make decidion")
        index = _map.find_tile_index(self.owner)
        if index == self.last_tile:
            return
        aim = 31
        pos = self.owner.map.find_tile_index(self.owner)
        D = self.owner.map.D
        left = D[pos - 1][aim]
        right = D[pos + 1][aim]
        direction = self.owner.direction
        up = D[pos - self.owner.map.columns][aim]
        down = D[pos + self.owner.map.columns][aim]
        #print("aim", aim, "pos", pos, "left", left, "right", right, "up", up, "down", down)
        move = [left, right, up, down]
        move = sorted(move)
        for i in range(0, 4):
            if move[i] != -1:
                if move[i] == left:
                    if direction != "right":
                        self.owner.change_direction("left")
                        break;
                if move[i] == right:
                    if direction != "left":
                        self.owner.change_direction("right")
                        break;
                if move[i] == up:
                    if direction != "down":
                        self.owner.change_direction("up")
                        break;
                if move[i] == down:
                    if direction != "up":
                        self.owner.change_direction("down")
                        break;

class StateInkyRun(State):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        self.last_tile = -1
        return super().__init__(*args, **kwargs)

    def make_decision(self, _map, tile):
        #print("make decidion")
        index = _map.find_tile_index(self.owner)
        if index == self.last_tile:
            return
        aim = 896
        pos = self.owner.map.find_tile_index(self.owner)
        D = self.owner.map.D
        left = D[pos - 1][aim]
        right = D[pos + 1][aim]
        direction = self.owner.direction
        up = D[pos - self.owner.map.columns][aim]
        down = D[pos + self.owner.map.columns][aim]
        #print("aim", aim, "pos", pos, "left", left, "right", right, "up", up, "down", down)
        move = [left, right, up, down]
        move = sorted(move)
        for i in range(0, 4):
            if move[i] != -1:
                if move[i] == left:
                    if direction != "right":
                        self.owner.change_direction("left")
                        break;
                if move[i] == right:
                    if direction != "left":
                        self.owner.change_direction("right")
                        break;
                if move[i] == up:
                    if direction != "down":
                        self.owner.change_direction("up")
                        break;
                if move[i] == down:
                    if direction != "up":
                        self.owner.change_direction("down")
                        break;

class StateClydeRun(State):
    def __init__(self, owner, *args, **kwargs):
        self.owner = owner
        self.last_tile = -1
        return super().__init__(*args, **kwargs)

    def make_decision(self, _map, tile):
        #print("make decidion")
        index = _map.find_tile_index(self.owner)
        if index == self.last_tile:
            return
        aim = 871
        pos = self.owner.map.find_tile_index(self.owner)
        D = self.owner.map.D
        left = D[pos - 1][aim]
        right = D[pos + 1][aim]
        direction = self.owner.direction
        up = D[pos - self.owner.map.columns][aim]
        down = D[pos + self.owner.map.columns][aim]
        #print("aim", aim, "pos", pos, "left", left, "right", right, "up", up, "down", down)
        move = [left, right, up, down]
        move = sorted(move)
        for i in range(0, 4):
            if move[i] != -1:
                if move[i] == left:
                    if direction != "right":
                        self.owner.change_direction("left")
                        break;
                if move[i] == right:
                    if direction != "left":
                        self.owner.change_direction("right")
                        break;
                if move[i] == up:
                    if direction != "down":
                        self.owner.change_direction("up")
                        break;
                if move[i] == down:
                    if direction != "up":
                        self.owner.change_direction("down")
                        break;
