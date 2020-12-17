import day02.borad.member.service as serv

class MemMenu:
    def __init__(self):
        self.service = serv.Service()

    def run(self):
        while True:
            m = int(input('1.가입 2.로그인 3.로그아웃 4.내정보수정 5.탈퇴 6.종료'))
            if m == 1:
                self.service.join()
            elif m == 2:
                self.service.login()
            elif m == 3:
                self.service.logout()
            elif m == 4:
                self.service.showInfo()
                self.service.editInfo()
            elif m == 5:
                self.service.out()
            elif m == 6:
                break

    def loginCheck(self):
        if self.service.loginId==None:
            return (False,)
        else:
            return True, self.service.loginId



