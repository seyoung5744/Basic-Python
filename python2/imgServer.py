import os, time, socket, threading, sys

def upload(soc):
    data = soc.recv(1024)  # 파일명/크기
    data2 = data.decode()
    k = data2.split('/')
    f_name = k[0]  # 파일명
    f_size = int(k[1])  # 크기
    f = open('C:\\img\\' + f_name, 'wb')
    cnt=0
    while True:
        data = soc.recv(1024)
        if data:
            f.write(data)
            cnt+=1024
        else:
            break
    print('size:', f_size)

    f.close()


def server():
    HOST = '192.168.0.9'  # server ip
    PORT = 9999  # server port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    while True:
        client_socket, addr = server_socket.accept()
        upload(client_socket)
    soc.close()


t = threading.Thread(target=server, args=())
t.start()