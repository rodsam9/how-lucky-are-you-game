import random
import time
import pygame
from pygame.locals import *
from button import Button

pygame.init()

# Set width for screen window
width = 1000
# Set height for screen window
height = 800

# Font for my text that I'll be using to display score.
main_font = pygame.font.Font('freesansbold.ttf', 20)

# Window display of my game.
gameDisplay = pygame.display.set_mode((width, height))
# Sets a caption for game window.
pygame.display.set_caption("How Lucky Are You?")


# Import crate image and set it to box variable.
box = pygame.transform.scale(pygame.image.load("images\crate.png"), (200,200))

# Import quit button image and set it to button_exit variable.
button_exit = pygame.transform.scale(pygame.image.load("images/exit.png"), (170, 90))

# Import submit button image and set it to button_submit variable.
button_submit = pygame.transform.scale(pygame.image.load("images/submit.png"), (170, 170))

# Import dollar sign image and set it to dollar variable.
dollar = pygame.transform.scale(pygame.image.load("images/dollar_sign.png"), (200,200))

# Import explosion image and set it to explosion variable.
explosion = pygame.transform.scale(pygame.image.load("images/explosion.png"), (200, 200))




# Create my 3x3 box button board.
box1 = Button(50,50, box)
box2 = Button(300,50, box)
box3 = Button(550,50, box)
box4 = Button(50,300, box)
box5 = Button(300,300, box)
box6 = Button(550,300, box)
box7 = Button(50,550, box)
box8 = Button(300,550, box)
box9 = Button(550,550, box)


# This is the quit button.
exit_button = Button(790, 600, button_exit)

# This is my submit button
submit_button = Button(790, 400, button_submit)

# Array for all the boxes in the 3x3 board game.
boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

# This function will draw images or elements on the window.
def draw(gameDisplay):
    # Fills the background to this rgb color.
    gameDisplay.fill((205,226,240))
    # For every box in the array, display on screen.
    for boxs in boxes:
        boxs.draw(gameDisplay)
    # Display the quit button on screen.
    exit_button.draw(gameDisplay)
    # Display the submit button on screen.
    submit_button.draw(gameDisplay)
    # Using fonts to display "score" text and adding RGB color, black.
    points_display = main_font.render(f"Score: {points}", True, (0, 0, 0))
    # This will then display the "score" text on upper right of the screen.
    gameDisplay.blit(points_display, (width - points_display.get_width() - 20, 50))

    # This will create a "temporary points" text.
    temp_points_display = main_font.render(f"Temporary Points: {temp_points}", True, (0, 0, 0))
    # Display "temporary points" text upper right screen under "score" text.
    gameDisplay.blit(temp_points_display, (width - temp_points_display.get_width() - 20, 150))
    # Updates the screen
    pygame.display.update()

# This function will be used to refresh the board back to boxes.
def refresh():
    # Every element in boxes array will be changed back to box image.
    for boxs in boxes:
        boxs.image = box

# This variable will keep track of the temporary points that the player has earned.
temp_points = 0

# This will keep track of the actual score the player has.
points = 100


gameExit = True
while gameExit:
    pygame.time.delay(10)
    # This will allow you to click "x" top right of window to exit game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = False
        # If mouse click, then do the following.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Gets position of where the mouse cursor is at.
            pos = pygame.mouse.get_pos()
            # If quit button is clicked, then exit game.
            if exit_button.clicked(pos):
                gameExit = False
            # Else if the submit button is clicked. 
            elif submit_button.clicked(pos):
                # Call refresh(), which will makes board game back to all boxes.
                refresh()
                # Add temporary points to the actual points.
                points += temp_points
                # Set temp_points back to 0.
                temp_points = 0
            else:
                for boxs in boxes:
                    if boxs.clicked(pos):
                        if boxs.image != box:
                            break
                        else:
                            symbols = (explosion, dollar)
                            random_selection = random.choice(symbols)
                            boxs.image = random_selection
                            draw(gameDisplay)

                            if random_selection == dollar:
                                temp_points += 10
                            else:
                                points -= 10
                                temp_points = 0
                                if points <= 0:
                                    gameExit = False
                                else:
                                    time.sleep(0.5)
                                    refresh()

    draw(gameDisplay)

