import socket, threading
import client_handler
address = ('localhost', 6543)
server = socket.socket()
server.bind(address)
server.listen(10)
while True:
    client, addr = server.accept()
    p = threading.Thread(target=client_handler.handler, args=(client, addr))
    p.start()
