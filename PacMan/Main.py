import pygame
import sys
import Map
import Packman
import GameObject
import Blinky
import Game


WIDTH = 800
HEIGHT = 600
TILE_SIZE = 16

KEY_UP = pygame.K_w
KEY_DOWN = pygame.K_s
KEY_LEFT = pygame.K_a
KEY_RIGHT = pygame.K_d

user = None

def main():
    if True:
        game = Game.Game()
        game.main_menu()
    else:
        clock = pygame.time.Clock()
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)

        #pacman = Packman.Packman(16, 16, "right")
        map = Map.Map()
        blinky = Blinky.Blinky(300, 300, "right", map)
        cnt = 0

        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if i.type == pygame.KEYDOWN:
                    if i.key == KEY_UP:
                        map.pacman.change_direction("up")
                    if i.key == KEY_DOWN:
                        map.pacman.change_direction("down")
                    if i.key == KEY_LEFT:
                        map.pacman.change_direction("left")
                    if i.key == KEY_RIGHT:
                        map.pacman.change_direction("right")
            # Calling the 'my_group.update' function calls the 'update' function of all 
            # its member sprites. Calling the 'my_group.draw' function uses the 'image'
            # and 'rect' attributes of its member sprites to draw the sprite.
            screen.fill((0, 0, 50))
            map.update()
            map.draw(screen)
        
            cnt += 1
            if cnt == 25:
                cnt = 0
                if blinky.direction == "left":
                    blinky.change_direction("right")
                else:
                   blinky.change_direction("left")

            blinky.update()
            blinky.draw(screen)
            #pacman.draw(screen)
            #pacman.update()
        
            pygame.display.flip()
            clock.tick(30)

if __name__ == '__main__':
    main()