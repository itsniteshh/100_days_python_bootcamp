import pygame
from pygame.locals import *

game_running = True

#Step 1-  simple pygame window with some bg
if __name__ == "__main__":
    pygame.init() # initializes the whole module
    
    surface = pygame.display.set_mode((500, 500))
    surface.fill("white")
    pygame.display.flip()
    
    while game_running:
        #Step - 2 FOR quitting the game
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_running = False
                    
            elif event.type == QUIT:
                game_running = False
                
        
    