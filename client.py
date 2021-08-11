# this is Client Page 
# import library
import cv2
import socket
import pickle
import struct
# create Socket
try:
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created Now Show ...")
except socket.error as err:
    print("Socket creation failed with error {}".formatat(err))
# main Program Block
port = 1234
server_ip = "192.168.56.1"
skt.connect((server_ip,port))
data = b""
payload_size = struct.calcsize("Q")
try:
    while True:
        while len(data) < payload_size:
            packet = skt.recv(4*1024)
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size =  struct.unpack("Q",packed_msg_size)[0]

        while len(data) < msg_size:
            data+= skt.recv(4*1024)
        img_data = data[:msg_size]
        data = data[msg_size:]
        img = pickle.loads(img_data)
        cv2.imshow("Recieving video", img)
        if cv2.waitKey(10) == 13:
            cv2.destroyAllWindows()
            break
    skt.close()
except:
    cv2.destroyAllWindows()
    skt.close()
