import socket
import threading
import pickle

HOST = "192.168.1.104"
PUERTO = 9000

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind((HOST, PUERTO)) #Asignamos direccion y puerto de nuestro servidor

socket_server.listen(5)

clientes = []
nombres_usuarios = []

def Broadcast(mensaje):
    for cliente in clientes:
        cliente.send(mensaje) #Enviara un mensaje a cada cliente. Broadcast => Lo escuchan todos


def Manejar_Conexion(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024)
            nombre_usuario = pickle.loads(mensaje)
            Broadcast(nombre_usuario)
        except:
            index_cliente = clientes.index(cliente) # Cojemos el index de la lista clientes
            clientes.remove(cliente)
            cliente.close()
            nombre_usuario = nombres_usuarios[index_cliente]
            Broadcast(pickle.dumps((str(nombre_usuario) + " abandono el chat")))
            nombres_usuarios.remove(nombre_usuario)
            break

def Recibir():
    while True:
        cliente, direccion = socket_server.accept()
        print("Conectado con direccion: " + str(direccion))
        usuario = pickle.dumps("USUARIO")
        cliente.send(usuario)
        nombre_usuario = cliente.recv(1024)
        nombre_usuario = pickle.loads(nombre_usuario)
        nombres_usuarios.append(nombre_usuario)
        clientes.append(cliente)

        print("Hemos añadido nombre usuario: " + str(nombre_usuario))
        Broadcast(pickle.dumps("Nombre de usuario añadido a la partida : " + str(nombre_usuario)))
        cliente.send(pickle.dumps("Conectado al servidor !"))

        hilo = threading.Thread(target=Manejar_Conexion, args=(cliente,))
        hilo.start()

print("Servidor esta escuchando!")
Recibir()