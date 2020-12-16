import day02.borad.member.dao as memberDao
import day02.borad.member.vo as vo

''' 1.회원가입 2.3.4.5.'''
class Service:
    loginId = None # 로그인한 사람의 아이디.

    def __init__(self):
        self.dao = memberDao.Dao()

    def join(self):
        print('회원가입')
        while True:
            id = input('id:')
            m = self.dao.select(id)
            if m==None: # 중복된지 않은 id
                break
            else:
                print("중복된 아이디. 다시 입력하시오")
        pwd = input('pwd:')
        name = input('name:')
        email = input('email:')
        self.dao.insert(vo.Member(id, pwd, name, email))

    def login(self):
        id = input('id:')
        m = self.dao.select(id)
        if m==None:
            print("없는 아이디")
        else:
            pwd = input("pwd:")
            if m.pwd == pwd:
                print("로그인 성공")
                Service.loginId = id
            else:
                print("패스워드 불일치")


    def loginCheck(self)->bool:
        if Service.loginId == None:
            print("로그인 먼저")
            return False    # 로그인이 안된 상태
        else:
            return True     # 로그인이 된 상태

    def logout(self):
        flag = self.loginCheck()
        if flag:
            Service.loginId = None

    def editInfo(self):
        flag = self.loginCheck()
        if flag:
            pwd = input('new pwd:')
            self.dao.update(Service.loginId, pwd)

    # 회원탈퇴
    def out(self):
        flag = self.loginCheck()
        if flag:
            self.dao.delete(Service.loginId)

    def showInfo(self):
        flag = self.loginCheck()
        if flag:
            member = self.dao.select(Service.loginId)
            print(member)