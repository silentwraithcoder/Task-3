# this is Server Page 
# import library
import cv2
import socket
import pickle
import struct
# create Socket 
try:
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created ...")
except socket.error as err:
    print("Socket creation failed with error {}".formatat(err))
# main Program Block
# Bind the port no and ipAddres
port = 1235
skt.bind(("", port))
skt.listen()
print("Socket is listening......")
try:
    while True:
        session, address = skt.accept()
        print("Connected to : ",address)
        if session:
            cam = cv2.VideoCapture(0)
            while(cam.isOpened()):
                ret, img = cam.read()
                data = pickle.dumps(img)
                msg = struct.pack("Q", len(data))+ data
                session.sendall(msg)
                cv2.imshow("Transmitting video...",img)
                if cv2.waitKey(1) == 13:
                    cv2.destroyAllWindows()
                    session.close()
                    break
except:
    cv2.destroyAllWindows()
    session.close()
