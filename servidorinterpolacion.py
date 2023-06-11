import socket
import time

# Initialize socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 5000))

# Initialize player position and velocity
player_pos = [0, 0]
player_vel = [0, 0]

# Start game loop
while True:
    # Update player position and velocity
    player_vel[0] += 0.5  # simulate acceleration
    player_vel[1] += 0.5
    player_pos[0] += player_vel[0]
    player_pos[1] += player_vel[1]

    # Send player position and velocity to client
    data = f"{player_pos[0]},{player_pos[1]},{player_vel[0]},{player_vel[1]}"
    server_socket.sendto(data.encode(), ('localhost', 5001))

    # Wait for 2 seconds before sending next update
    time.sleep(0.5)
