import socket

UDP_IP_ADDRESS = '192.168.122.90'
UDP_PORT = 5050

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind(((UDP_IP_ADDRESS,UDP_PORT)))
filename='server2.jpg'
fp = open(filename,'wb+')
count=0
while True:
    data, addr = serverSock.recvfrom(1024)
    count=count+len(data)
    print(addr," blok ", count,"panjang : ",len(data), data)
    fp.write(data)

# while True:
#     data,addr = serverSock.recvfrom(1024)
#     print("Message: ", data.decode())
