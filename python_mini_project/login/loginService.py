import python_mini_project.login.loginDao as ld
class LoginService:
    def __init__(self):
        self.dao = ld.LoginDao()

    def getMember(self, id):
        member = self.dao.getMember(id)
        return member

    def getMemberList(self):
        return self.dao.getMemberList()