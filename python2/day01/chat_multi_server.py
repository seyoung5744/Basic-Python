import socket, threading

class Room:  #채팅방 클래스
    def __init__(self):
        self.clients = []

    def addClient(self, c):  # c : 텔레마케터. client 1명씩 전담하는 쓰레드
        self.clients.append(c)

    def delClient(self, c):
        self.clients.remove(c)

    def sendMsgAll(self, msg):  # 채팅방에 있는 모든 사람한테 메시지 전송
        for i in self.clients:
            i.sendMsg(msg)

class ChatClient : # 텔레마케터
    def __init__(self, room, soc):
        self.room = room  # 채팅방. Room 객체
        self.id = None  # 채팅방에 들어온 사람이 사용할 id
        self.soc = soc  # 사용자와 1:1 통신할 소켓

    def rendMsg(self):
        self.id = self.soc.recv(1024).decode()  # id 읽기, decode = 역 코드화 = 복호화

        self.room.sendMsgAll(self.id + "님이 입장하셨습니다")  # 모든 사람에게 msg 뿌리기

        while True :
            msg = self.soc.recv(1024).decode()  # 사용자가 전송한 메시지 읽음
            if msg == "/stop": # 종료 메시지이면 루프 종표
                self.soc.sendall(msg.encode())  # 이 메시지를 보낸 한명에게만 전송. encode = 코드화 = 암호화 (문자열을 바이트코드)
                self.room.delClient(self)
                break

            self.room.sendMsgAll(self.id + ': ' + msg)  # 모든 사람에게 msg 뿌리기

        self.room.sendMsgAll(self.id + "님이 퇴장하셨습니다.")

    def sendMsg(self, msg):
        self.soc.sendall(msg.encode(encoding="utf-8")) # 한글로 encode


class ChatServer:
    # class 변수 / static 변수
    ip = 'localhost'  # or 본인 ip or 127.0.0.1
    port = 5555

    def __init__(self):
        self.server_soc = None  # 서버 소켓(대문)
        self.room = Room()

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((ChatServer.ip, ChatServer.port))
        self.server_soc.listen()

    def run(self):
        self.open()
        print("서버 시작")
        while True:
            client_soc, addr = self.server_soc.accept()  # accept() : 클라 접속을 기다리다 수락
            print(addr, "접속")
            c = ChatClient(self.room, client_soc)
            self.room.addClient(c)  # 생성한 객체를 리스트에 추가
            th = threading.Thread(target=c.rendMsg())
            th.start()
        #self.server_soc.close()

def main():
    cs = ChatServer()
    cs.open()
    print("서버 시작")


main()
