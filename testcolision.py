import pygame

pygame.init()

# Set up game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up camera
camera_pos = [0, 0]

# Set up game objects
square_size = 50
square_color = (255, 0, 0)
squares = []
for i in range(10):
    square_x = i * (square_size + 10)
    square_y = WINDOW_HEIGHT/2 - square_size/2
    square_rect = pygame.Rect(square_x, square_y, square_size, square_size)
    squares.append(square_rect)

# Set up game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Remove the first square and add a new one
                squares.pop(0)
                new_square_x = squares[-1].right + 10
                new_square_y = WINDOW_HEIGHT/2 - square_size/2
                new_square_rect = pygame.Rect(new_square_x, new_square_y, square_size, square_size)
                squares.append(new_square_rect)

    # Update game state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera_pos[0] += 5
    if keys[pygame.K_RIGHT]:
        camera_pos[0] -= 5

    # Update screen
    screen.fill((0, 0, 0))
    for square in squares:
        square_draw_rect = square.move(camera_pos)
        pygame.draw.rect(screen, square_color, square_draw_rect)
    pygame.display.flip()

pygame.quit()
