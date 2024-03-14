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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tupla):
    return str(tupla[0]) + "," + str(tupla[1])

pos = [(0, 0), (100, 100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Desconectado")
                break

            else:
                if player == 1:
                   reply = pos[0]
                else:
                    reply = pos[1] 

                print("Recebido: ", data)
                print("Enviando: ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        
        except:
            break

    print("Conexão perdida")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Conectado a:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1