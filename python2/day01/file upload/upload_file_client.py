import socket
import os


class UploadClient:
    ip = 'localhost'
    port = 5555

    def __init__(self, path):
        self.client_soc = None
        self.path = path

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((UploadClient.ip, UploadClient.port))

        # 디렉토리가 없을 때만 생성
    def mkDir(self):
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def upload(self):
        f_list = os.listdir('/')  # 현재 디렉토리 파일 목록 가져오기
        print("파일 목록")
        for idx, i in enumerate(f_list):
            print(idx, ', ', i)

        num = int(input("업로드할 파일의 번호를 입력하시오"))
        if 0 <= num < len(f_list):
            f_name = f_list[num]
            f = open(f_name, 'r', encoding='utf-8')
            f_content = f.read()
            f.close()
            self.client_soc.sendall(f_name.encode(encoding='utf-8'))  # 파일명 서버 전송
            self.client_soc.sendall(f_content.encode(encoding='utf-8'))  # 파일내용 서버 전송

    def download(self):
        f_list = self.client_soc.recv(1024).decode()
        print('파일목록')
        print(f_list)
        num = input('다운로드할 파일의 번호를 입력하시오.')
        self.client_soc.sendall(num.encode())
        err_flag = self.client_soc.recv(20).decode()
        if err_flag == 'true':
            print("잘못된 번호 입력으로 다운로드 중단")
            return

        f_name = self.client_soc.recv(500).decode()
        f_content = self.client_soc.recv(1024).decode()

        # 이름 중복 테크하여 중복된 이름은 ~_1. 형태로 변경
        f_list = os.listdir(self.path)
        for i in f_list:
            if f_name == i:
                s = f_name.split('.')  # s[0]:파일명, s[1]:확장자
                f_name = s[0] + '_1.' + s[1]

        f = open(self.path + '/' + f_name, 'w', encoding='utf-8')
        f.write(f_content)
        f.close()

    def run(self):
        self.conn()
        self.mkDir()
        while True:
            m = input("1.업로드 2.다운로드 3.종료")
            self.client_soc.sendall(m.encode())  # 선택한 메뉴를 서버로 전송

            if m == '1':
                self.upload()
            elif m == '2':
                self.download()
            elif m == '3':
                break


def main():
    uc = UploadClient('down')
    uc.run()


main()
