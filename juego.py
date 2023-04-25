import pygame
import math
import sys
from random import randint

class Juego:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        # Set up window dimensions
        self.altura_ventana = 600
        self.ancho_ventana = 800

        self.tecla_pulsada = False

        # Cantidad de zoom
        self.cantidad_zoom = 1
        self.zoom_cambiado = False
        
        #Cargo Fuente:
        self.ruta_fuente = "MinimalPixelFont.ttf"

        # Menu local jugando:
        self.imagen_mapa = pygame.image.load("mapa.png")
        self.pos_imagen_mapa = (10, 500)
        self.dimensiones_imagen_mapa = (self.imagen_mapa.get_width(), self.imagen_mapa.get_height())

        #Barra inferior
        self.imagen_barra = pygame.image.load("barra_editar.png")
        self.pos_imagen_barra = (172, 505)
        self.dimensiones_imagen_barra = (self.imagen_barra.get_width(), self.imagen_barra.get_height())
        self.tecla_1_pulsado = False

        #Marcador
        self.imagen_marcador = pygame.image.load("marcador.png")
        self.pos_imagen_marcador = (667, 11)
        self.dimensiones_imagen_marcador = (self.imagen_marcador.get_width(), self.imagen_marcador.get_height())

        #Cantidad Recursos
        self.fuente_recursos = pygame.font.Font(self.ruta_fuente, 50)
        self.petroleo_jugador = 0
        self.imagen_gota_petroleo = pygame.image.load("gota_petroleo.png")
        self.gota_petroleo_pos = (9, 44)
        self.imagen_bala_icono = pygame.image.load("bala_icono.png")
        self.balas_jugador = 0
        self.bala_icono_pos = (9, 120)

        # Tamaño real de mapa:
        self.mapa_ancho = 6400
        self.mapa_alto = 6400
        self.tamaño_tile = 200
        self.mapa = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

        # Mis listas de decoracion ("esto lo tendra que cargar el server"):
        self.lista_arboles = []
        for i in range(200):
            self.lista_arboles.append([randint(0, self.mapa_ancho), randint(0, self.mapa_alto), "arbol"])

        self.lista_yacimiento_petroleo = []
        self.lista_yacimiento_petroleo.append([200, 200, "petroleo"])
        self.lista_yacimiento_petroleo.append([200, 6000, "petroleo"])
        for i in range(30):
            self.lista_yacimiento_petroleo.append([randint(0, self.mapa_ancho), randint(0, self.mapa_alto), "petroleo"])

        self.lista_balas_iconos = []
        for a in range(200):
            self.lista_balas_iconos.append([randint(0, self.mapa_ancho), randint(0, self.mapa_alto), "bala"])

        # Cargo imagenes:
        self.tile_cesped = pygame.image.load("cesped200.png")
        self.arbol1 = pygame.image.load("arbol1.png")
        self.yacimiento_petroleo = pygame.image.load("yacimiento_petroleo.png")
        self.yacimiento_petroleo_arreglado = pygame.image.load("yacimiento_petroleo_arreglado.png")
        self.yacimiento_petroleo_arreglado_colocando = pygame.image.load("yacimiento_petroleo_arreglado_colocando.png")
        self.imagen_barra_vida = pygame.image.load("barravida.png")
        self.imagen_yacimiento_jugador = pygame.image.load("yacimiento_petroleo_arreglado.png")

        self.screen = pygame.display.set_mode((self.ancho_ventana, self.altura_ventana))
        pygame.display.set_caption("Salva a tu soldado Ryan")

        

        # Configuramos la posición inicial de la cámara
        self.camera_x = 0
        self.camera_y = 0

        # Configuramos la velocidad de la cámara
        self.camera_speed = 4

        # Configuramos el reloj para controlar la tasa de fotogramas
        self.clock = pygame.time.Clock()

        # Datos de mouse:
        self.angulo = 0
        self.mouse_x = 0
        self.mouse_y = 0

        self.move_to(50, 50, 200, 200)

    def move_to(self, x1, y1, x2, y2):
    # Calculate the distance to move in the x-axis direction
        cantidad_abajo = 0
        cantidad_derecha = 0
        if x2 < x1:
            dx = abs(x1 - x2)
            print(f"Moving left by {dx} units.")
        elif x2 > x1:
            dx = abs(x2 - x1)
            print(f"Moving right by {dx} units.")
        else:
            print("Not moving in the x-axis direction.")
            dx = 0
        
        # Calculate the distance to move in the y-axis direction
        if y2 > y1:
            dy = abs(y1 - y2)
            print(f"Moving down by {dy} units.")
        elif y2 < y1:
            dy = abs(y2 - y1)
            print(f"Moving up by {dy} units.")
        else:
            print("Not moving in the y-axis direction.")
            dy = 0
    
        # Actually move to the destination position
        # (replace this with your own code that does the actual movement)
        return cantidad_derecha, cantidad_abajo
        

            

    def Distancia2Puntos(self, x1, y1, x2, y2):
        distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return distancia
    
    def Angulo2Puntos(self, x1, y1, x2, y2, radian=False):
        # Calcular diferencias en las coordenadas x e y
        delta_x = x1 - x2
        delta_y = y1 - y2

        # Calcular ángulo en radianes
        angulo = math.atan2(delta_y, delta_x)*-1
        if radian == True:
            return angulo
        else:
            return math.degrees(angulo)
        
    def Colision2DCajas(self, x1, y1, w1, h1, x2, y2, w2, h2):
        if (x1 < x2 + w2 and x1 + w1 > x2 and
            y1 < y2 + h2 and y1 + h1 > y2):
            return True
        else:
            return False

    
    def zoom_teclado(self):
        '''
        Esta Funcion mira si se da a las teclas: q y e si se da
        Se añadira y restara zoom a => cantidad_zoom
        '''
            
        # Obtenemos el estado de todas las teclas
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.cantidad_zoom = round(self.cantidad_zoom + 0.1, 2)
            self.zoom_cambiado = True
        if keys[pygame.K_e]:
            # Si el zoom no es menor a 0.1 se puede hacer menos zoom
            self.cantidad_zoom = round(max(0.8, self.cantidad_zoom - 0.1), 2)
            self.zoom_cambiado = True
    

    def Cargar_Mapa(self, lista_mapa, surface_pintar, posicioncamara_x, posicioncamara_y):
        # Cargamos la imagen de fondo por cada tile de nuestra lista de izquierda a derecha 
        # y arriba a abajo
        tile_cesped_escalado = pygame.transform.scale(self.tile_cesped, (self.tamaño_tile * self.cantidad_zoom, self.tamaño_tile * self.cantidad_zoom))
        x = 0 + posicioncamara_x*self.cantidad_zoom
        y = 0 + posicioncamara_y*self.cantidad_zoom
        for c_vertical in range(len(lista_mapa)):

            for c_horizontal in range(len(lista_mapa[c_vertical])):

                if self.mapa[c_vertical][c_horizontal] == 1: # Es cesped:
                
                    surface_pintar.blit(tile_cesped_escalado, (x, y))


                x = x + self.tamaño_tile*self.cantidad_zoom

            x = 0 + posicioncamara_x*self.cantidad_zoom

            # Sumamos verticalmente tamaño del tile:
            y = y + self.tamaño_tile*self.cantidad_zoom

    def CargarDecoracion(self, surface_pintar, lista_de_listas_de_objeto, lista_de_imagen, posjugador_y):
        '''
        Importante! poner imagenes de a lista: lista_de_imagen en el orden correcto de elif de esta funcion
        '''
        # Vamos a crear una lista de imagenes escaladas de la lista de imagenes de nuestro parametro: lista_listas_de_imagen
        lista_imagenes_escaladas = []
        for imagen in range(len(lista_de_imagen)):
            lista_imagenes_escaladas.append(pygame.transform.scale(lista_de_imagen[imagen], (lista_de_imagen[imagen].get_width() * self.cantidad_zoom, lista_de_imagen[imagen].get_height() * self.cantidad_zoom)))
        #imagen_objeto_escalado = pygame.transform.scale(imagen_objeto, (imagen_objeto.get_width() * self.cantidad_zoom, imagen_objeto.get_height() * self.cantidad_zoom))
        frame_actual = pygame.time.get_ticks()//150 #Modificar el 150 que es la duracion de cada frame para hacerlo mas lento

        #Creamos una lista con su contenido unido a una nueva lista:
        lista_objeto_jugador = []
        for lista in range(len(lista_de_listas_de_objeto)):
            lista_objeto_jugador = lista_de_listas_de_objeto[lista].copy() + lista_objeto_jugador

        

        #Ahora metemos jugador en nuestra nueva lista
        lista_objeto_jugador.append([jugador.posjugador_x, jugador.posjugador_y, "jugador"]) # Añadimos pos del jugador a la lista
        lista_objeto_jugador = sorted(lista_objeto_jugador, key=lambda x: x[1]) # Ordenamos por "y"

        for i in range(len(lista_objeto_jugador)):
            x = lista_objeto_jugador[i][0]
            y = lista_objeto_jugador[i][1]
            x = (x+self.camera_x)*self.cantidad_zoom
            y = (y+self.camera_y)*self.cantidad_zoom

            
            # En caso de que el objeto este delante del jugador osea "y" dibujamos:
            if lista_objeto_jugador[i][-1] == "bala":
                surface_pintar.blit(lista_imagenes_escaladas[2], (x, y)) # Sin mitad me interesa que este detras
            elif lista_objeto_jugador[i][-1] == "jugador":
                jugador.ImprimirJugador(self.screen, juego.angulo, None,  frame_actual)
            elif lista_objeto_jugador[i][-1] == "arbol":
                surface_pintar.blit(lista_imagenes_escaladas[0], (x, y-(lista_imagenes_escaladas[0].get_height()/1.5))) #Lo imprimo la mitad porque quiero lograr el efecto de que si pasa por la mitad imprime de frente
                pygame.draw.circle(surface_pintar, (255, 255, 0), (x, y), 5)
            elif lista_objeto_jugador[i][-1] == "petroleo":
                surface_pintar.blit(lista_imagenes_escaladas[1], (x, y-(lista_imagenes_escaladas[1].get_height()/1.5))) #Lo imprimo la mitad porque quiero lograr el efecto de que si pasa por la mitad imprime de frente
            

            
    def EncontrarPuntoMinimapa(self, pos_jugador_x, pos_jugador_y, ancho_minimapa, alto_minimapa, anchura_mapa, altura_mapa):
        '''
        Esta funcion pequeña coge la posicion del jugador y la anchura y altura del minimapa y el mapa
        real y devuele la posicion que estaria en el minimapa
        '''
        minimapa_x = pos_jugador_x / anchura_mapa * ancho_minimapa
        minimapa_y = pos_jugador_y / altura_mapa * alto_minimapa
        return minimapa_x, minimapa_y

    def CargarMenu(self):

        # Primero cargo mapa:
        self.screen.blit(self.imagen_mapa, self.pos_imagen_mapa)

        # Donde esta el jugador:
        posminimapa_x, posminimapa_y = self.EncontrarPuntoMinimapa(jugador.posjugador_x, jugador.posjugador_y, 122, 96, self.mapa_ancho, self.mapa_alto)
        pygame.draw.circle(self.screen, (255, 0, 255), (self.pos_imagen_mapa[0]+posminimapa_x, self.pos_imagen_mapa[1]+posminimapa_y), 5)

        # Ahora la barra inferior:
        self.screen.blit(self.imagen_barra, self.pos_imagen_barra)

        # Marcador:
        self.screen.blit(self.imagen_marcador, self.pos_imagen_marcador)

        # Ahora la cantidad de petroleo que tiene el jugador:
        self.screen.blit(self.imagen_gota_petroleo, self.gota_petroleo_pos)
        # Texto:
        texto_petroleo = ("X " + str(self.petroleo_jugador))
        # Crear una superficie de texto usando la fuente
        surface_texto_petroleo = self.fuente_recursos.render(texto_petroleo, True, (25, 25, 25))
        # Obteniendo el rectángulo para la superficie de texto
        rect_texto_petroleo = surface_texto_petroleo.get_rect()
        # Posicion:
        rect_texto_petroleo.topleft = ((self.gota_petroleo_pos[0]+80, self.gota_petroleo_pos[1]+15))
        self.screen.blit(surface_texto_petroleo, rect_texto_petroleo)
        

        # Y balas:
        self.screen.blit(self.imagen_bala_icono, self.bala_icono_pos)
        # Texto:
        texto_balas = ("X " + str(self.balas_jugador))
        # Crear una superficie de texto usando la fuente
        surface_texto_balas = self.fuente_recursos.render(texto_balas, True, (168, 153, 17))
        # Obteniendo el rectángulo para la superficie de texto
        rect_texto_balas = surface_texto_balas.get_rect()
        # Posicion:
        rect_texto_balas.topleft = ((self.bala_icono_pos[0]+80, self.bala_icono_pos[1]+15))
        self.screen.blit(surface_texto_balas, rect_texto_balas)


    def ColocarYacimiento(self, lista_yacimientos, lista_yacimiento_jugador, usuario_jugador):


        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            
            self.tecla_1_pulsado = True

        if self.tecla_1_pulsado == True: #Boton se a apretado "pero no mantenido"
            raton_x, raton_y = tuple(pygame.mouse.get_pos())
            raton_x = int(raton_x-(50*self.cantidad_zoom)) #Le resto la mitad del cuadro 100px porque queremos el cuadrado del raton en el centro y no en la esquina de arriba
            raton_y = int(raton_y-(50*self.cantidad_zoom))
            ancho, alto = 100*self.cantidad_zoom, 200*self.cantidad_zoom
            
            self.screen.blit(self.yacimiento_petroleo_arreglado_colocando, (raton_x, raton_y))

            # Obtenemos el estado del click izq raton:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #Raton a hecho click

                    raton_x, raton_y = tuple(pygame.mouse.get_pos())
                    raton_x = int(raton_x-(50*self.cantidad_zoom)) #Le resto la mitad del cuadro 100px porque queremos el cuadrado del raton en el centro y no en la esquina de arriba
                    raton_y = int(raton_y-(50*self.cantidad_zoom))

                    if self.camera_x < 0:
                        #Camara va a la derecha # Piensa que el mapa empieza en posicion negativo porque en pygame empieza en 0,0
                        x_mouse = int(((raton_x*-1)+((self.camera_x)*2))*self.cantidad_zoom) # lo convierte en negativo 
                    else:
                        #Camara va a la izquierda
                        x_mouse = int(((raton_x)-(self.camera_x))*self.cantidad_zoom)  # lo convierte en positivo

                    if self.camera_y < 0:
                        #Camara va abajo
                        y_mouse = int(((raton_y*-1)+((self.camera_y)*2))*self.cantidad_zoom)  # lo convierte en negativo
                    else:
                        #Camara va arriba:
                        y_mouse = int(((raton_y)-(self.camera_y))*self.cantidad_zoom)  # lo convierte en positivo


                    for yacimiento in range(len(lista_yacimientos)):
              
                        x_yacimiento = int((lista_yacimientos[yacimiento][0]-self.camera_x)*self.cantidad_zoom)
                        y_yacimiento = int((lista_yacimientos[yacimiento][1]-self.camera_y)*self.cantidad_zoom)
                        x_yacimiento = x_yacimiento *-1
                        y_yacimiento = y_yacimiento *-1

                        #print("mouse: " + str(x_mouse) + " " + str(y_mouse) + " yacimiento: " + str(x_yacimiento) + " " + str(y_yacimiento))
                        if self.Colision2DCajas(x_mouse, y_mouse, 100*self.cantidad_zoom, 100*self.cantidad_zoom, x_yacimiento, y_yacimiento, ancho, alto) == True:
                            
                            #Cogemos el yacimiento de la lista publica y eliminamos el yacimiento y lo metemos a la lista del jugador con la misma posicion
                            #En esta lista del jugador el formato es: [x, y, "nombre_del_jugador", vida_objeto, "tipo_objeto"]

                            x_yacimiento, y_yacimiento =  lista_yacimientos[yacimiento][0], lista_yacimientos[yacimiento][1]

                            del lista_yacimientos[yacimiento]


                            jugador.lista_yacimiento_petroleo_jugador.append([jugador.posjugador_x, jugador.posjugador_y, usuario_jugador, 2, "yacimiento"])
                            print("elemento añadido a lista del jugadoor: " + usuario_jugador)

                            self.tecla_1_pulsado = False
                            break

                

    def Crear_Surface_Fuente_Imprimir(self, tamaño_fuente, texto, color, posicion, surface_opcional_encima, offset_xy=None):
        '''
        Me tienes que dar o el surface de la imagen que quieres poner encima el texto o poner el offset para ajustar pos texto
        '''
        fuente = pygame.font.Font(self.ruta_fuente, int(tamaño_fuente*self.cantidad_zoom))
        x, y = posicion
        if not surface_opcional_encima == None:
            x, y = (((x-(surface_opcional_encima.get_width()/1.5))+self.camera_x)*self.cantidad_zoom, ((y-(surface_opcional_encima.get_height()/4))+self.camera_y)*self.cantidad_zoom)
        else:
            #Me han dado offset_xy
            x_offset, y_offset = offset_xy
            x, y = (((x-x_offset)+self.camera_x)*self.cantidad_zoom, ((y-y_offset)+self.camera_y)*self.cantidad_zoom)

        posicion = x, y # Nuevas cordenadas
        # Crear una superficie de texto usando la fuente
        superficie_texto = fuente.render(texto, True, (255, 255, 255))
        # Obteniendo el rectángulo para la superficie de texto
        rectangulo_texto = superficie_texto.get_rect()
        #Posicion:
        rectangulo_texto.topleft = posicion
        self.screen.blit(superficie_texto, rectangulo_texto)

    def BarraVida(self, valor_vida, posicion, offset=(0, 0)):
        '''
        Esta funcion solo crea una barra de vida que va cambiando segun el valor vida cambie
        '''
        #Primero imagen
        x_sin_camara, y_sin_camara = posicion
        x_camara_con_offset = ((x_sin_camara+offset[0])+self.camera_x)*self.cantidad_zoom
        y_camara_con_offset = ((y_sin_camara+offset[1])+self.camera_y)*self.cantidad_zoom
        x_camara_sin_offset = (x_sin_camara+self.camera_x)*self.cantidad_zoom
        y_camara_sin_offset = (y_sin_camara+self.camera_y)*self.cantidad_zoom

        posicion = (x_camara_sin_offset, y_camara_sin_offset)

        imagen_escalada_barra = pygame.transform.scale(self.imagen_barra_vida, (self.imagen_barra_vida.get_width() * self.cantidad_zoom, self.imagen_barra_vida.get_height() * self.cantidad_zoom))
        self.screen.blit(imagen_escalada_barra, posicion)

        #Ahora barra de vida roja
        offset_x, offset_y = offset

        
        if valor_vida == 5:
            rect_imagen_copia = pygame.Rect((x_camara_con_offset), y_camara_con_offset, imagen_escalada_barra.get_width()/1.4, imagen_escalada_barra.get_height()/2)
        elif valor_vida == 4:
            rect_imagen_copia = pygame.Rect((x_camara_con_offset), y_camara_con_offset, imagen_escalada_barra.get_width()/1.8, imagen_escalada_barra.get_height()/2)
        elif valor_vida == 3:
            rect_imagen_copia = pygame.Rect((x_camara_con_offset), y_camara_con_offset, imagen_escalada_barra.get_width()/2, imagen_escalada_barra.get_height()/2)
        elif valor_vida == 2:
            rect_imagen_copia = pygame.Rect((x_camara_con_offset), y_camara_con_offset, imagen_escalada_barra.get_width()/2.8, imagen_escalada_barra.get_height()/2)
        elif valor_vida == 1:
            rect_imagen_copia = pygame.Rect((x_camara_con_offset), y_camara_con_offset, imagen_escalada_barra.get_width()/5, imagen_escalada_barra.get_height()/2)
        else:
            rect_imagen_copia = pygame.Rect((x_camara_con_offset), y_camara_con_offset, 0, imagen_escalada_barra.get_height()/2)

        pygame.draw.rect(self.screen, (145, 14, 14), rect_imagen_copia)


    
    def CargarObjetosJugadores(self, lista_objeto_usuario, surface_imagen):
        '''
        Esta funcion va a imprimir por pantalla los objetos de los jugadores como yacimientos, tiendas etc ...

        lista_objeto_usuario=> El tipo de objeto

        '''
        imagen_escalada_yacimiento = pygame.transform.scale(self.imagen_yacimiento_jugador, (self.imagen_yacimiento_jugador.get_width() * self.cantidad_zoom, self.imagen_yacimiento_jugador.get_height() * self.cantidad_zoom))
        for lista in range(len(lista_objeto_usuario)):
            x_sin_camara, y_sin_camara = lista_objeto_usuario[lista][0], lista_objeto_usuario[lista][1]
            #De posicion real a pos => camara
            x = (x_sin_camara+self.camera_x)*self.cantidad_zoom
            y = (y_sin_camara+self.camera_y)*self.cantidad_zoom

            usuario_jugador = lista_objeto_usuario[lista][2]
            vida_objeto = lista_objeto_usuario[lista][3]

            #Imprimo imagen
            self.screen.blit(imagen_escalada_yacimiento, (x, y))
            self.Crear_Surface_Fuente_Imprimir(70, usuario_jugador, (209, 115, 255), (x_sin_camara, y_sin_camara), self.imagen_yacimiento_jugador)

            #Ahora barra vida:
            self.BarraVida(vida_objeto, (x_sin_camara, y_sin_camara), (+21, +5))





                    
            
                
        
        
        
    
                
                
            



        
    def run(self):
        running = True
        while running == True:
            self.clock.tick(60) # Fijamos la tasa de actualización a 60 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    exit() # Cerramos python
            
            # Obtenemos el estado de todas las teclas
            keys = pygame.key.get_pressed()

            # Actualizamos la posición de la cámara según si hay colision entre la pantalla impirimida y nuestro jugador

            # Conseguimos x y y de la esquina izquierda de nuestra pantalla
            rect = self.screen.get_rect()
            pos_pantalla_x, pos_pantalla_y = rect.x, rect.y

            # Movimiento normal del jugador con teclas: w a s d
            #print("pos_jugador: ", str(jugador.posjugador_x), str(jugador.posjugador_y), "pos_camara: " + str(self.camera_x), str(self.camera_y))
            if keys[pygame.K_a]:

                self.tecla_pulsada = True
                jugador.posjugador_x = jugador.posjugador_x - 4
                jugador.posjugador_pantalla_x = jugador.posjugador_pantalla_x  - 4

                if (jugador.posjugador_pantalla_x-80) < pos_pantalla_x:
                    self.camera_x = round((self.camera_x + (self.camera_speed/2) * self.cantidad_zoom), 2)
                    jugador.posjugador_pantalla_x = jugador.posjugador_pantalla_x + (self.camera_speed/2) * self.cantidad_zoom

            if keys[pygame.K_d]:
                self.tecla_pulsada = True
                jugador.posjugador_x = jugador.posjugador_x + 4
                jugador.posjugador_pantalla_x = jugador.posjugador_pantalla_x  + 4

                if (jugador.posjugador_pantalla_x+160) > self.ancho_ventana/self.cantidad_zoom:
                    self.camera_x = round((self.camera_x - (self.camera_speed/2) * self.cantidad_zoom), 2)
                    jugador.posjugador_pantalla_x = jugador.posjugador_pantalla_x - (self.camera_speed/2) * self.cantidad_zoom

            if keys[pygame.K_w]:
                self.tecla_pulsada = True
                jugador.posjugador_y = jugador.posjugador_y - 4
                jugador.posjugador_pantalla_y = jugador.posjugador_pantalla_y  - 4

                if (jugador.posjugador_pantalla_y-80) < pos_pantalla_y:
                    self.camera_y = round((self.camera_y + (self.camera_speed/2) * self.cantidad_zoom), 2)
                    jugador.posjugador_pantalla_y = jugador.posjugador_pantalla_y + (self.camera_speed/2) * self.cantidad_zoom

            if keys[pygame.K_s]:
                self.tecla_pulsada = True
                jugador.posjugador_y = jugador.posjugador_y + 4
                jugador.posjugador_pantalla_y = jugador.posjugador_pantalla_y  + 4

                if (jugador.posjugador_pantalla_y+160) > self.altura_ventana/self.cantidad_zoom:
                    self.camera_y = round((self.camera_y - (self.camera_speed/2) * self.cantidad_zoom), 2)
                    jugador.posjugador_pantalla_y = jugador.posjugador_pantalla_y - (self.camera_speed/2) * self.cantidad_zoom

            #Actualizar pantalla local con teclas de flecha:

            if keys[pygame.K_RIGHT]:
                self.camera_x = round((self.camera_x - self.camera_speed * self.cantidad_zoom), 2)
                jugador.posjugador_pantalla_x = jugador.posjugador_pantalla_x - self.camera_speed * self.cantidad_zoom
            if keys[pygame.K_LEFT]:
                self.camera_x = round((self.camera_x + self.camera_speed * self.cantidad_zoom), 2)
                jugador.posjugador_pantalla_x = jugador.posjugador_pantalla_x + self.camera_speed * self.cantidad_zoom
            if keys[pygame.K_DOWN]:
                self.camera_y = round((self.camera_y - self.camera_speed * self.cantidad_zoom), 2)
                jugador.posjugador_pantalla_y = jugador.posjugador_pantalla_y - self.camera_speed * self.cantidad_zoom
            if keys[pygame.K_UP]:
                self.camera_y = round((self.camera_y + self.camera_speed * self.cantidad_zoom), 2)
                jugador.posjugador_pantalla_y = jugador.posjugador_pantalla_y + self.camera_speed * self.cantidad_zoom



            # Activar y desactivar zoom
            self.zoom_teclado()
            # Toca llamar a escalar imagnes porque a cambiado zoom
            jugador.EscalarImagenJugador(self.zoom_cambiado)
                
            self.screen.fill((255, 255, 255)) # Rellenamos la pantalla de blanco

            

            self.Cargar_Mapa(self.mapa, self.screen, self.camera_x, self.camera_y) # Cargamos mapa
            
            lista_imagenes = [self.arbol1, self.yacimiento_petroleo, self.imagen_bala_icono]
            lista_lista_objetos = [self.lista_arboles, self.lista_yacimiento_petroleo, self.lista_balas_iconos]

            # Cargamos yacimientos:
            self.CargarDecoracion(self.screen, lista_lista_objetos, lista_imagenes, jugador.posjugador_pantalla_y)

            #Cargamos objetos de jugador:
            self.CargarObjetosJugadores(jugador.lista_yacimiento_petroleo_jugador, self.imagen_yacimiento_jugador)
            
            datos_mouse = self.PosicionMouse(jugador.posjugador_x, jugador.posjugador_pantalla_y) # Esto nos da una tupla con : x, y, distancia y angulo en grados
            # Pongo el nuevo angulo:
            self.angulo = datos_mouse[3]

            
            pygame.draw.circle(self.screen, (255, 240, 255), (50, 50), 10)
            pygame.draw.circle(self.screen, (255, 240, 255), (jugador.posjugador_x, jugador.posjugador_y), 10)

            #Barra inferior
            self.ColocarYacimiento(self.lista_yacimiento_petroleo, jugador.lista_yacimiento_petroleo_jugador, "Robert_Connolly")

            #Miro si icono de la bala colisiona con el jugador:
            self.ComprobarColisionBalaIJugador((jugador.posjugador_x, jugador.posjugador_y), self.lista_balas_iconos)

            #Cargo Menu local:
            self.CargarMenu()

            pygame.draw.circle(self.screen, (255, 255, 0), (self.camera_x, self.camera_y), 30)
        

        
            
            pygame.display.flip() # Actualizamos la pantalla

    def PosicionMouse(self, posicion_jugador_x, posicion_jugador_y):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        distancia = self.Distancia2Puntos(mouse_x, mouse_y, posicion_jugador_x, posicion_jugador_y)
        angulo_degree = self.Angulo2Puntos(mouse_x, mouse_y, posicion_jugador_x, posicion_jugador_y, False)
        return (mouse_x, mouse_y, distancia, angulo_degree)
    
    def ComprobarColisionBalaIJugador(self, posicionjugador, lista_balas_icono):
        posjugador_x, posjugador_y = posicionjugador

        for iterador in range(len(lista_balas_icono)):
            ibala_x, ibala_y, _ = lista_balas_icono[iterador]
            #Miramos si el icono de bala colisiona con jugador:
            if self.Distancia2Puntos(posjugador_x, posjugador_y, ibala_x, ibala_y) < 20:
                print("colision entre i_bala y jugador!")
                del lista_balas_icono[iterador] # Elimino la bala de la lista del server
                self.balas_jugador = self.balas_jugador+1 #Añadimos una bala al jugador
                break

class Jugador:
    def __init__(self):
        # Constructor:
        # Esta posicion no es real "no se puede utulizar en red" se le añade la camara local (que se mueve)
        self.posjugador_pantalla_x = 0
        self.posjugador_pantalla_y = 0
        # Posicion real sin camara añadida
        self.posjugador_y = 0
        self.posjugador_x = 0
        self.angulo_jugador = 0
        self.caja_camara_jugador = (200, 200) # Esto es la caja de colision del jugador

        #Nombre usuario:
        self.usuario_jugador = "Robert"

        # Cargo imagenes:
        self.fronteus = pygame.image.load("frenteus.png")
        self.atrasus = pygame.image.load("atrasus.png")

        # Caminando:
        self.fronteuscaminando1 = pygame.image.load("frenteuscaminando1.png")
        self.fronteuscaminando2 = pygame.image.load("frenteuscaminando2.png")
        self.atrasuscaminando1 = pygame.image.load("atrasuscaminando1.png")
        self.atrasuscaminando2 = pygame.image.load("atrasuscaminando2.png")

        # Imagenes Escaladas que son escaldas solo cuando se hace zoom:
        self.atrasus_ecalado = self.atrasus
        self.fronteus_ecalado = self.fronteus
        self.fronteuscaminando1_esclado = self.fronteuscaminando1
        self.fronteuscaminando2_esclado = self.fronteuscaminando2
        self.atrasuscaminando1_esclado = self.atrasuscaminando1
        self.atrasuscaminando2_esclado = self.atrasuscaminando2

        # Yacimiento petrolifero del jugador:
        self.lista_yacimiento_petroleo_jugador = []


    def EscalarImagenJugador(self, zoom_cambiado=False):
        '''
        Esta funcion cuando se la llama con el bool en True va a escalar todas las imagenes del jugador a la nueva cantidad de zoom
        '''
        if zoom_cambiado == True:
            self.atrasus_ecalado = pygame.transform.scale(self.atrasus, (self.atrasus.get_width() * juego.cantidad_zoom, self.atrasus.get_width() * juego.cantidad_zoom))
            self.fronteus_ecalado = pygame.transform.scale(self.fronteus, (self.fronteus.get_width() * juego.cantidad_zoom, self.fronteus.get_width() * juego.cantidad_zoom))
            self.fronteuscaminando1_esclado = pygame.transform.scale(self.fronteuscaminando1, (self.fronteuscaminando1.get_width() * juego.cantidad_zoom, self.fronteuscaminando1.get_width() * juego.cantidad_zoom))
            self.fronteuscaminando2_esclado = pygame.transform.scale(self.fronteuscaminando2, (self.fronteuscaminando2.get_width() * juego.cantidad_zoom, self.fronteuscaminando2.get_width() * juego.cantidad_zoom))
            self.atrasuscaminando1_esclado = pygame.transform.scale(self.atrasuscaminando1, (self.atrasuscaminando1.get_width() * juego.cantidad_zoom, self.atrasuscaminando1.get_width() * juego.cantidad_zoom))
            self.atrasuscaminando2_esclado = pygame.transform.scale(self.atrasuscaminando2, (self.atrasuscaminando2.get_width() * juego.cantidad_zoom, self.atrasuscaminando2.get_width() * juego.cantidad_zoom))

            zoom_cambiado = False


    def ImprimirJugador(self, pantalla, angulo_objectivo, direccion: str, frame_actual):
        

        x = self.posjugador_pantalla_x *juego.cantidad_zoom
        y = self.posjugador_pantalla_y *juego.cantidad_zoom
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_s]:
            tecla_pulsada = True
        else:
            tecla_pulsada = False


        #Primero imprimimos si esta quieto
        if angulo_objectivo > 0 and angulo_objectivo < 180:
            if tecla_pulsada == False:
                pantalla.blit(self.atrasus_ecalado, (x, y))
            else:
                if frame_actual % 2 == 0:
                    imagen_actual = self.atrasuscaminando1_esclado
                else:
                    imagen_actual = self.atrasuscaminando2_esclado
                tecla_pulsada = False
                pantalla.blit(imagen_actual, (x, y))
                

        if angulo_objectivo < -1 and angulo_objectivo > -180:

            if tecla_pulsada == False:
                pantalla.blit(self.fronteus_ecalado, (x, y))
            else:
                if frame_actual % 2 == 0:
                    imagen_actual = self.fronteuscaminando1_esclado
                else:
                    imagen_actual = self.fronteuscaminando2_esclado
                
                pantalla.blit(imagen_actual, (x, y))
                tecla_pulsada = False

        



                
            

juego = Juego()
jugador = Jugador()
jugador2 = Jugador()


juego.zoom_teclado()
juego.run()
