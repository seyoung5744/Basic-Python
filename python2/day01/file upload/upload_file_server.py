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
               5. 파일 닫기
        """
        f_name = self.client_soc.recv(1024).decode()  # 파일명
        f_content = self.client_soc.recv(1024).decode()  # 파일 내용

        # 이름 중복 테크하여 중복된 이름은 ~_1. 형태로 변경
        f_list = os.listdir(self.path)
        for i in f_list:
            if f_name == i:
                fName, fExtension = f_name.split('.')
                f_name = fName + '_1.' + fExtension

        f = open(self.path + '/' + f_name, 'w', encoding='utf-8')
        f.write(f_content)
        f.close()

    def download(self):
        print("다운로드")
        """
        1. 서버가 파일목록을 전송
        2. 클라이언트는 받은 파일 목록을 출력 => 파일 선택 => 번호 전송
        3. 서버는 파일 번호를 전송 받음 => 숫자 변환 => 리스트에서 파일명 뽑음
        4. 서버는 파일명과 파일 내용을 클라이언트에 전송
        5. 클라이언트는 파일명으로 파일 w모드로 오픈 및 내용 복사
        
        서버가 할 일 : 1, 3, 4
        클라이언트가 할 일 : 2, 5
        """
        f_list = os.listdir(self.path)
        s = ''
        for idx, i in enumerate(f_list):  # up 폴더의 파일 목록을 문자열 하나로 붙임
            s += str(idx) + '. ' + i + '\n'

        self.client_soc.sendall(s.encode(encoding='utf-8'))
        num = self.client_soc.recv(10).decode()  # num은 str
        num = int(num)

        # 클라이언트 측에서 잘못된 번호가 전송되었을 때
        err_flag = 'false'  # 에러 발생 여부를 표시
        if num < 0 or num >= len(f_list):
            err_flag = 'true'
        self.client_soc.sendall(err_flag.encode())  # 클라이언트는 err_flag가 정상이든 아니든 항상 대기하고 있으므로 무조건 전송은 해줘야 함.

        if err_flag == 'true':
            print("잘못된 번호로 다운도르 중단")
            return

        f_name = f_list[num]
        f = open(self.path + "/" + f_name, 'r', encoding='utf-8')
        f_content = f.read()
        f.close()

        # 파일명, 파일내용 전송
        self.client_soc.sendall(f_name.encode(encoding='utf-8'))
        self.client_soc.sendall(f_content.encode(encoding='utf-8'))

    def run(self):  # 메뉴
        self.open()
        self.mkDir()
        print("서버 오픈")
        self.client_soc, addr = self.server_soc.accept()
        while True:  # 클라이언트로부터 메뉴를 입력 받음
            m = self.client_soc.recv(10)
            m = m.decode()
            print("선택메뉴 : " , m)

            if m == '1':
                self.upload()
            elif m == '2':
                self.download()
            elif m == '3':
                break

        print("서버 종료")
        self.client_soc.close()
        self.server_soc.close()


def main():
    up = UploadServer('up')
    up.run()


main()
