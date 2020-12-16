import socket

HOST = '192.168.200.150'  #server ip. localhost. or  127.0.0.1. cmd-ipconfig
PORT = 9999         #server port. 프로그램을 구분하는 유일한 번호.

# 서버 소켓 오픈. 클라이언트 맞기 위해서 큰 대문을 열어두는 것.
#server socket open. socket.AF_INET:주소체계(IPV4), socket.SOCK_STREAM:tcp 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#포트 여러번 바인드하면 발생하는 에러 방지
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#바인드:오픈한 소켓에 IP와 PORT 할당
server_socket.bind((HOST, PORT))

#이제 accept할 수 있음을 알림
server_socket.listen()

print('server start')

#accept로 client의 접속을 기다리다 요청시 처리.
#client와 1:1통신할 작은 소켓과 연결된 상대방의 주소 반환
client_socket, addr = server_socket.accept()

print('Connected by', addr)

while True:
    data = client_socket.recv(1024)
    msg = data.decode()
    print('Received from', addr, msg)
    client_socket.sendall(data)
    if msg=='/stop':
        break

client_socket.close()
server_socket.close()
