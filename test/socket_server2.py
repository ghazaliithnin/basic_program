#Imporimport random
import socket
from SocketServer import SocketServer
from threading import Thread
port = 6666
s = socket.socket()
print("Image socket server is created")

s.bind(("", port))

conn = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

buffer = []
cmd_buffer = []
ss = SocketServer(8080, 1, 1024, buffer, cmd_buffer)
#main_thread = Thread(target=ss.run)
#main_thread.start()
ss.run()
s.listen(30)
conn, addr = s.accept()
while True:
    message = conn.recv(1024).decode() #Gets the incomming message
    print(message)

    
