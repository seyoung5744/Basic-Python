import os

class LoginDao:

    def getMember(self, id):
        f = open(id + ".txt", "r", encoding="utf-8")
        str = f.read()
        f.close()
        return str

    def getMemberList(self):
        os.chdir('../data/login')
        g = os.listdir()
        print("현재 파일 리스트 : ", g)
        return g