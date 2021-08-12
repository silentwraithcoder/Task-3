Socket Programming in Python
Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server.
They are the real backbones behind web browsing. In simpler terms there is a server and a client.
Sockets are the endpoints of a bidirectional communications channel. Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.
Sockets may be implemented over a number of different channel types: Unix domain sockets, TCP, UDP, and so on. The socket library provides specific classes for handling the common transports as well as a generic interface for handling the rest.
Server :
A server has a bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port. A server has a listen() method which puts the server into listen mode. This allows the server to listen to incoming connections. And last a server has an accept() and close() method. The accept method initiates a connection with the client and the close method closes the connection with the client
Simple Client
Let us write a very simple client program which opens a connection to a given port 12345 and given host. This is very simple to create a socket client using Python’s socket module function.
The socket.connect(hosname, port ) opens a TCP connection to hostname on the port. Once you have a socket open, you can read from it like any IO object. When done, remember to close it, as you would close a file.
Server Program-
import socket, cv2, pickle,struct
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(‘HOST IP:’,host_ip)
print(“\t\t\t\n=================================================”)
port = 9999
socket_address = (‘192.168.56.1’,port)
print(“Socket Created”)
print(“\t\t\t\n=================================================”)
server_socket.bind(socket_address)
print(“Socket Bind Successfully”)
print(“\t\t\t\n=================================================”)
server_socket.listen(5)
print(“LISTENING AT:”,socket_address)
print(“\t\t\t\n=================================================”)
print(“Socket Accept”)
print(“\t\t\t\n=================================================”)
while True:
client_socket,addr = server_socket.accept()
print(‘GOT CONNECTION FROM:’,addr)
if client_socket:
vid = cv2.VideoCapture(0)

while(vid.isOpened()):
img,frame = vid.read()
a = pickle.dumps(frame)
message = struct.pack(“Q”,len(a))+a
client_socket.sendall(message)


cv2.imshow(‘TRANSMITTING VIDEO’,frame)
key = cv2.waitKey(1) & 0xFF
if key ==ord(‘q’):
client_socket.close()
print(“Thank you guy’s”)
print(“\t\t\t\n=================================================”)


Client Program-
import socket,cv2, pickle,struct

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.1.4' 
port = 9999
print("Socket Created")
print("\t\t\t\n=================================================")

client_socket.connect((host_ip,port))
data = b""
payload_size = struct.calcsize("Q")
print("Socket Accept")
print("\t\t\t\n=================================================")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024) # 4K
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("RECEIVING VIDEO",frame)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'):
        break
client_socket.close()

print("Thank you guy's")
print("\t\t\t\n=================================================")
