import socket ,cv2


HOST =  "192.168.29.203"  # The server's hostname or IP address
PORT=2020

s=socket.socket()
s.connect((HOST, PORT))

cap = cv2.VideoCapture(1) # check this

while True:

    ret, photo = cap.read()

    cv2.imwrite('csimg.jpg',photo)

    file = open('csimg.jpg', 'rb')

    data = file.read(122880)

    file.close()

    if not (data):
        break

    s.sendall(data)

    file = open('crimg.jpg', "wb")

    data = s.recv(122880)

    if not (data):
        break
    file.write(data)

    file.close()

    photo=cv2.imread('crimg.jpg')

    cv2.imshow("client side", photo)

    if cv2.waitKey(10) == 13:
        break

cv2.destroyAllWindows()
s.close()
