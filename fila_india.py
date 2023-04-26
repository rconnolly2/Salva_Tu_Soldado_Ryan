import pygame
import random

# Define el tamaño de la pantalla y la velocidad de fotogramas
ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 1000
FPS = 60

# Inicializa Pygame
pygame.init()

# Crea la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Ejemplo Pygame")

# Crea los cuadrados
posicion_cuadrado1 = [random.randint(0, ANCHO_PANTALLA), random.randint(0, ALTO_PANTALLA)]
posicion_cuadrado2 = [random.randint(0, ANCHO_PANTALLA), random.randint(0, ALTO_PANTALLA)] # azul
tamanio_cuadrado = 10

#Lista cuadrados azules:
lista_cuadrado_azul = [posicion_cuadrado2]
for i in range(5):
    lista_cuadrado_azul.append([random.randint(0, ANCHO_PANTALLA), random.randint(0, ALTO_PANTALLA)])

def MoverRojoMouse():
    # Obtiene la posición actual del mouse
    posicion_mouse = pygame.mouse.get_pos()
    x, y = posicion_mouse
    posicion_cuadrado1[0], posicion_cuadrado1[1] = x, y

# Define la función para mover el segundo cuadrado
def mover_cuadrado(posicion_cuadrado1, posicion_cuadrado2, espacio_mantener=30, velocidad=5):
    dx = posicion_cuadrado1[0] - posicion_cuadrado2[0]
    dy = posicion_cuadrado1[1] - posicion_cuadrado2[1]
    distancia = ((dx ** 2) + (dy ** 2)) ** 0.5
    if distancia > espacio_mantener:
        posicion_cuadrado2[0] += dx * velocidad / distancia
        posicion_cuadrado2[1] += dy * velocidad / distancia


# Define el bucle principal del juego
jugando = True
reloj = pygame.time.Clock()

while jugando:
    # Maneja los eventos de Pygame
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                print("Key 1 pressed")
                del lista_cuadrado_azul[0]
            if evento.key == pygame.K_3:
                print("Key 3 pressed")
                del lista_cuadrado_azul[3]
            if evento.key == pygame.K_5:
                print("nuevos cuadrados azules")
                lista_cuadrado_azul.append([random.randint(0, ANCHO_PANTALLA), random.randint(0, ALTO_PANTALLA)])
    #Mover cuadrado rojo:
    MoverRojoMouse()

    # Mueve el segundo cuadrado
    x, y = posicion_cuadrado1
    posicion_alterada = x, y
    mover_cuadrado(posicion_alterada, lista_cuadrado_azul[0], 100, 5)

    #Ahora los otros 5 cuadrados se seguiran al anterior el primero seria lista_cuadrado_azul[0]

    for a in range(1, len(lista_cuadrado_azul)):
        mover_cuadrado(lista_cuadrado_azul[a-1], lista_cuadrado_azul[a], 100, 5)

    # Dibuja los cuadrados en la pantalla
    pantalla.fill((255, 255, 255))

    #ahora pintar :)
    for b in range(1, len(lista_cuadrado_azul)):
        pygame.draw.rect(pantalla, (0, 0, 255), (lista_cuadrado_azul[b][0], lista_cuadrado_azul[b][1], tamanio_cuadrado, tamanio_cuadrado))

    
    pygame.draw.rect(pantalla, (255, 0, 0), (posicion_cuadrado1[0], posicion_cuadrado1[1], tamanio_cuadrado, tamanio_cuadrado))
    pygame.draw.rect(pantalla, (0, 0, 255), (posicion_cuadrado2[0], posicion_cuadrado2[1], tamanio_cuadrado, tamanio_cuadrado))
    pygame.display.flip()

    # Limita la velocidad de fotogramas del juego
    reloj.tick(FPS)

# Cierra Pygame
pygame.quit()
