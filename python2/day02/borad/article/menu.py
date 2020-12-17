import day02.borad.article.service as serv

class ArtMenu:
    def __init__(self):
        self.service = serv.Service()

    def run(self, loginId):
        self.service.loginId = loginId
        while True:
            m = int(input('1. 글쓰기 2.글목록 3.글번호검색 4. 글 제목으로 검색 5.작성자로 글검색 6.글수정 7.글삭제 8.종료'))
            if m == 1:
                self.service.writeArticle()
            elif m == 2:
                self.service.showAllArticle()
            elif m == 3:
                self.service.showArticleByNum()
            elif m == 4:
                self.service.showArticleByTitle()
            elif m == 5:
                self.service.showArticleByWriter()
            elif m == 6:
                self.service.editArticle()
            elif m == 7:
                self.service.deleteArticle()
            elif m==8:
                break



