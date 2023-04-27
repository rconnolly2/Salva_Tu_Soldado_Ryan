import socket
import pickle
import random
# Creamos el socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecemos el puerto y la dirección IP del servidor
puerto = 12345
direccion_ip = '192.168.1.104'

# Enlazamos el socket al puerto y dirección IP
servidor.bind((direccion_ip, puerto))

# Escuchamos conexiones entrantes
servidor.listen()

# Aceptamos la conexión entrante
cliente, direccion = servidor.accept()
print(f'Conexión entrante desde {direccion}')

# Creamos una lista para enviar al cliente
lista_elementos = ["usuario", []]

# Serializamos la lista con pickle
datos = pickle.dumps(lista_elementos)

# Enviamos los datos al cliente
cliente.send(datos)

# Cerramos la conexión
cliente.close()
servidor.close()
