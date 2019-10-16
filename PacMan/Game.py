import pygame
import sys
import Map
import Packman
import GameObject
import Blinky
import Button
import MapEditor

from Auth import Authorization
from database import Database

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class Game(object):
    
    def __init__(self):
        self.user = Authorization()#меню Авторизации
        self.db = Database("database", "table_of_records")
        self.width = 600
        self.height = 600
        self.map = Map.Map(self)
        self.score = 0
        self.lives = 3
        self.level = 0
        self.buttons = []
        self.map_shift = (100, 0)
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.editor = MapEditor.MapEditor(self)
      
    
    def relogin(self):
        self.user = Authorization()

    def main_menu(self):
        self.buttons = []
        self.screen.fill((0, 0, 0))
        header = Button.Button(150, 100, "Pacman", 100, self.main)
        self.buttons.append(header)
        header.draw(self.screen)
        start_button = Button.Button(100, 300, "start", 60, self.main)
        start_button.draw(self.screen)
        self.buttons.append(start_button)

        editor_button = Button.Button(100, 400, "map editor", 60, self.editor.editor)
        editor_button.draw(self.screen)
        self.buttons.append(editor_button)

        relogin = Button.Button(100, 500, "relogin", 60, self.relogin)
        relogin.draw(self.screen)
        self.buttons.append(relogin)

        pacman = Packman.Packman(80, 250, "right", self.map)
        blinky = Blinky.Blinky(110, 250, "right", self.map)
        pinky = Blinky.Pinky(130, 250, "right", self.map)
        inky = Blinky.Inky(150, 250, "right", self.map)
        clyde = Blinky.Clyde(170, 250, "right", self.map)


        count = 0

        self.clock = pygame.time.Clock()
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:
                        #pygame.quit()
                        raise SystemExit
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        for but in self.buttons:
                            if but.rect.collidepoint(i.pos):
                                but.clicked()
            
            count += 1
            if count >= 360:
                if pacman.direction == "right":
                    pacman.change_direction("left")
                    blinky.change_direction("left")
                    pinky.change_direction("left")
                    inky.change_direction("left")
                    clyde.change_direction("left")
                else:
                    pacman.change_direction("right")
                    blinky.change_direction("right")
                    pinky.change_direction("right")
                    inky.change_direction("right")
                    clyde.change_direction("right")

                blinky.swap_images()
                pinky.swap_images()
                inky.swap_images()
                clyde.swap_images()
                count = 0

            pacman.update()
            blinky.update()
            pinky.update()
            inky.update()
            clyde.update()

            self.screen.fill((0, 0, 0))
            for i in self.buttons:
                i.draw(self.screen)
            
            pacman.draw(self.screen)
            blinky.draw(self.screen)
            pinky.draw(self.screen)
            inky.draw(self.screen)
            clyde.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)


    def main(self):
        WIDTH = 600
        HEIGHT = 600
        TILE_SIZE = 16

        KEY_UP = pygame.K_w
        KEY_DOWN = pygame.K_s
        KEY_LEFT = pygame.K_a
        KEY_RIGHT = pygame.K_d        
        
        self.clock = pygame.time.Clock()
        

        
        self.map = Map.Map(self)
        surface = pygame.Surface((self.map.columns * self.map.tile_size, self.map.rows * self.map.tile_size))
        self.screen.fill((0, 0, 0))
        self.draw_map()
        self.music_pause("audio\\opening_song.ogg")
        buttons = []
        score_button = Button.Button(320, 500, "score", 45, None)
        buttons.append(score_button)
        score = Button.Button(405, 500, str(self.score), 45, None, (210, 202, 7))
        buttons.append(score)
        lives_button = Button.Button(170, 500, "lives", 45, None)
        buttons.append(lives_button)

        live = pygame.image.load("res//pacman-r 4.gif")
        for i in self.buttons:
            i.draw(self.screen)
        for i in range(0, self.lives):
                self.screen.blit(live, (220 + 20 * (i + 1), 510))

        pygame.display.flip()
        pygame.mixer_music.load("audio\\march.mp3")
        pygame.mixer_music.play(-1)
        #
        t1 = 0
        t2 = 0
        rows = self.map.rows
        columns = self.map.columns
        counter = 0
        #
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if i.type == pygame.KEYDOWN:
                    if i.key == KEY_UP:
                        self.map.pacman.change_direction("up")
                    if i.key == KEY_DOWN:
                        self.map.pacman.change_direction("down")
                    if i.key == KEY_LEFT:
                        self.map.pacman.change_direction("left")
                    if i.key == KEY_RIGHT:
                        self.map.pacman.change_direction("right")
            surface.fill((0, 0, 0))
            self.screen.fill((0, 0, 0))
            self.map.update()
            self.map.draw(surface)
            self.screen.blit(surface, self.map_shift)
            for i in range(0, self.lives):
                self.screen.blit(live, (220 + 20 * (i + 1), 510))

            score.set_text(str(self.score))
            for but in buttons:
                but.draw(self.screen)
            #pacman.draw(screen)
            #pacman.update()
        
            pygame.display.flip()
            self.clock.tick(60)

    def remove_live(self):
        self.lives -= 1
        self.music_pause("audio\\die.ogg")
        if self.lives == 0:
            self.db.add_to_table(self.user.name, self.score) #добавление рекорда в базу данных
            self.game_over_menu()

      
    def music_pause(self, filename):
        pygame.mixer_music.pause()
        pygame.mixer.quit
        pygame.mixer.init
        sound = pygame.mixer.Sound(filename)
        sound.play(0)
        #pygame.mixer_music.load(filename)
        #pygame.mixer_music.play(0)
        clock = pygame.time.Clock()
        while pygame.mixer.get_busy():
            clock.tick(2)
        pygame.mixer_music.unpause()

    def game_over_menu(self):
        self.score = 0
        self.buttons = []
        self.screen.fill((0, 0, 0))
        header = Button.Button(150, 50, "high scores", 30, None)
        self.buttons.append(header)
        header.draw(self.screen)
        ok_button = Button.Button(150, 500, "ok", 30, self.main_menu)
        ok_button.draw(self.screen)
        self.buttons.append(ok_button)

        records = self.db.get_dict()
        records.sort(key = lambda el: el["score"], reverse = True)
        i, j = 0, 0
        buttons = []
        images = ["res\\blinky\\ghost-red-r 0.gif", "res\\pinky\\ghost-red-r 0.gif", "res\\inky\\ghost-red-r 0.gif", "res\\clyde\\ghost-red-r 0.gif"]

        while i < 10 and i < len(records):
            buttons.append(Button.ImageButton(20, 90 + i * 40, images[j], None))
            buttons.append(Button.Button(50, 90 + i * 40, records[i]["login"], 30, None))
            buttons.append(Button.Button(450, 90 + i * 40, str(records[i]["score"]), 30, None))
            i += 1
            j = (j + 1) % 4
       
        self.clock = pygame.time.Clock()
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        for but in self.buttons:
                            if but.rect.collidepoint(i.pos):
                                but.clicked()
            
            self.screen.fill((0, 0, 0))
            for i in self.buttons:
                i.draw(self.screen)
            for i in buttons:
                i.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)

    def finish_level_menu(self):
        self.level += 1
        #self.user.cur_db.add_to_table(self.user.name, self.score)
        self.buttons = []
        self.screen.fill((0, 0, 0))
        header = Button.Button(150, 100, "high scores", 50, None)
        self.user.cur_db.print_db() #table_of_records - получает словарь рекордов
        self.buttons.append(header)
        header.draw(self.screen)
        ok_button = Button.Button(150, 500, "next level", 30, self.main)
        ok_button.draw(self.screen)
        self.buttons.append(ok_button)

        records = self.db.get_dict()
        records.sort(key = lambda el: el["score"], reverse = True)
        i, j = 0, 0
        buttons = []
        images = ["res\\blinky\\ghost-red-r 0.gif", "res\\pinky\\ghost-red-r 0.gif", "res\\inky\\ghost-red-r 0.gif", "res\\clyde\\ghost-red-r 0.gif"]

        while i < 10 and i < len(records):
            buttons.append(Button.ImageButton(20, 90 + i * 40, images[j], None))
            buttons.append(Button.Button(50, 90 + i * 40, records[i]["login"], 30, None))
            buttons.append(Button.Button(450, 90 + i * 40, str(records[i]["score"]), 30, None))
            i += 1
            j = (j + 1) % 4

        self.clock = pygame.time.Clock()
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        for but in self.buttons:
                            if but.rect.collidepoint(i.pos):
                                but.clicked()
            
            self.screen.fill((0, 0, 0))
            for i in self.buttons:
                i.draw(self.screen)
            for i in buttons:
                i.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)
    
    def draw_map(self):
        surface = pygame.Surface((self.map.columns * self.map.tile_size, self.map.rows * self.map.tile_size))
        self.map.draw(surface)
        self.screen.blit(surface, self.map_shift)
        pygame.display.flip()


