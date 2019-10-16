import Tile
import Main
import Packman
import Blinky
import pygame
import os
import math
import random

class Map(object):
    
    def __init__(self, game):
        self.game_over = False
        self.game = game
        self.tiles = []
        self.tile_size = 16
        self.sound_type = ""
        self.music_tile = None
        f = open("map.txt", 'r')
        cnt = 0
        lines = f.readlines()
        self.rows = len(lines)
        self.columns = len(lines[0])
        
        for line in lines:
            words = line.split()
            self.columns = len(words)
            for word in words:
                x = cnt % self.columns * self.tile_size
                y = cnt // self.columns * self.tile_size
                #print("cnt", cnt, "x", x, "y", y)
                self.tiles.append(Tile.Tile(word, cnt, x, y, self.game, 0))
                cnt += 1

        f = open("food_map.txt", 'r')
        cnt = 0
        self.food_count = 0
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if int(word) != 0:
                    self.food_count += 1
                self.tiles[cnt].set_food(int(word))
                cnt = cnt + 1
        f.close()        

        #init distanse array
        if os.path.exists("shortest_distances.txt"):
            f = open("shortest_distances.txt", 'r')
            lines = f.readlines()
            i = 0
            j = 0
            self.D = []
            for line in lines:
                words = line.split()
                self.D.append([])
                for word in words:
                    self.D[i].append(int(word))
                i += 1
            f.close()  
        else:
            self.D = []
            for i in range(0, self.rows * self.columns):
                self.D.append([])
                for j in range(0, self.rows * self.columns):
                    if i == j:
                        self.D[i].append(0)
                    else:
                        self.D[i].append(-1)
        
            shifts = [-1, +1, - self.columns, self.columns]
            for i in range(0, self.rows * self.columns):
                if not self.tiles[i].is_wall:
                    for shift in shifts:
                        if i + shift < self.columns * self.rows and i + shift > 0 and not self.tiles[i + shift].is_wall:
                            self.D[i][i + shift] = 1
        
            n = self.rows * self.columns
            for k in range(0, n):
                for i in range(0, n):
                    for j in range(0, n):
                        if self.D[i][k] == -1 or self.D[k][j] == -1:
                            b = -1
                        else:
                            b = self.D[i][k] + self.D[k][j]
                        if self.D[i][j] == -1:
                            self.D[i][j] =  b
                        elif b == -1:
                            self.D[i][j] =  self.D[i][j]
                        elif self.D[i][j] >= b:
                            self.D[i][j] = b
        
                        #self.D[i][j] = min(self.D[i][j], mysum(self.D[i][k], self.D[k][j]))             
                print(k)

        
            f = open("shortest_distances.txt", 'w')
            for i in range(0, n):
                for j in range(0, n):
                    f.write(str(self.D[i][j]))
                    if j != n - 1:
                        f.write(" ")
                f.write("\n")
            f.close()     
        
        
        self.pacman = Packman.Packman(240, 368, "left", self)

        self.ghosts = []
        self.blinky = Blinky.Blinky(416, 16, "down", self)
        self.pinky = Blinky.Pinky(16, 16, "down", self)
        self.inky = Blinky.Inky(416, 464, "left", self)
        self.clyde = Blinky.Clyde(16, 464, "right", self)
        self.ghosts.append(self.blinky)
        self.ghosts.append(self.pinky)
        self.ghosts.append(self.inky)
        self.ghosts.append(self.clyde)
        
        self.state = "chase"
        self.counter = 0
        #speed improve
        self.cnt_speed_pacman = 0
        self.cnt_speed_ghosts = 0

    
    def update(self):
        
        if self.state == "fear":
            if self.counter == 540:
                sound = pygame.mixer.Sound("audio\\siren.ogg")
                sound.play(0)
            if self.counter >= 600:
                self.counter = 0
                self.change_state_to_chase()
                for ghost in self.ghosts:
                    ghost.swap_images()
            else:
                self.counter += 1
        
           
        if self.state == "run":
            if self.counter >= 120:
                self.counter = 0
                self.change_state_to_chase()
            else:
                self.counter += 1
 
                
        if self.state == "chase":
            if self.counter >= 1800 + random.randrange(0, 1800, 1):
                self.counter = 0
                self.change_state_to_run()
            else:
                self.counter += 1


        ##########################
        self.cnt_speed_pacman += 1
        if self.cnt_speed_pacman >= 20:
            self.cnt_speed_pacman = 0
            if self.check_direction(self.pacman.last_direction):
                self.pacman.change_direction(self.pacman.last_direction)
        
            if self.check_direction(self.pacman.direction, 2):
                self.pacman.update()
            else:
                tile = self.find_tile_index(self.pacman)
                self.pacman.rect.x = self.tiles[tile].rect.x
                self.pacman.rect.y = self.tiles[tile].rect.y
            next = self.find_tile_index(self.pacman)
        ##########################


        if self.check_direction(self.pacman.last_direction):
            self.pacman.change_direction(self.pacman.last_direction)
        
        if self.check_direction(self.pacman.direction, 2):
            self.pacman.update()
        else:
            tile = self.find_tile_index(self.pacman)
            self.pacman.rect.x = self.tiles[tile].rect.x
            self.pacman.rect.y = self.tiles[tile].rect.y
        next = self.find_tile_index(self.pacman)
        

        ##########################
        self.cnt_speed_ghosts += 1
        if self.cnt_speed_ghosts >= 20 - 2 * self.game.level:
            self.cnt_speed_ghosts = 0
            for ghost in self.ghosts:
                index = self.find_tile_index(ghost)
                near = self.get_near_tiles(index)
                if len(near) > 2:
                    if math.fabs(ghost.rect.x - self.tiles[index].rect.x) <= 2 and math.fabs(ghost.rect.y - self.tiles[index].rect.y) <= 2:
                        ghost.state.make_decision(self, index)
                if self.check_ghost_direction(ghost, ghost.direction, 2):
                    ghost.update()
                else:
                    tile = self.find_tile_index(ghost)
                    ghost.rect.x = self.tiles[tile].rect.x
                    ghost.rect.y = self.tiles[tile].rect.y
                    ghost.state.make_decision(self, tile)
        ##########################

        for ghost in self.ghosts:
            index = self.find_tile_index(ghost)
            near = self.get_near_tiles(index)
            if len(near) > 2:
                if math.fabs(ghost.rect.x - self.tiles[index].rect.x) <= 2 and math.fabs(ghost.rect.y - self.tiles[index].rect.y) <= 2:
                    ghost.state.make_decision(self, index)
            if self.check_ghost_direction(ghost, ghost.direction, 2):
                ghost.update()
            else:
                tile = self.find_tile_index(ghost)
                ghost.rect.x = self.tiles[tile].rect.x
                ghost.rect.y = self.tiles[tile].rect.y
                ghost.state.make_decision(self, tile)
            
                   
        #eating food
        if self.tiles[next].food_type != 0:
            if self.pacman.rect.collidepoint(self.tiles[next].food.x, self.tiles[next].food.y):

                if self.tiles[next].food_type == 2:
                    self.change_state_to_fear()
                    sound = pygame.mixer.Sound("audio\\eatpill.ogg")
                    sound.play(0)
                self.tiles[next].food.eat()
                self.food_count -= 1
                if self.food_count == 0:
                    self.game.finish_level_menu()

        
        #eating pacman or ghosts
        if self.state != "fear":
            for ghost in self.ghosts:
                if self.find_tile_index(self.pacman) == self.find_tile_index(ghost):
                    self.game.remove_live()
                    self.to_start_position()
                    self.game.draw_map()
                    pygame.display.flip()
                    self.game.music_pause("audio\\opening_song.ogg")
        

        
            


   

    def draw(self, screen):
        #x, y = 0, 0
        #for i in range(0, self.rows):
        #    x = 0
        #    for j in range(0, self.columns):
        #        screen.blit(self.tiles[i * self.columns + j].image, (x, y))
        #        x += self.tiles[i].rect.width
        #    y += self.tiles[i].rect.height
        #self.pacman.draw(screen)
        self.surface = screen

        for i in self.tiles:
            i.draw(screen)
        self.blinky.draw(screen)
        self.pinky.draw(screen)
        self.inky.draw(screen)
        self.clyde.draw(screen)
        self.pacman.draw(screen)

    def find_tile_index(self, game_object):
        column = (game_object.rect.x + 4) // self.tile_size
        row = (game_object.rect.y + 4) // self.tile_size
        index = self.columns * row + column
        return index

    def get_next_tiles(self, game_object):
        index = self.find_tile_index(game_object)
        res = []
        if not self.tiles[index - self.columns].is_wall:
            res.append(self.tiles[index - self.columns])
        if not self.tiles[index + 1].is_wall:
            res.append(self.tiles[index + 1])
        if not self.tiles[index + self.columns].is_wall:
            res.append(self.tiles[index + self.columns])
        if not self.tiles[index - 1].is_wall:
            res.append(self.tiles[index - 1])
        return res

    def next_tile_index(self, game_object):
        index = self.find_tile_index(game_object)
        if game_object.direction == "up":
            return index - self.columns
        elif game_object.direction == "down":
            return index + self.columns
        elif game_object.direction == "left":
            return index - 1
        elif game_object.direction == "right":
            return index + 1

    def get_near_tiles(self, index):
        res = []
        if not self.tiles[index - self.columns].is_wall:
            res.append(self.tiles[index - self.columns])
        if not self.tiles[index + 1].is_wall:
            res.append(self.tiles[index + 1])
        if not self.tiles[index + self.columns].is_wall:
            res.append(self.tiles[index + self.columns])
        if not self.tiles[index - 1].is_wall:
            res.append(self.tiles[index - 1])
        return res
        
    def get_near_walls(self, index):
        res = []
        if self.tiles[index - self.columns].is_wall:
            res.append(self.tiles[index - self.columns])
        if self.tiles[index + 1].is_wall:
            res.append(self.tiles[index + 1])
        if self.tiles[index + self.columns].is_wall:
            res.append(self.tiles[index + self.columns])
        if self.tiles[index - 1].is_wall:
            res.append(self.tiles[index - 1])
        
        if self.tiles[index + 1 - self.columns].is_wall:
            res.append(self.tiles[index + 1 - self.columns])
        if self.tiles[index - 1 - self.columns].is_wall:
            res.append(self.tiles[index - 1 - self.columns])
        if self.tiles[index + 1 + self.columns].is_wall:
            res.append(self.tiles[index + 1 + self.columns])
        if self.tiles[index - 1 + self.columns].is_wall:
            res.append(self.tiles[index - 1 + self.columns])
        return res

    def to_start_position(self):
        self.pacman.to_start_position()
        self.blinky.to_start_position()
        self.pinky.to_start_position()
        self.inky.to_start_position()
        self.clyde.to_start_position()

    def check_direction(self, direction, bound = 4):
        row = self.rows
        columns = self.columns
        rect = self.pacman.image.get_rect(topleft = (self.pacman.rect.x, self.pacman.rect.y))
        index = self.find_tile_index(self.pacman)
        walls = self.get_near_walls(index)
        addx = 0
        addy = 0
        if direction == "up":
            addx = 0
            addy = -1
        if direction == "down":
            addx = 0
            addy = 1
        if direction == "left":
            addx = -1
            addy = 0
        if direction == "right":
            addx = 1
            addy = 0

        for wall in walls:
            rect = self.pacman.image.get_rect(topleft = (self.pacman.rect.x, self.pacman.rect.y))
            for i in range(0, bound):
                rect.x += addx
                rect.y += addy
                if wall.rect.colliderect(rect):
                    return False
        return True

    def check_ghost_direction(self, ghost, direction, bound = 4):
        row = self.rows
        columns = self.columns
        rect = ghost.image.get_rect(topleft = (ghost.rect.x, ghost.rect.y))
        index = self.find_tile_index(ghost)
        walls = self.get_near_walls(index)
        addx = 0
        addy = 0
        if direction == "up":
            addx = 0
            addy = -1
        if direction == "down":
            addx = 0
            addy = 1
        if direction == "left":
            addx = -1
            addy = 0
        if direction == "right":
            addx = 1
            addy = 0

        for wall in walls:
            rect = ghost.image.get_rect(topleft = (ghost.rect.x, ghost.rect.y))
            for i in range(0, bound):
                rect.x += addx
                rect.y += addy
                if wall.rect.colliderect(rect):
                    return False
        return True

    def change_state_to_run(self):
        self.counter = 0
        for ghost in self.ghosts:
            if ghost.direction == "up":
                ghost.change_direction("down")
            if ghost.direction == "down":
                ghost.change_direction("up")
            if ghost.direction == "left":
                ghost.change_direction("right")
            if ghost.direction == "right":
                ghost.change_direction("left")
            ghost.state = ghost.state_run
        self.state = "run"
        print("run")

    def change_state_to_chase(self):
        self.counter = 0
        for ghost in self.ghosts:
            ghost.state = ghost.state_chase
        self.state = "chase"
        print("chase")

    def change_state_to_fear(self):
        self.counter = 0
        for ghost in self.ghosts:
            if ghost.direction == "up":
                ghost.change_direction("down")
            if ghost.direction == "down":
                ghost.change_direction("up")
            if ghost.direction == "left":
                ghost.change_direction("right")
            if ghost.direction == "right":
                ghost.change_direction("left")
            ghost.state = ghost.state_fear
            if self.state != "fear":
                ghost.swap_images()
        self.state = "fear"
        print("fear")