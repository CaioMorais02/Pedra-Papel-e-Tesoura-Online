import socket
from _thread import *
import sys

server = "192.168.56.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Esperando por uma conexão, Servidor Inicializado!")

def threaded_client(conn):
    conn.send(str.encode("Conectado"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Desconectado")
                break

            else:
                print("Recebido: ", reply)
                print("Enviando: ", reply)

            conn.sendall(str.encode(reply))
        
        except:
            break

    print("Conexão perdida")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Conectado a:", addr)

    start_new_thread(threaded_client, (conn,))