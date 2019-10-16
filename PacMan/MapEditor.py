import pygame
import Game
import Tile
import Button
import Food

class MapEditor(object):
    
    def __init__(self, game, filename = "map.txt", *args, **kwargs):
        self.game = game
      
        
        self.image_buttons = []
        self.buttons = []
        save_button = Button.Button(20, 500, "save", 50, self.save)
        save_button.draw(self.game.screen)
        self.buttons.append(save_button)
        self.back_button = Button.Button(20, 560, "back", 50, None)

        self.tile_size = self.game.map.tile_size
        self.current_type = "empty"
        self.current_food = 0
        self.map_shift = (100, 50)

        self.tiles = []
        f = open(filename, 'r')
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
                self.tiles.append(Tile.Tile(word, cnt, x, y, None))
                cnt += 1

        f = open("food_map.txt", 'r')
        cnt = 0
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                self.tiles[cnt].set_food(int(word))
                cnt = cnt + 1

        self.tile_types = ["wall-x", "empty", "wall-nub", "wall-corner-ll", "wall-corner-lr", "wall-corner-ul", "wall-corner-ur", "wall-end-b", "wall-end-l", "wall-end-r", "wall-end-t", "wall-straight-horiz", "wall-straight-vert", "wall-t-bottom", "wall-t-left", "wall-t-right", "wall-t-top"]
        self.food_types = ["food", "empty", "food-power"]
        y = 20
        x = 20
        for i in self.tile_types:
            self.image_buttons.append(Button.ImageButton(x, y, "res\\" + i + ".gif", None, i, 0))
            x = x + 30
        self.image_buttons.append(Button.ImageButton(x, y, "res\\food.gif", None, "empty", 1))
        x = x + 30
        self.image_buttons.append(Button.ImageButton(x, y, "res\\empty.gif", None, "empty", 0))
        x = x + 30
        self.image_buttons.append(Button.ImageButton(x, y, "res\\food-power.gif", None, "empty", 2))
        x = x + 30
        self.game = game
        self.map = pygame.Surface((self.columns * self.tile_size, self.rows * self.tile_size))
        self.map_rect = self.map.get_rect()
        self.map_rect.x = self.map_shift[0]
        self.map_rect.y = self.map_shift[1]
        #self.tiles = []
        #for i in range(0, self.rows):
           # for j in range(0, self.columns):
               # index = i * self.columns + j
                #self.tiles.append(Tile.Tile("empty", index, j * self.tile_size, i * self.tile_size))

    def editor(self):

        KEY_UP = pygame.K_w
        KEY_DOWN = pygame.K_s
        KEY_LEFT = pygame.K_a
        KEY_RIGHT = pygame.K_d        
        
        self.clock = pygame.time.Clock()
        screen = self.game.screen
        
        screen.fill((0, 0, 0))
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        if self.back_button.rect.collidepoint(i.pos):
                            return
                        for but in self.image_buttons:
                            if but.rect.collidepoint(i.pos):
                                self.current_type = but.info 
                                self.current_food = but.info2
                        for but in self.buttons:
                            if but.rect.collidepoint(i.pos):
                                but.clicked("newMap.txt")
                        if self.map_rect.collidepoint(i.pos):
                            x = i.pos[0] - self.map_shift[0]
                            y = i.pos[1] - self.map_shift[1]
                            row = y // self.tile_size
                            col = x // self.tile_size
                            index = self.columns * row + col
                            tile = Tile.Tile(self.current_type, index, self.tiles[index].rect.x, self.tiles[index].rect.y, self.game, self.current_food)
  
                            self.tiles[index] = tile
            screen.fill((0, 0, 50))
            for i in self.image_buttons:
                i.draw(screen)
            
            self.map.fill((0, 0, 0))
            for i in self.tiles:
                #self.map.blit(i.image, i.rect)
                i.draw(self.map)
            
            screen.blit(self.map, self.map_shift)
            for but in self.buttons:
                but.draw(screen)
            
            self.back_button.draw(screen)

            pygame.display.flip()
            self.clock.tick(30)

    def save(self, filename):
        f = open(filename, "w")
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                f.write(self.tiles[i * self.columns + j].type)
                if j < self.columns - 1:
                    f.write(" ")
            f.write("\n")
        f.close()
        f = open("food_" + filename , "w")
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                f.write(str(self.tiles[i * self.columns + j].food_type))
                if j < self.columns - 1:
                    f.write(" ")
            f.write("\n")
        f.close()

