
# https://www.youtube.com/watch?v=_k-E5GbOeQg&t=601s

# Socket Tutorial P.2 -- Communicating Between A Windows C# Client And A Python Server by Lime Parallelogram

#Imports modules
import socket

listensocket = socket.socket() #Creates an instance of socket
Port = 7777 #Port to host server on
maxConnections = 999 # last one 30
IP = socket.gethostname() #IP address of local machine

listensocket.bind(('',Port))

#Starts server
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

#Accepts the incomming connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")


while True:
    message = clientsocket.recv(1024).decode() #Gets the incomming message
    print(message)
