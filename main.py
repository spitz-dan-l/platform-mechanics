import sys
if sys.version_info[0] != 3:
    print("This project requires Python 3")
    exit()
#
# PYTHON 3+ ONLY BEYOND THIS POINT
#
import pygame
from pygame.locals import ( Color, QUIT, KEYDOWN, K_ESCAPE )
# Default Settings
BG_COLOR = Color(135, 206, 250) #sky blue
MAX_FPS = 60
# Game globals
millis_elapsed = 0
screen = None
clock = None

def update_world():
    """Update function for our world """
    global millis_elapsed
    millis_elapsed += clock.get_time()
    #millis_elapsed is total time elapsed since world bagan


def display_world():
    """Display function for our world """
    screen.fill(BG_COLOR)
    #clear and draw our sprites
    pygame.display.update()


def main():
    """Holds main game loop and setup code """
    global clock, screen
    screen = pygame.display.set_mode((320, 240)) #setup window display
    clock = pygame.time.Clock() #setup clock and fixed timestep
    #TODO: reload our previous physics/settings
    game_is_running = True #begin game loop
    while(game_is_running):
        #input events
        for e in pygame.event.get():
            if e.type == QUIT: game_is_running = False
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE: game_is_running = False
        update_world()
        display_world()
        clock.tick(MAX_FPS) #never run the loop more than MAX_FPS
        pygame.display.set_caption("fps: " + str(clock.get_fps()))
    #TODO: add some save/quit code to resume from our last settings
    quit()



if __name__ == "__main__":
    pygame.init()
    main()
