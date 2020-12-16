import socket, threading

class UniClient:
    ip = 'localhost'  # or 본인 ip or 127.0.0.1
    port = 5555

    def __init__(self):
        self.client_soc = None

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((UniClient.ip, UniClient.port))

    def sendMsg(self):  # 키보드 입력받아 상대방에게 메시지 전송.
        while True:
            msg = input('msg:')
            data = msg.encode(encoding='utf-8')
            self.client_soc.sendall(data)
            if msg == '/stop':
                break

    def recvMsg(self):  # 상대방이 보낸 메시지 읽어서 화면에 출력
        while True:
            data = self.client_soc.recv(1024)
            msg = data.decode()
            print('상대방 메시지:', msg)
            if msg == '/stop':
                break

    def run(self):
        self.conn()
        th1 = threading.Thread(target=self.sendMsg)
        th1.start()
        th2 = threading.Thread(target=self.recvMsg)
        th2.start()

def main():
    c = UniClient()
    c.run()

main()