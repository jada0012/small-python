import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'
#simple socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[new connection] {addr} connected")
    connected = True
    while connected:
        msg_len= conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}]{msg}")
            conn.send('message received'.encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f'[listening] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn, addr))
        thread.start()
        print(f"[Active connections] {threading.activeCount()-1}")

print('server is starting...')
start()