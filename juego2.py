import pygame
import math
import sys
from random import randint
import random
import socket
import json
import threading
import time

#from TCP_Server import recibir_lista

class Host:
    def __init__(self, IP_HOST, Puerto, Es_Host=False):
        # Seccion sockets:
        
        self.lista_clientes = []
        self.lista_usuarios = []
        # Create a socket object
        if Es_Host == True:
            print("funciona")
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Bind del socket
            self.socket.bind((IP_HOST, Puerto))
            self.socket.listen(3) #Limitado a 2 jugador + host = 3 
            hilo_nueva_conexion = threading.Thread(target=self.NuevaConexion) # Creo hilo nuevo
        
            hilo_nueva_conexion.start() # Inicio hilo
        else: # si no es host se conecta a la ip
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((IP_HOST, Puerto))
        


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
        self.tecla_2_pulsado = False

        #Marcador
        self.imagen_marcador = pygame.image.load("marcador.png")
        self.pos_imagen_marcador = (667, 11)
        self.dimensiones_imagen_marcador = (self.imagen_marcador.get_width(), self.imagen_marcador.get_height())
        self.fuente_nombre = pygame.font.Font(self.ruta_fuente, 35)
        self.posnombre = (695, 45)
        self.imagen_cabeza_ryan = pygame.image.load("cabeza_ryan.png")

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
        for i in range(100):
            self.lista_arboles.append([randint(0, self.mapa_ancho), randint(0, self.mapa_alto), "arbol"])

        self.lista_yacimiento_petroleo = []
        self.lista_yacimiento_petroleo.append([200, 200, "petroleo"])
        self.lista_yacimiento_petroleo.append([200, 6000, "petroleo"])
        for i in range(30):
            self.lista_yacimiento_petroleo.append([randint(0, self.mapa_ancho), randint(0, self.mapa_alto), "petroleo"])

        self.lista_balas_iconos = []
        for a in range(100):
            self.lista_balas_iconos.append([randint(0, self.mapa_ancho), randint(0, self.mapa_alto), "bala"])

        #Otros jugadores:
        self.listapos_otrosjugadores = []
        self.listapos_soldados_jugadores = []
        self.tiempo_pasado = time.time()
        self.tiempo_actual = 0

        # Cargo imagenes:
        self.tile_cesped = pygame.image.load("cesped200.png")
        self.arbol1 = pygame.image.load("arbol1.png")
        self.yacimiento_petroleo = pygame.image.load("yacimiento_petroleo.png")
        self.yacimiento_petroleo_arreglado = pygame.image.load("yacimiento_petroleo_arreglado.png")
        self.yacimiento_petroleo_arreglado_colocando = pygame.image.load("yacimiento_petroleo_arreglado_colocando.png")
        self.imagen_barra_vida = pygame.image.load("barravida.png")
        self.imagen_yacimiento_jugador = pygame.image.load("yacimiento_petroleo_arreglado.png")
        self.imagen_tienda_campana = pygame.image.load("tienda_rosa.png")
        self.imagen_tienda_campana_colocando = pygame.image.load("tienda_rosa_colocando.png")

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
        
    #Seccion Sockets:
    def NuevaConexion(self):
        '''
        Esta funcion es para que el host reciba nuevos usuarios y lo envia a su lista de usuarios:
        '''
        while True:
            if len(self.lista_clientes) < 3: # Limite de 2 jugador +
                cliente, addr = self.socket.accept()
            print("Nueva conexion con ip: " + str(addr))

            #Añadimos cliente a nuestra lista de clientes :
            self.lista_clientes.append(cliente)
            print('Number of connected clients:', len(self.lista_clientes))
            # Decirle a cliente que nos de su nombre_usuario
            dame_tu_nombre = ["NOMBRE", ""]

            # Convertir datos python a bytes
            datos = json.dumps(dame_tu_nombre)

            # Enviar bytes sobre socket
            cliente.send(datos.encode())



            hilo_recibir = threading.Thread(target=self.RecibirMensaje, args=(cliente,)) # Creo hilo nuevo
            #hilo_recordatorio_host = threading.Thread(target=self.RecordatorioHost,) # Creo hilo nuevo
            #hilo_recordatorio_host.start()
            hilo_recibir.start()
            

    def RecibirMensaje(self, cliente):
        while True:
            try:
                mensaje_tipo = cliente.recv(2048)
                if len(mensaje_tipo) > 0: # no esta vacio
                    print("mensaje no esta vacio: ")
                    mensaje_tipo = mensaje_tipo.decode()
                    mensaje_desencriptado = json.loads(mensaje_tipo)

                    print("Cliente dijo: " + str(mensaje_desencriptado))
                    print(len(mensaje_desencriptado[0]) == len("1"))
                    #Aqui tenemos los tipos de mensaje y luego los mensajes:

                    if mensaje_desencriptado[0] == "USUARIO":
                        self.lista_usuarios.append(mensaje_desencriptado[1]) #Añado su nombre a mi lista
                        print("enviando broadcast")
                        print(self.lista_clientes)
                        time.sleep(0.3)
                        self.Broadcast("Gracias por tu usuario! cliente", cliente)
                    elif mensaje_desencriptado[0] == "LISTA_ARBOLES":
                        #Me va a enviar su usuario:
                        lista_arboles = [["LISTA_ARBOLES"], [self.lista_arboles]]
                        lista_arboles_encriptado = json.dumps(lista_arboles)
                        lista_arboles_encriptado = lista_arboles_encriptado.encode()
                        print("Enviando arboles")
                        cliente.send(lista_arboles_encriptado)
                    elif mensaje_desencriptado[0] == "LISTA_YACIMIENTOS":
                        #Me va a enviar su usuario:
                        lista_yacimientos = [["LISTA_YACIMIENTOS"], [self.lista_yacimiento_petroleo]]
                        lista_yacimientos_encriptado = json.dumps(lista_yacimientos)
                        lista_yacimientos_encriptado = lista_yacimientos_encriptado.encode()
                        print("Enviando yacimientos")
                        cliente.send(lista_yacimientos_encriptado)
                    elif mensaje_desencriptado[0] == "LISTA_BALAS":
                        #Me va a enviar su usuario:
                        lista_balas = [["LISTA_BALAS"], [self.lista_balas_iconos]]
                        lista_balas_encriptado = json.dumps(lista_balas)
                        lista_balas_encriptado = lista_balas_encriptado.encode()
                        print("Enviando balas")
                        cliente.send(lista_balas_encriptado)
                    elif mensaje_desencriptado[0] == "POS_JUGADOR":

                        self.listapos_otrosjugadores.append(mensaje_desencriptado[1])
                        print(self.listapos_otrosjugadores)
                    else:
                        #No le he entendido
                        no_entendido = "No te he entendido"
                        no_entendido = json.dumps(no_entendido)
                        no_entendido = no_entendido.encode()
                        time.sleep(0.1)
                        cliente.send(no_entendido)
            except:
                index_cliente = self.lista_clientes.index(cliente) # Cojemos el index de la lista clientes
                self.lista_clientes.remove(cliente)
                cliente.close()
                break

    def Broadcast(self, mensaje_desencriptado, cliente):
        '''
        Esta funciona solo va a enviar un mensaje a cada cliente en nuestra lista
        '''
        mensaje = str("Broadcast : " + mensaje_desencriptado)
        mensaje_encriptado = json.dumps(mensaje)
        mensaje_encriptado = mensaje_encriptado.encode()

        print("enviando mensaje bc")
        cliente.send(mensaje_encriptado) # Enviamos el mensaje a cada cliente

    def RecordatorioHost(self):
        '''
        El host cada 2 segundos(mas o menos) va a recordar a sus usuarios que manden la nueva poscion de sus jugadores y soldados:
        '''
        mensaje = ["DAME_POS_JUGADOR", ""]
        mensaje_encriptado = json.dumps(mensaje)
        mensaje_encriptado = mensaje_encriptado.encode()
        while True:
            if (self.tiempo_actual - self.tiempo_pasado) >= 5: #an pasado 2 segundos
                for cliente in self.lista_clientes:
                    time.sleep(0.4)
                    print("Enviando recordatorio host!")
                    cliente.send(mensaje_encriptado)
                #Nuevo tiempo pasado es tiempo actual
                self.tiempo_pasado = time.time()



    def ImprimirOtrosJugadores(self):
        '''
        Comprobar si los otros jugadores se han movido si es asi imprimir segun su direccion
        '''
        for i in range(2):
            # Determina las coordenadas iniciales x e y de los puntos
            if len(self.listapos_otrosjugadores) > 2:
                x1, y1 = self.listapos_otrosjugadores[-2]
                x1_nuevo, y1_nuevo = self.listapos_otrosjugadores[-1]

                # Verifica la dirección del movimiento en las direcciones x e y
                direccion_x = ""
                direccion_y = ""

                if x1_nuevo > x1:
                    direccion_x = "derecha"
                elif x1_nuevo < x1:
                    direccion_x = "izquierda"

                if y1_nuevo > y1:
                    direccion_y = "arriba"
                elif y1_nuevo < y1:
                    direccion_y = "abajo"

                x, y = self.move_to(x1, y1, x1_nuevo, y1_nuevo)

                x1, y1 = x1+x/2, y1+y/2
                x1_camara_escalado = (x1+self.camera_x)*self.cantidad_zoom
                y1_camara_escalado = (y1+self.camera_y)*self.cantidad_zoom
                self.screen.blit(jugador.fronteus, (x1_camara_escalado, y1_camara_escalado))



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
                jugador.ImprimirJugador(self.screen, juego.angulo,  frame_actual)
            elif lista_objeto_jugador[i][-1] == "arbol":
                surface_pintar.blit(lista_imagenes_escaladas[0], (x, y-(lista_imagenes_escaladas[0].get_height()/1.5))) #Lo imprimo la mitad porque quiero lograr el efecto de que si pasa por la mitad imprime de frente
                pygame.draw.circle(surface_pintar, (255, 255, 0), (x, y), 5)
            elif lista_objeto_jugador[i][-1] == "petroleo":
                surface_pintar.blit(lista_imagenes_escaladas[1], (x, y-(lista_imagenes_escaladas[1].get_height()/1.5))) #Lo imprimo lda mitad porque quiero lograr el efecto de que si pasa por la mitad imprime de frente

            
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

        lista_usuarios = [jugador.usuario_jugador, jugador.usuario_jugador, jugador.usuario_jugador]
        lista_de_ryans = [jugador.numero_ryans, jugador.numero_ryans, jugador.numero_ryans]
        self.ImprimirMarcador(lista_usuarios, lista_de_ryans)

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


    def ImprimirMarcador(self, lista_nombre_usuarios, lista_ryan_raptados):
        '''
        Esta funciona coge todoso los nombres de jugadores y la lista de listas de ryans capturados
        si en una partida de 3 jugadores hay una persona consigue capturar 2 ryans y defender su ryan gana:
        este marcador imprime: nombre y la segunda linia 3 cabezas segun las que tenga capturadas
        !IMPORTANTE Mantener el mismo orden en las 2 listas ya que usaran el mismo iterador
        '''
        diferencia_y = 16
        pos_x, pos_y = self.posnombre[0], self.posnombre[1]+15
        for i in range(len(lista_nombre_usuarios)):
            #Imprimo el nombre de cada usuario de la lista:
            # Texto:
            texto_nombre = lista_nombre_usuarios[i]
            # Crear una superficie de texto usando la fuente
            surface_texto_nombre = self.fuente_nombre.render(texto_nombre, True, (206, 90, 235))
            # Obteniendo el rectángulo para la superficie de texto
            rect_texto_nombre = surface_texto_nombre.get_rect()
            # Posicion:
            rect_texto_nombre.topleft = ((pos_x, pos_y+15))
            self.screen.blit(surface_texto_nombre, rect_texto_nombre)

            pos_y = pos_y+diferencia_y

            #Imprimimos las cabezas de ryan segun jugador.numero_ryans
            if lista_ryan_raptados[i] == 1:
                self.screen.blit(self.imagen_cabeza_ryan, (pos_x+3, pos_y+22)) #offset

            elif lista_ryan_raptados[i] == 2:
                for a in range(2):
                    self.screen.blit(self.imagen_cabeza_ryan, (pos_x+3, pos_y+22))
                    pos_x = pos_x + 20
                pos_x = self.posnombre[0]
            elif lista_ryan_raptados[i] == 3:
                for a in range(3):
                    self.screen.blit(self.imagen_cabeza_ryan, (pos_x+3, pos_y+22))
                    pos_x = pos_x + 20
                pos_x = self.posnombre[0]

            #Añadimos y + 16 para el siguiente nombre
            pos_y = pos_y+diferencia_y
        


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


                            jugador.lista_yacimiento_petroleo_jugador.append([x_yacimiento, y_yacimiento, usuario_jugador, 5, "yacimiento"])
                            print("elemento añadido a lista del jugadoor: " + usuario_jugador)

                            self.tecla_1_pulsado = False
                            break


    def ColocarObjeto(self, lista_objeto_jugador, usuario_jugador, imagen_objeto_transparente, imagen_objeto, nombre_append_lista):


        keys = pygame.key.get_pressed()

        if keys[pygame.K_2]: #En caso de tecla 2:
            
            self.tecla_2_pulsado = True

        if self.tecla_2_pulsado == True: #Boton se a apretado "pero no mantenido"
            raton_x, raton_y = tuple(pygame.mouse.get_pos()) #Cogemos la posicion raton dentro del rango de pantalla
            raton_x = int(raton_x-(50*self.cantidad_zoom)) #Le resto la mitad del cuadro 100px porque queremos el cuadrado del raton en el centro y no en la esquina de arriba
            raton_y = int(raton_y-(50*self.cantidad_zoom))
            ancho, alto = imagen_objeto.get_width()*self.cantidad_zoom, imagen_objeto.get_height()*self.cantidad_zoom
            
            self.screen.blit(imagen_objeto_transparente, (raton_x, raton_y)) #imagen pre colocacion

            # Obtenemos el estado del click izq raton:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #Raton a hecho click

                    raton_x, raton_y = tuple(pygame.mouse.get_pos())
                    raton_x = int(raton_x-(50*self.cantidad_zoom)) #Le resto la mitad del cuadro 100px porque queremos el cuadrado del raton en el centro y no en la esquina de arriba
                    raton_y = int(raton_y-(50*self.cantidad_zoom))
                    raton_x = (raton_x+(self.camera_x*-1))
                    raton_y = (raton_y+(self.camera_y*-1))
                    #self.camera_x*-1 convierte camara en positivo para que lo pueda sumar a posicion raton
                    
                    lista_objeto_jugador.append([raton_x, raton_y, usuario_jugador, 5, nombre_append_lista])
                    print("elemento añadido a lista del jugadoor: " + usuario_jugador + str(lista_objeto_jugador))

                    self.tecla_2_pulsado = False
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
        y_camara_sin_offset = ((y_sin_camara-25)+self.camera_y)*self.cantidad_zoom

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


    
    def CargarObjetosJugadores(self, lista_objeto_usuario, surface_imagen, offset_texto, offset_barra_vida):
        '''
        Esta funcion va a imprimir por pantalla los objetos de los jugadores como yacimientos, tiendas etc ...

        lista_objeto_usuario=> El tipo de objeto

        '''
        imagen_escalada_imagen = pygame.transform.scale(surface_imagen, (surface_imagen.get_width() * self.cantidad_zoom, surface_imagen.get_height() * self.cantidad_zoom))
        for lista in range(len(lista_objeto_usuario)):
            x_sin_camara, y_sin_camara = lista_objeto_usuario[lista][0], lista_objeto_usuario[lista][1]

            #De posicion real a pos => camara
            x = (x_sin_camara+self.camera_x)*self.cantidad_zoom
            y = (y_sin_camara+self.camera_y)*self.cantidad_zoom

    

            usuario_jugador = lista_objeto_usuario[lista][2]
            vida_objeto = lista_objeto_usuario[lista][3]

            #Imprimo imagen
            self.screen.blit(imagen_escalada_imagen, (x, y))
            self.Crear_Surface_Fuente_Imprimir(70, usuario_jugador, (209, 115, 255), (x_sin_camara, y_sin_camara),None, offset_texto)

            #Ahora barra vida:
            self.BarraVida(vida_objeto, (x_sin_camara, y_sin_camara), offset_barra_vida)





                    
            
                
        
        
        
    
                
                
            



        
    def run(self):
        running = True
        while running == True:
            self.clock.tick(60) # Fijamos la tasa de actualización a 60 fps
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    exit() # Cerramos python
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_t:
                        print("The T key is pressed!")
                        jugador.CrearSoldados()
                    
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

            datos_mouse = self.PosicionMouse(jugador.posjugador_pantalla_x, jugador.posjugador_pantalla_y) # Esto nos da una tupla con : x, y, distancia y angulo en grados
            # Pongo el nuevo angulo:
            self.angulo = datos_mouse[3]

            self.Cargar_Mapa(self.mapa, self.screen, self.camera_x, self.camera_y) # Cargamos mapa

            #Miro si quiero una nueva bala
            if self.angulo > -90 and self.angulo < 0:
                jugador.DispararBala((jugador.posjugador_x+26, jugador.posjugador_y+26), 10, jugador.imagen_bala)
            else:
                jugador.DispararBala((jugador.posjugador_x+10, jugador.posjugador_y+26), 10, jugador.imagen_bala)

            #ImprimirBalas
            jugador.ImprimirBalas(self.screen, self.cantidad_zoom, (self.camera_x, self.camera_y))
            #Elimino las balas que esten fuera del mapa para ahorrar memoria:
            jugador.EliminarBalasFuera(self.mapa_ancho)
            
            lista_imagenes = [self.arbol1, self.yacimiento_petroleo, self.imagen_bala_icono]
            lista_lista_objetos = [self.lista_arboles, self.lista_yacimiento_petroleo, self.lista_balas_iconos]

            # Cargamos yacimientos, jugador, arbol etc ...:
            self.CargarDecoracion(self.screen, lista_lista_objetos, lista_imagenes, jugador.posjugador_pantalla_y)

            #Cargamos objetos de jugador:
            self.CargarObjetosJugadores(jugador.lista_yacimiento_petroleo_jugador, self.imagen_yacimiento_jugador, (+10, 70), (+20, -20))
            # Cargo tienda jugador
            self.CargarObjetosJugadores(jugador.lista_tienda_campaña, self.imagen_tienda_campana, (+10, +70), (+20, -20))
            
            # Cargo Lista de soldados:
            frame_actual = pygame.time.get_ticks()//150 #Modificar el 150 que es la duracion de cada frame para hacerlo mas lento
            self.ImprimirSoldados(jugador.lista_soldados, juego.angulo, frame_actual)
            #Los muevo en fila india:
            jugador.MoverSoldadosFilaIndia(jugador.lista_soldados, 100, 60)

            #Imprimo otros jugadores:
            #self.ImprimirOtrosJugadores()
            if (self.tiempo_actual - self.tiempo_pasado) >= 1:
                jugador.posjugador_x_anterior = jugador.posjugador_x
                jugador.posjugador_y_anterior = jugador.posjugador_y


            pygame.draw.circle(self.screen, (255, 240, 255), (50, 50), 10)
            pygame.draw.circle(self.screen, (255, 240, 255), (jugador.posjugador_x, jugador.posjugador_y), 10)

            #Barra inferior
            self.ColocarYacimiento(self.lista_yacimiento_petroleo, jugador.lista_yacimiento_petroleo_jugador, "Roberto")
            #Tienda de campaña
            self.ColocarObjeto(jugador.lista_tienda_campaña, "Roberto", self.imagen_tienda_campana_colocando, self.imagen_tienda_campana, "tienda")

            #Miro si icono de la bala colisiona con el jugador:
            self.ComprobarColisionBalaIJugador((jugador.posjugador_x, jugador.posjugador_y), self.lista_balas_iconos)

            #Cargo Menu local:
            self.CargarMenu()

            #Host necesita nueva pos?
            self.tiempo_actual = time.time()

            pygame.draw.circle(self.screen, (255, 255, 0), (self.camera_x, self.camera_y), 30)
        

        
            
            pygame.display.flip() # Actualizamos la pantalla

    def PosicionMouse(self, posicion_jugador_x, posicion_jugador_y):
        mouse_x, mouse_y = pygame.mouse.get_pos()


        distancia = self.Distancia2Puntos(mouse_x-self.camera_x, mouse_y-self.camera_y, posicion_jugador_x, posicion_jugador_y)
        angulo_degree = self.Angulo2Puntos(mouse_x, mouse_y, posicion_jugador_x, posicion_jugador_y, False)
        return (mouse_x, mouse_y, distancia, angulo_degree)
    
    def ComprobarColisionBalaIJugador(self, posicionjugador, lista_balas_icono):
        posjugador_x, posjugador_y = posicionjugador
        posjugador_x = posjugador_x + (jugador.atrasus.get_width()/2*self.cantidad_zoom)
        posjugador_y = posjugador_y + (jugador.atrasus.get_height()/2*self.cantidad_zoom)#deja los puntos ...


        for iterador in range(len(lista_balas_icono)):
            ibala_x, ibala_y, _ = lista_balas_icono[iterador]
            ibala_x = ibala_x + (self.imagen_bala_icono.get_width()/2*self.cantidad_zoom)
            ibala_y = ibala_y + (self.imagen_bala_icono.get_height()/2*self.cantidad_zoom)#deja los puntos de colision en el centro
       
            #Miramos si el icono de bala colisiona con jugador:
            if self.Distancia2Puntos(posjugador_x, posjugador_y, ibala_x, ibala_y) < 33:
                print("colision entre i_bala y jugador!")
                del lista_balas_icono[iterador] # Elimino la bala de la lista del server
                self.balas_jugador = self.balas_jugador+1 #Añadimos una bala al jugador
                break

    def ImprimirSoldados(self, lista_objetos_soldados, angulo_direccion, frame_actual):
        '''
        Esta funcion es para imprimir todos los soldados en pantalla de nuestra lista de objetos soldados
        '''
        for soldado in range(len(lista_objetos_soldados)):
            lista_objetos_soldados[soldado].EscalarImagenJugador(self.zoom_cambiado)
            lista_objetos_soldados[soldado].ImprimirJugador(self.screen, angulo_direccion, frame_actual)







class Jugador:

    def __init__(self):
        # Constructor:
        # Esta posicion no es real "no se puede utulizar en red" se le añade la camara local (que se mueve)
        self.posjugador_pantalla_x = 0
        self.posjugador_pantalla_y = 0
        # Posicion real sin camara añadida
        self.posjugador_y = 0
        self.posjugador_x = 0
        self.posjugador_x_anterior = 0
        self.posjugador_y_anterior = 0
        self.caja_camara_jugador = (200, 200) # Esto es la caja de colision del jugador

        #Ryan
        self.numero_ryans = 2
        self.pos_miryan = (self.posjugador_x, self.posjugador_y)

        #Soldados
        self.lista_soldados = []

        #Nombre usuario:
        self.usuario_jugador = "Roberto"
        
        # Cargo imagenes:
        self.fronteus = pygame.image.load("frenteus.png")
        self.atrasus = pygame.image.load("atrasus.png")
        self.imagen_bala = pygame.image.load("bala.png")
        self.rifle1 = pygame.image.load("rifle.png")
        self.rifle2 = pygame.image.load("rifle2.png")


        # Bala:
        self.lista_bala_jugador = []

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
        self.rifle1_escalado = self.rifle1
        self.rifle2_escalado = self.rifle2

        # Yacimiento petrolifero del jugador:
        self.lista_yacimiento_petroleo_jugador = []
        # Lista tiendas campaña
        self.lista_tienda_campaña = []


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
            self.rifle1_escalado = pygame.transform.scale(self.rifle1, (self.rifle1.get_width() * juego.cantidad_zoom, self.rifle1.get_height() * juego.cantidad_zoom))
            self.rifle2_escalado = pygame.transform.scale(self.rifle2, (self.rifle2.get_width() * juego.cantidad_zoom, self.rifle2.get_height() * juego.cantidad_zoom))

            zoom_cambiado = False


    def ImprimirJugador(self, pantalla, angulo_objectivo, frame_actual):
        
        
        x = (self.posjugador_x+juego.camera_x) * juego.cantidad_zoom
        y = (self.posjugador_y+juego.camera_y) * juego.cantidad_zoom
        x_rifle = (self.posjugador_x+juego.camera_x+18) *juego.cantidad_zoom
        y_rifle = (self.posjugador_y+juego.camera_y+20) *juego.cantidad_zoom
        
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
                
                tecla_pulsada = False
                pantalla.blit(imagen_actual, (x, y))

        #De arriba a abajo izq-der
        if angulo_objectivo > -90 and angulo_objectivo < 0:
            rifle_rotado = pygame.transform.rotate(self.rifle1_escalado, angulo_objectivo)
            
            imagen_actual_rifle = rifle_rotado
            pantalla.blit(imagen_actual_rifle, (x_rifle, y_rifle))

         #De arriba a abajo der-izq
        if angulo_objectivo < -90 and angulo_objectivo > -180:
            rifle_rotado = pygame.transform.rotate(self.rifle2_escalado, angulo_objectivo)
            
            imagen_actual_rifle = rifle_rotado
            pantalla.blit(imagen_actual_rifle, (x_rifle, y_rifle))

    def DispararBala(self, posicion_bala, velocidad_bala, surface_bala):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                raton_x, raton_y = pygame.mouse.get_pos()

                velocidad_bala = 3
                raton_x = (raton_x+(juego.camera_x*-1))
                raton_y = (raton_y+(juego.camera_y*-1))
               
                angulo_direccion = juego.Angulo2Puntos(self.posjugador_x, self.posjugador_y, raton_x, raton_y, radian=False)
                    
                surface_bala_rotada = pygame.transform.rotate(surface_bala, angulo_direccion)
                
                #Convierto en angulo de grados a radianes y lo invierto con *-1:
                angulo_radianes = math.radians(angulo_direccion*-1)
                
                posicion_bala_x, posicion_bala_y = posicion_bala

                projectile_dx = velocidad_bala * math.cos(angulo_radianes)
                projectile_dy = velocidad_bala * math.sin(angulo_radianes)

                #Nueva bala en la lista (posicion.x, posicion.y, direccion.x, direcciom.y, surface_bala_rotada):
                #Hay que cambiar la posicion con otra funcion para imprimir por pantalla
                self.lista_bala_jugador.append([posicion_bala_x, posicion_bala_y, projectile_dx*-1, projectile_dy*-1, surface_bala_rotada])

    def ImprimirBalas(self, pantalla, cantidad_zoom, camara_tupla):

        
        #Esta funcion solo cambia la posicion de la bala con la direccion y imprime por pantalla:
        for i in range(len(self.lista_bala_jugador)):
            #Añado camara y zoom al surface rotado:
            surface_bala_rotada = self.lista_bala_jugador[i][4]
            camara_x, camara_y = camara_tupla
            surface_ajustado_camara = pygame.transform.scale(surface_bala_rotada, (surface_bala_rotada.get_width()*cantidad_zoom, surface_bala_rotada.get_height()*cantidad_zoom))

            
            self.lista_bala_jugador[i][0] = self.lista_bala_jugador[i][0] + self.lista_bala_jugador[i][2] # direccion x
            self.lista_bala_jugador[i][1] = self.lista_bala_jugador[i][1] + self.lista_bala_jugador[i][3] # direccion y
            # imprimo
            posicionbala_x, posicionbala_y = (self.lista_bala_jugador[i][0]+camara_x)*cantidad_zoom, (self.lista_bala_jugador[i][1]+camara_y)*cantidad_zoom
            pantalla.blit(surface_ajustado_camara, (posicionbala_x, posicionbala_y))

    def EliminarBalasFuera(self, tamano_mapa):
        '''
        Esta funcion solo elimina las balas que salgan de 0 a 6400
        '''
        for i in range(len(self.lista_bala_jugador)):
            posbala_x = self.lista_bala_jugador[i][0]
            posbala_y = self.lista_bala_jugador[i][1]

            if posbala_x > tamano_mapa or posbala_x < 0:
                del self.lista_bala_jugador[i]
                break
            elif posbala_y > tamano_mapa or posbala_y < 0:
                del self.lista_bala_jugador[i]
                break

    def CrearSoldados(self):
        '''
        Esta funcion va a crear objetos Soldados y meterlos en nuestra lista los soldados van a aprecer alrededor
        de nuestra posicion y se spawnearan con la tecla "T"
        '''

        print("nuevo soldado")
        alreador_x, alreador_y = self.posjugador_x+randint(0, 30), self.posjugador_x+randint(0, 30)
        self.lista_soldados.append(Soldado((alreador_x, alreador_y)))


    
    def ObjetoSigueObjeto(self, posicion_cuadrado1, posicion_cuadrado2, espacio_mantener=30, velocidad=5):
        dx = posicion_cuadrado1[0] - posicion_cuadrado2[0]
        dy = posicion_cuadrado1[1] - posicion_cuadrado2[1]
        distancia = ((dx ** 2) + (dy ** 2)) ** 0.5
        if distancia > espacio_mantener:
            nuevasposx = int(posicion_cuadrado2[0] + dx * velocidad / distancia)
            nuevaposy = int(posicion_cuadrado2[1] + dy * velocidad / distancia)
            return (nuevasposx, nuevaposy)
        else:
            return None

    def MoverSoldadosFilaIndia(self, lista_objetos_soldados, distancia_mantener, distancia_mantener_1seccion):
        '''
        Esta funcion coge la lista de objetos de soldados y hace que los soldado se muevan en Fila india mateniendo una distancia
        '''
        if not len(lista_objetos_soldados) == 0:
            #no esta vacia
            soldado1_x, soldado1_y = self.lista_soldados[0].posjugador_x, self.lista_soldados[0].posjugador_y
            posicion_jugador = (self.posjugador_x, self.posjugador_y)
            posicion_soldado = (soldado1_x, soldado1_y)
            resultado = self.ObjetoSigueObjeto(posicion_jugador, posicion_soldado, 65, 5)

            if not resultado == None: # si no es none
                self.lista_soldados[0].posjugador_x, self.lista_soldados[0].posjugador_y = resultado

            for i in range(1, len(self.lista_soldados)):
                soldado = self.lista_soldados[i] #objeto soldado
                soldado1_x, soldado1_y = soldado.posjugador_x, soldado.posjugador_y
                posicion_soldado_siguiente = self.lista_soldados[i-1].posjugador_x, self.lista_soldados[i-1].posjugador_y
                posicion_soldado = soldado1_x, soldado1_y
                resultado = self.ObjetoSigueObjeto(posicion_soldado_siguiente, posicion_soldado, distancia_mantener, 5)
                if not resultado == None:
                    soldado.posjugador_x, soldado.posjugador_y = resultado # El soldado se le cambia la posicion
            


class Cliente(Host):
    def __init__(self, IP_Conectarse, Puerto, nombre_usuario, Es_Host=False):

        super().__init__(IP_Conectarse, Puerto, Es_Host)
        # Seccion sockets:

        #Eliminamos cosas que no necesitamos:
        del self.lista_clientes, self.lista_usuarios

        self.nombre_usuario = nombre_usuario
        self.enviando = False
        #Empiezo la conexion pidiendo de mi parte: yacimientos, arboles, balas y dando 3 veces mi posicion
        self.mensaje_tmp_para_enviar = [["LISTA_YACIMIENTOS", self.nombre_usuario], ["LISTA_ARBOLES", self.nombre_usuario], ["POS_JUGADOR", self.nombre_usuario, (jugador.posjugador_x, jugador.posjugador_y)], ["POS_JUGADOR", self.nombre_usuario,  (jugador.posjugador_x, jugador.posjugador_y)], ["POS_JUGADOR", self.nombre_usuario, (jugador.posjugador_x, jugador.posjugador_y)]]


    def PrimeraConexion(self):
        '''
        Esto es una funcion que enviara los datos como nombre_usuario al establecer conexion por primera vez:
        '''
        mensaje = self.socket.recv(2048)
        mensaje = mensaje.decode()
        mensaje_desencriptado = json.loads(mensaje)
        print("Mensaje recibido: " + str(mensaje_desencriptado))
        if mensaje_desencriptado[0] == "NOMBRE":
            lista_mensaje = ["LISTA_BALAS", self.nombre_usuario]

            lista_mensaje_encriptado = json.dumps(lista_mensaje)
            lista_mensaje_encriptado = lista_mensaje_encriptado.encode()


            time.sleep(0.1)
            print("Enviando nombre")
            self.socket.send(lista_mensaje_encriptado)
            time.sleep(0.1)
            #self.EnviarMensajeHost(self.mensaje, self.enviando)
            self.enviando = False
            self.recibiendo = True
            hilo_nueva_recibir = threading.Thread(target=self.RecibirMensajeHost,) # Creo hilo nuevo
            hilo_nueva_enviar = threading.Thread(target=self.EnviarMensajeHost, args=(self.mensaje_tmp_para_enviar,)) # Creo hilo nuevo

            hilo_nueva_enviar.start() # Inicio hilo
            hilo_nueva_recibir.start() # Inicio hilo

                
        else:
            mensaje = "hola servidor no te he entendido!"
            mensaje_encriptado = json.dumps(mensaje)
            mensaje_encriptado = mensaje_encriptado.encode()
            self.socket.send(mensaje_encriptado)

    def RecibirMensajeHost(self):
            #Ahora recibir mensaje de host:
            while True:
                try:
                    mensaje = self.socket.recv(4096)
                    if len(mensaje) > 0 :
                        mensaje = mensaje.decode()
                        mensaje_desencriptado = json.loads(mensaje)
                        print("Host dijo: " + str(mensaje_desencriptado[0]))
                        #print("Host dijo: " + str(mensaje_desencriptado[0][1])) #datos de la array
                        #Pintar en pantalla listas:
                        if mensaje_desencriptado[0][0] == "LISTA_ARBOLES":#Es la lista de arboles
                            self.lista_arboles = mensaje_desencriptado[1][0]
                        elif mensaje_desencriptado[0][0] == "LISTA_YACIMIENTOS":#Es la lista de yacimientos
                            self.lista_yacimiento_petroleo = mensaje_desencriptado[1][0]
                        elif mensaje_desencriptado[0][0] == "LISTA_BALAS":#Es la lista de balas
                            self.lista_balas_iconos = mensaje_desencriptado[1][0]
                        elif mensaje_desencriptado[0] == "DAME_POS_JUGADOR":#Es la lista de posjugador
                            #Toca darle pos jugador:
                            print("Enviando pos jugador:")
                            self.mensaje_tmp_para_enviar.append(["POS_JUGADOR", [jugador.posjugador_x, jugador.posjugador_y]])
                            self.enviando = True
                        else:
                            print("No entiendo el mensaje del server")
                        if len(self.mensaje_tmp_para_enviar) > 0:
                            print(self.mensaje_tmp_para_enviar[0][0])
                            print(self.mensaje_tmp_para_enviar)

                        self.enviando = True

                         # fin
                except ConnectionAbortedError as e:
                    print("Error: Connection aborted:", e)
                    # perform appropriate error handling such as closing the connection or reconnecting


    def EnviarMensajeHost(self, mensaje):
        #Ahora enviar mensajes al host:
        while True:
                try:
                    if len(self.mensaje_tmp_para_enviar) > 0:
                        
                        mensaje_encriptado = json.dumps(mensaje[0]) # el primero de la lista
                        mensaje_encriptado = mensaje_encriptado.encode()
                        print("Enviando con funcion enviar! esto: " + str(mensaje[0]))
                        self.socket.send(mensaje_encriptado)

                        time.sleep(1)
                        self.enviando = True
                        del self.mensaje_tmp_para_enviar[0] # el primero
                        #if len(self.mensaje_tmp_para_enviar) == 0:
                            #break # hora de apagar :)
                    else:
                        #No hay mensaje que enviar
                        time.sleep(0.2)
                    
                except ConnectionAbortedError as e:
                    print("Error: Connection aborted:", e)
                    # perform appropriate error handling such as closing the connection or reconnecting
                    break

    


    
    

            

        



                
jugador = Jugador()
jugador2 = Jugador()


juego = Cliente("192.168.1.106", 9001, "Roberto", False)
juego.PrimeraConexion()




juego.zoom_teclado()

juego.run()