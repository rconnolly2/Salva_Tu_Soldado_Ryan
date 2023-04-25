import pygame
import math
import sys

# inicializar pygame
pygame.init()

# tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# configurar la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Disparar 365 grados")

# configurar el reloj
clock = pygame.time.Clock()

# posición y velocidad del proyectil
projectile_x = 0
projectile_y = 0
projectile_speed = 10

# función para calcular el ángulo de disparo
def get_angle(x, y):
    dx = x - SCREEN_WIDTH / 2
    dy = y - SCREEN_HEIGHT / 2
    angle = math.atan2(dy, dx)
    return angle

# bucle principal del juego
while True:
    # manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # si se hace clic en el botón del mouse, dispara el proyectil
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = get_angle(mouse_x, mouse_y)
            projectile_x = SCREEN_WIDTH / 2
            projectile_y = SCREEN_HEIGHT / 2
            projectile_dx = projectile_speed * math.cos(angle)
            projectile_dy = projectile_speed * math.sin(angle)

            # imprimir el ángulo en grados en la pantalla
            degrees = math.degrees(angle)
            adjusted_degrees = degrees + 90
            if adjusted_degrees > 360:
                adjusted_degrees -= 360
            print(f"Ángulo: {adjusted_degrees:.2f} grados")

    # mover el proyectil
    try:
        projectile_x += projectile_dx
        projectile_y += projectile_dy
    except NameError:
        pass

    # dibujar la pantalla
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (int(projectile_x), int(projectile_y)), 10)
    pygame.display.update()

    # limitar la velocidad de fotogramas
    clock.tick(60)
