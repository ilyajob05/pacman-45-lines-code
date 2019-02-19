# - * - coding: utf-8 - * -

# library loading
import pygame

# library initialization
pygame.init ()

# setting the screen size
sizeScr = (800, 600)
screen = pygame.display.set_mode (sizeScr)

# title for window
pygame.display.set_caption ('Pacman')
 
# timer creation
clock = pygame.time.Clock ()

# image loading for pacman
privedenie = pygame.image.load ('./ pac1.png')
# resize -> 100x100 pixels
privedenie = pygame.transform.scale (privedenie, (100,100))

# loading image for cast
pacMan = pygame.image.load ('./ pac2.png')
# resize -> 100x100 pixels
pacMan = pygame.transform.scale (pacMan, (100,100))

# coordinates of pacman
pacX = 0
pacY = 0

# cast coordinates
privedenieX = 400
privedenieY = 400

# flag to exit the program (necessary for the correct closure of the program)
runApp = true
 
# -------- program loop -----------
# execute while runApp is True
while runApp:
    # --- reading the list of events
    for event in pygame.event.get ():
        # if there is a QUIT event in the list, then close the program
        if event.type == pygame.QUIT:
            runApp = False
 
    # reading key pressed
    keyP = pygame.key.get_pressed ()
    # if left key is pressed
    if keyP [pygame.K_LEFT]:
        # reduce x coordinate
        pacX = pacX - 3
    if keyP [pygame.K_RIGHT]:
        pacManPovernutii = pygame.transform.rotate (pacMan, 0)
        # increase x coordinate
        pacX = pacX + 3
    if keyP [pygame.K_UP]:
        pacManPovernutii = pygame.transform.rotate (pacMan, 90)
        pacY = pacY - 3
    if keyP [pygame.K_DOWN]:
        pacManPovernutii = pygame.transform.rotate (pacMan, 270)
        pacY = pacY + 3
 
    # --- logic of Ira
    # if pacman falls into cast coordinates +/- 50 pixels in X and then in Y
    if (pacX> privedenieX - 50) & (pacX <privedenieX + 50) & (privedenieX == 400):
        if (pacY> privedenieY - 50) & (pacY <privedenieY + 50):
            # transfer the cast to coordinates (0, 0)
            privedenieX = 0
            privedenieY = 0
    elif (pacX> privedenieX - 50) & (pacX <privedenieX + 50) & (privedenieX! = 400):
        if (pacY> privedenieY - 50) & (pacY <privedenieY + 50):
            # add 50 pixels to cast coordinates
            privedenieX + = 50
            privedenieY + = 50
       
 
    # --- Screen redraw
    # Here we draw the background
    screen.fill ((200,200,200))
 
    # Here we draw objects
    screen.blit (privedenie, (privedenieX, privedenieY))
    screen.blit (pacMan, (pacX, pacY))
    
    # --- Update screen
    pygame.display.flip ()
 
    # --- Waiting for 60 timer ticks
    clock.tick (60)
 
# exit from the program
pygame.quit ()
