import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the player square
player_size = 50
player_pos = [screen_width/2, screen_height/2]

# Define the bullet square
bullet_size = 10
bullet_pos = [0, 0]
bullet_speed = 10
bullet_state = False
bullet_angle = 0

# Define the enemy square
enemy_size = 50
enemy_pos = [random.randint(0, screen_width-enemy_size), random.randint(0, screen_height-enemy_size)]

# Define game variables
clock = pygame.time.Clock()
fps = 60

# Move the player square
def move_player(keys_pressed):
    global player_pos
    
    if keys_pressed[pygame.K_w] and player_pos[1] > 0:
        player_pos[1] -= 5
    if keys_pressed[pygame.K_s] and player_pos[1] < screen_height - player_size:
        player_pos[1] += 5
    if keys_pressed[pygame.K_a] and player_pos[0] > 0:
        player_pos[0] -= 5
    if keys_pressed[pygame.K_d] and player_pos[0] < screen_width - player_size:
        player_pos[0] += 5

# Fire a bullet
def fire_bullet():
    global bullet_state, bullet_pos, bullet_angle
    
    if not bullet_state:
        bullet_pos = [player_pos[0] + player_size/2 - bullet_size/2, player_pos[1] + player_size/2 - bullet_size/2]
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - player_pos[0]
        dy = mouse_pos[1] - player_pos[1]
        bullet_angle = math.degrees(math.atan2(-dy, dx))
        bullet_state = True

# Check if the bullet hit the enemy
def is_collision():
    global bullet_pos, enemy_pos
    
    if bullet_pos[1] <= enemy_pos[1] + enemy_size and bullet_pos[1] >= enemy_pos[1]:
        if bullet_pos[0] >= enemy_pos[0] and bullet_pos[0] <= enemy_pos[0] + enemy_size:
            return True
    return False

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullet()
    
    # Move the player square
    keys_pressed = pygame.key.get_pressed()
    move_player(keys_pressed)
    
    # Move the bullet square
    if bullet_state:
        bullet_speed_x = bullet_speed * math.cos(math.radians(bullet_angle))
        bullet_speed_y = -bullet_speed * math.sin(math.radians(bullet_angle))
        bullet_pos[0] += bullet_speed_x
        bullet_pos[1] += bullet_speed_y
        if bullet_pos[1] < 0 or bullet_pos[1] > screen_height or bullet_pos[0] < 0 or bullet_pos[0] > screen_width:
            bullet_state = False
