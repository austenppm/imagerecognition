import pygame
import sys 

# outer radius of the donut
outer_radius = 10

# inner radius of the donut (set to half the outer radius to create a hole in the center)
inner_radius = outer_radius / 2

# center coordinates of the donut
center_x = outer_radius
center_y = outer_radius

# create a list to store the characters that make up the donut
donut = []

# loop through the rows
for i in range(2 * outer_radius + 1):
    row = []
    # loop through the columns
    for j in range(2 * outer_radius + 1):
        # calculate the distance from the center
        distance = ((i - center_y) ** 2 + (j - center_x) ** 2) ** 0.5

        # check if the distance is within the outer radius and outside the inner radius
        if outer_radius >= distance >= inner_radius:
            # calculate the depth of the donut at this position
            depth = int((outer_radius - distance) / 2)
            # use different characters and patterns to represent the depth and texture of the donut at this position
            if depth == 0:
                row.append("*")
            elif depth == 1:
                row.append("o")
            elif depth == 2:
                row.append("O")
            else:
                row.append("#")
        else:
            # add a space
            row.append(" ")
    # add the row to the donut list
    donut.append(row)

# initialize pygame
pygame.init()

# set the window size
window_size = (outer_radius * 2 + 1) * 10

# create the window
screen = pygame.display.set_mode((window_size, window_size))

# set the window title
pygame.display.set_caption("Donut")

# set the font and font size
font = pygame.font.Font(None, 36)

# loop until the user closes the window
while True:
    # loop through the rows of the donut
    for i, row in enumerate(donut):
        # loop through the columns of the donut
        for j, char in enumerate(row):
            # render the character using the font
            text = font.render(char, True, (0, 0, 0))
            # calculate the position of the character on the screen
            x = j * 10
            y = i * 10
            # blit the character onto the screen
            screen.blit(text, (x, y))

    # update the display
    pygame.display.flip()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
