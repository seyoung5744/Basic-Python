import day02.borad.article.dao as articleDao
import day02.borad.article.vo as vo
import day02.borad.member.service as mem_serv

'''
2. 게시판(로그인 상태에서만 사용가능)(vo, dao, service)
  =>1. 글쓰기 2.글목록 3.글번호검색 4. 글 제목으로 검색 5.작성자로 글검색 6.글수정 7.글삭제
'''


class Service:
    def __init__(self):
        self.dao = articleDao.Dao()
        self.Borad = vo.Board()
        self.memberService = mem_serv.Service()

    def writeArticle(self):
        loginId = mem_serv.Service.loginId
        flag = self.memberService.loginCheck()
        if flag:
            print("글쓰기")
            title = input('title:')
            content = input('content:')
            w_date = input('w_date')
            self.dao.insert(vo.Board(0, loginId, w_date, title, content))

    def showAllArticle(self):
        articles = self.dao.selectAll()
        for i in articles:
            print(i)

    def showArticleByNum(self):
        self.showAllArticle()
        num = int(input("\n출력할 번호 입력:"))
        print(self.dao.selectByNum(num))

    def showArticleByTitle(self):
        self.showAllArticle()
        title = input("\n검색할 제목 입력")
        print(self.dao.selectByTitle(title))

    def showArticleByWriter(self):
        self.showAllArticle()
        writer = input("\n검색할 작가 입력")
        articles = self.dao.selectByWriter(writer)
        for i in articles:
            print(i)

    def editArticle(self):
        flag = self.memberService.loginCheck()
        loginId = mem_serv.Service.loginId
        if flag:
            print("수정 가능한 글 목룍")
            self.showAllArticle()

            title = input('수정할 글 제목 입력:')
            content = input('content:')
            self.dao.update(loginId , title, content)

    def deleteArticle(self):
        flag = self.memberService.loginCheck()
        loginId = mem_serv.Service.loginId
        if flag:
            print("삭제 가능한 글 목룍")
            self.showAllArticle()

            num = int(input("삭제할 번호 입력"))
            self.dao.delete(num)
