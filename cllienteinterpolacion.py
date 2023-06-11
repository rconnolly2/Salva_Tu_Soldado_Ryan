import pygame
import socket
import pickle

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Client")

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.SysFont(None, 30)

# Set up the socket
host = 'localhost'
port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Initialize player position and velocity
player_pos = [screen_width // 2, screen_height // 2]
player_vel = [0, 0]

# Initialize interpolation variables
prev_player_pos = player_pos[:]
curr_player_pos = player_pos[:]
interpolation_alpha = 0.0

# Initialize prediction variables
predicted_pos = player_pos[:]
last_update_time = pygame.time.get_ticks()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel[0] -= 5
            elif event.key == pygame.K_RIGHT:
                player_vel[0] += 5
            elif event.key == pygame.K_UP:
                player_vel[1] -= 5
            elif event.key == pygame.K_DOWN:
                player_vel[1] += 5

    # Send player velocity to server
    client_socket.sendall(pickle.dumps(player_vel))
    dt = clock.tick(60) / 1000.0 
    # Receive updates from server
    data = client_socket.recv(1024)
    if data:
        # Unpack the received data
        server_pos, server_vel = pickle.loads(data)

        # Update the player position and velocity
        player_pos = server_pos[:]
        player_vel = server_vel[:]

        # Update interpolation variables
        prev_player_pos = curr_player_pos[:]
        curr_player_pos = player_pos[:]
        interpolation_alpha = 0.0

        # Update prediction variables
        predicted_pos = player_pos[:]
        last_update_time = pygame.time.get_ticks()

    else:
        # If no data is received, use dead reckoning to predict player position
        current_time = pygame.time.get_ticks()
        delta_time = current_time - last_update_time
        predicted_pos[0] += player_vel[0] * delta_time / 1000.0
        predicted_pos[1] += player_vel[1] * delta_time / 1000.0

    # Update player position using dead reckoning
    current_time = pygame.time.get_ticks()
    delta_time = current_time - last_update_time
    player_pos[0] += player_vel[0] * delta_time / 1000.0
    player_pos[1] += player_vel[1] * delta_time / 1000.0

    # Interpolate player position between updates
    interpolation_alpha += delta_time / 1000.0
    if interpolation_alpha > 1.0:
        interpolation_alpha = 1.0
    player_pos[0] = prev_player_pos[0] * (1.0 - interpolation_alpha) + curr_player_pos[0] * interpolation_alpha
    player_pos[1] += player_vel[1] * dt
    # Fill the background
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.circle(screen, BLACK, [int(player_pos[0]), int(player_pos[1])], 10)

    # Draw the predicted player position
    pygame.draw.circle(screen, RED, [int(predicted_pos[0]), int(predicted_pos[1])], 5)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)


