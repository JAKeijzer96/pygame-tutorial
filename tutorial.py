import pygame as pg
from sys import exit
from random import randint

pg.init() # initialize pg modules. Returns a tuple of (succesful, unsuccesful) initializations

WHITE = (255, 255, 255) # RGB value of the color
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (34, 176, 76)

display_width = 800
display_height = 600

# Initialize game display
program_surface = pg.display.set_mode((display_width,display_height)) # returns a surface object with (w,h) wxh pixels
pg.display.set_caption('Tanks')

clock = pg.time.Clock() # pg clock object used to set fps
fps = 15


smallfont = pg.font.SysFont("comicsansms", 25) # size 25
medfont = pg.font.SysFont("comicsansms", 50) # size 25
largefont = pg.font.SysFont("comicsansms", 80) # size 25

def game_intro():
    intro = True

    while intro:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    intro = False
                if event.key == pg.K_q:
                    pg.quit()
                    exit()
        
        program_surface.fill(WHITE)
        message_to_screen("Welcome to Tanks!", GREEN, -100, "large")
        message_to_screen("The objective is to shoot and destroy", BLACK, -30)
        message_to_screen("the enemy tank before they destroy you.", BLACK)
        message_to_screen("The more enemies destroy, the harder they get.", BLACK, 30)
        message_to_screen("Press C to play, P to pause or Q to quit", BLACK, 180)
        pg.display.update()
        clock.tick(15) # no need for high fps, just dont make the delay on keydown too long

def print_score(score):
    text = smallfont.render(f"Score: {score}", True, BLACK)
    program_surface.blit(text, [0,0])

def pause():
    # Can do one update once paused, then stop updating
    # and only check for event handling
    # this way you can make more of an overlay instead of a new full screen
    paused = True
    message_to_screen("Paused", BLACK, -100, size="large")
    message_to_screen("Press C to continue or Q to quit", BLACK)
    pg.display.update()
    
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    paused = False
                elif event.key == pg.K_q:
                    pg.quit()
                    exit()

        #program_surface.fill(white)

        clock.tick(15) # dont need high fps

def text_objects(text, color, size):
    if size == "small":
        text_surface = smallfont.render(text, True, color) # render message, True (for anti-aliasing), color
    elif size == "med":
        text_surface = medfont.render(text, True, color) # render message, True (for anti-aliasing), color
    elif size == "large":
        text_surface = largefont.render(text, True, color) # render message, True (for anti-aliasing), color
    return text_surface, text_surface.get_rect()

def message_to_screen(msg, color, y_displace=0, size="small"):
    text_surface, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width//2, display_height//2 + y_displace)
    program_surface.blit(text_surface, text_rect) # show screen_text on [coords]

def game_loop():
    program_exit = False
    game_over = False

    score = 0 # score, could use snake_length - base length but base length still not certain

    while not program_exit:
        if game_over: # only paste text once
            #program_surface.fill(white)
            message_to_screen("Game over", RED, y_displace=-50, size="large")
            message_to_screen("Press C to play again or Q to quit", BLACK, 50, size="med")
            pg.display.update()
            
        while game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    program_exit = True
                    game_over = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        program_exit = True
                        game_over = False
                    if event.key == pg.K_c:
                        game_loop()

        for event in pg.event.get(): # gets all events (mouse movenent, key press/release, quit etc)
            if event.type == pg.QUIT:
                program_exit = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    pass
                elif event.key == pg.K_RIGHT:
                    pass
                elif event.key == pg.K_UP:
                    pass
                elif event.key == pg.K_DOWN:
                    pass
                elif event.key == pg.K_p:
                    pause()


        program_surface.fill(WHITE)

        print_score(score)
        pg.display.update() # update the display



        clock.tick(fps) # tick(x) for a game of x frames per second, put this after display.update()

    pg.quit() # uninitialize pygame
    exit() # quit the program

game_intro()
game_loop()