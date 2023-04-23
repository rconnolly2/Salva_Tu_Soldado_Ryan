import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Collision Detection")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the first square
square1_size = 50
square1_x, square1_y = 100, 100
square1_vel = 5

# Set up the second square
square2_size = 50
square2_x, square2_y = 300, 300

# Define the collision detection function
def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x1 < x2 + w2 and x1 + w1 > x2 and
        y1 < y2 + h2 and y1 + h1 > y2):
        return True
    else:
        return False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the first square with the mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    square1_x, square1_y = mouse_x, mouse_y
    
    # Check for collision
    if check_collision(square1_x, square1_y, square1_size, square1_size,
                        square2_x, square2_y, square2_size, square2_size):
        square2_color = RED
    else:
        square2_color = WHITE
    
    # Draw the squares
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (square1_x, square1_y, square1_size, square1_size))
    pygame.draw.rect(screen, square2_color, (square2_x, square2_y, square2_size, square2_size))
    
    # Update the display
    pygame.display.update()
    
    # Limit the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()
