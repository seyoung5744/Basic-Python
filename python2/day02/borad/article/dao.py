import pymysql
import day02.borad.article.vo as arti
import day02.borad.member.service as mem_serv

'''
 num=None, writer=None, w_date=None, title=None, content=None
'''
class Dao:
    def connect(self):
        return pymysql.connect(host='localhost', user='pythonUser', password='won9975744!', db='pythonTest', charset='utf8')

    def selectByNum(self, num):
        conn = self.connect()
        sql = 'select * from board where num=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, num)  # sql실행. 실행한 결과는 cursor 객체에 담아
        row = cursor.fetchone()#검색 결과 한줄추출
        conn.close()
        if row is not None:
            return arti.Board(row[0], row[1], row[2], row[3], row[4])

    def selectByTitle(self, title):
        conn = self.connect()
        sql = 'select * from board where title=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, title)  # sql실행. 실행한 결과는 cursor 객체에 담아
        row = cursor.fetchone()#검색 결과 한줄추출
        conn.close()
        if row is not None:
            return arti.Board(row[0], row[1], row[2], row[3], row[4])

    def selectByWriter(self, writer):
        conn = self.connect()
        sql = 'select * from board where writer=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, writer)  # sql실행. 실행한 결과는 cursor 객체에 담아
        articles = []
        for row in cursor:
            articles.append(arti.Board(row[0], row[1], row[2], row[3], row[4]))
        conn.close()
        return articles

    def selectAll(self):
        conn = self.connect()
        sql = 'select * from board'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:
            datas.append(arti.Board(row[0], row[1], row[2], row[3], row[4]))
        conn.close()
        return datas


    def insert(self, b):
        conn = self.connect()
        sql = 'insert into board(writer, w_date, title, content) values(%s, %s, %s, %s)'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        board = (b.writer, b.w_date, b.title, b.content)
        cursor.execute(sql, board)
        conn.commit()  # 쓰기 완료
        conn.close()

    def update(self, writer, title, content):# 수정할 제품번호와 새 가격을 Test 객체로 받아옴
        conn = self.connect()
        sql = 'update board set content=%s where writer=%s and title=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (content, writer, title)
        cursor.execute(sql, d)
        conn.commit()  # 쓰기 완료
        conn.close()

    def delete(self, num):
        conn = self.connect()
        sql = 'delete from board where num=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, num)
        conn.commit()  # 쓰기 완료
        conn.close()

