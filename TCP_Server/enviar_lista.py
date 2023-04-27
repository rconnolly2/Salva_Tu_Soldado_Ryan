import socket
import pickle

# Creamos el socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecemos el puerto y la dirección IP del servidor
puerto = 12345
direccion_ip = '192.168.1.104'

# Conectamos al servidor
cliente.connect((direccion_ip, puerto))

# Recibimos los datos del servidor
datos = cliente.recv(4096)

# Deserializamos la lista con pickle
mi_lista = pickle.loads(datos)

# Imprimimos la lista recibida
print(mi_lista)
print(mi_lista[0][0] == "u")

# Cerramos la conexión
cliente.close()
