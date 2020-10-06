import pygame as pg
from sys import exit
from random import randint

pg.init() # initialize pg modules. Returns a tuple of (succesful, unsuccesful) initializations

WHITE = (255, 255, 255) # RGB value of the color
BLACK = (0, 0, 0)
RED = (200, 0, 0)
LIGHT_RED = (255, 0, 0)
GREEN = (34, 176, 76)
LIGHT_GREEN = (0, 255, 0)
YELLOW = (200, 200, 0)
LIGHT_YELLOW = (255, 255, 0)



display_width = 800
display_height = 600

# Initialize game display
program_surface = pg.display.set_mode((display_width,display_height)) # returns a surface object with (w,h) wxh pixels
pg.display.set_caption('Tanks')

clock = pg.time.Clock() # pg clock object used to set fps
fps = 15


smallfont = pg.font.SysFont("calibri", 25) # size 25
medfont = pg.font.SysFont("comicsansms", 50) # size 25
largefont = pg.font.SysFont("calibri", 80) # size 25

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
        #message_to_screen("Press C to play, P to pause or Q to quit", BLACK, 180)

        button("Play", 150, 500, 100, 50, GREEN, LIGHT_GREEN, game_loop)
        button("Controls", 350, 500, 100, 50, YELLOW, LIGHT_YELLOW, game_controls)
        button("Quit", 550, 500, 100, 50, RED, LIGHT_RED, quit)


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

        clock.tick(15) # dont need high fps

def game_controls():
    game_cont = True
    while game_cont:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        program_surface.fill(WHITE)
        message_to_screen("Controls", BLACK, -100, "large")
        message_to_screen("Fire: Spacebar", BLACK, -30)
        message_to_screen("Move turret: Up and down arrows", BLACK)
        message_to_screen("Move tank: Left and right arrows", BLACK, 30)
        message_to_screen("Pause: P", BLACK, 60)

        button("Play", 150, 500, 100, 50, GREEN, LIGHT_GREEN, game_loop)
        # TODO: make option to return to main menu without infinite loop
        #button("Return", 350, 500, 100, 50, YELLOW, LIGHT_YELLOW, game_intro)
        button("Quit", 550, 500, 100, 50, RED, LIGHT_RED, quit)

        pg.display.update()
        clock.tick(15) # no need for high fps, just dont make the delay on keydown too long

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

def button(text, x, y, width, height, inactive_color, active_color, function):
    # TODO: check for usage of rect.collidepoint with the text rect?
    # https://stackoverflow.com/questions/58717367/how-does-the-collidepoint-function-in-pygame-work

    cur = pg.mouse.get_pos() # (x,y) tuple of mouse location
    click = pg.mouse.get_pressed() # (left, middle, right) tuple of mouse buttons, values are either 1 (down) or 0 (up)

    if x < cur[0] < x+width and y < cur[1] < y+height:
        pg.draw.rect(program_surface, active_color, (x, y, width, height))
        if click[0]:
            function() # call the function passed as parameter
    else:
        pg.draw.rect(program_surface, inactive_color, (x, y, width, height))
    text_to_button(text, BLACK, x, y, width, height)
    
def text_to_button(text, color, x, y, width, height, size="small"):
    text_surface, text_rect = text_objects(text, color, size)
    text_rect.center = ( x + (width//2), y + (height//2) )
    program_surface.blit(text_surface, text_rect)

def game_loop():
    program_exit = False
    game_over = False

    score = 0

    while not program_exit:
        if game_over: # only paste text once
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
        pg.display.update()



        clock.tick(fps) # tick(x) for a game of x frames per second, put this after display.update()

    pg.quit() # uninitialize pygame
    exit() # quit the program

game_intro()