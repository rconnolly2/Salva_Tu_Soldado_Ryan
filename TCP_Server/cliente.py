import socket
import threading
import pickle
nombre_usuario = input("Dame el nombre de usuarios que deseas")
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("192.168.1.104", 9000))


def Reicibir():
    while True:
        try:
            mensaje = socket_cliente.recv(1024)
            mensaje = pickle.loads(mensaje)

            if mensaje == "USUARIO":
                socket_cliente.send(pickle.dumps(nombre_usuario))
            else:
                print(mensaje)

        except:
            print("A occurrido un error!")
            socket_cliente.close()
            break


def Escribir():
    while True:
        mensaje = (str(nombre_usuario) + ": " + input(""))
        mensaje = pickle.dumps(mensaje)
        socket_cliente.send(mensaje)

hilo_recibir = threading.Thread(target=Reicibir)
hilo_enviar = threading.Thread(target=Escribir)

hilo_recibir.start()
hilo_enviar.start()