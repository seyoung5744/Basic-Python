import socket
import os


class UploadClient:
    ip = 'localhost'
    port = 5555

    def __init__(self):
        self.client_soc = None

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((UploadClient.ip, UploadClient.port))

    def run(self):
        self.conn()
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
            self.client_soc.sendall(f_name.encode(encoding='utf-8'))
            self.client_soc.sendall(f_content.encode(encoding='utf-8'))


def main():
    uc = UploadClient()
    uc.run()


main()
