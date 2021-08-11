# Task-3
Create Live Streaming Video Chat App without voice using cv2 module of Python
Socket Programming in Python Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at
an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server. They are the real backbones
behind web browsing. In simpler terms there is a server and a client.

Server :
A server has a bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port. A server has a listen() method which puts
the server into listen mode. This allows the server to listen to incoming connections. And last a server has an accept() and close() method. The accept method initiates a 
connection with the client and the close method closes the connection with the client

Simple Client
Let us write a very simple client program which opens a connection to a given port 12345 and given host. This is very simple to create a socket client using Python’s socket 
module function. The socket.connect(hosname, port ) opens a TCP connection to hostname on the port. Once you have a socket open, you can read from it like any IO object.
When done, remember to close it, as you would close a file.
