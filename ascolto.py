import socket

server_socket = socket.socket()
#host = '10.0.3.215'
host = '127.0.0.1'
port = 6364
server_socket.bind((host, port))
server_socket.listen(1)

f = open('logfile.txt', 'w')
f.write(f"Server listening on {host}:{port}\n")

for i in range(5):
    conn, addr = server_socket.accept()
    f.write(f"Connected by {addr}\n")
    ## apertura file in scrittura
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            richiesta = data.decode()
            risposta = f"Ho ricevuto il tuo messaggio: {richiesta}\n"
            f.write(risposta)
            conn.sendall(risposta.encode())
    finally:
        conn.close()

f.close()
server_socket.close()