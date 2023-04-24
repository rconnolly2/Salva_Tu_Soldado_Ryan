import pygame

pygame.init()

# set up the display window
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# load a custom font
font_path = "MinimalPixelFont.ttf"
font_size = 150
font = pygame.font.Font(font_path, font_size)

# create a text surface using the custom font
text = "Hello, Pygame!"
text_surface = font.render(text, True, (255, 255, 255))

# get the rectangle for the text surface
text_rect = text_surface.get_rect()

# center the text on the screen
text_rect.center = (screen_width // 2, screen_height // 2)

# draw the text onto the screen
screen.blit(text_surface, text_rect)

# update the display
pygame.display.flip()

# wait for the user to quit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

