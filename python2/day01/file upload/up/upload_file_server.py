# server
import socket
import os


class UploadServer:
    # class 변수 / static 변수
    ip = 'localhost'  # or 본인 ip or 127.0.0.1
    port = 5555

    def __init__(self, path):
        self.server_soc = None  # 서버 소켓(대문)
        self.client_soc = None  # 클라이언트와 1:1 통신 소켓
        self.path = path

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((UploadServer.ip, UploadServer.port))
        self.server_soc.listen()

    # 디렉토리가 없을 때만 생성
    def mkDir(self):
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def upload(self):
        """
               1. 파일명을 받아옴
               2. up 폴더에 받아온 파일명으로 파일 쓰기 모드로 오픈
               3. 파일 내용 받음
               4. 2번에서 오픈한 파일에 내용 복사
      