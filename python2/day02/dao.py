import pymysql
#vo(value object)=dto(data transefer object)
class Test:
    def __init__(self, num=None, name=None, price=None, disc=None):
        self.num = num
        self.name = name
        self.price = price
        self.disc = disc

    def __str__(self):#
        return 'num:'+str(self.num)+' / name:'+self.name+' / price:'+str(self.price)+' / disc:'+self.disc

class Dao:
    def connect(self):
        return pymysql.connect(host='localhost', user='pythonUser', password='won9975744!', db='pythonTest', charset='utf8')

    def select(self, num):
        conn = self.connect()
        sql = 'select * from test where num=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, num)  # sql실행. 실행한 결과는 cursor 객체에 담아
        row = cursor.fetchone()#검색 결과 한줄추출
        conn.close()
        if row != None:
            return Test(row[0], row[1], row[2], row[3])

    def selectAll(self):
        conn = self.connect()
        sql = 'select * from test'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql)  # sql실행. 실행한 결과는 cursor 객체에 담아
        datas = []
        for row in cursor:  # 검색된 결과를 한 줄씩 추출
            datas.append(Test(row[0], row[1], row[2], row[3]))
        conn.close()
        return datas

    def insert(self, t):
        conn = self.connect()
        sql = 'insert into test(name, price, disc) values(%s, %s, %s)'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (t.name, t.price, t.disc)
        cursor.execute(sql, d)
        conn.commit()  # 쓰기 완료
        conn.close()

    def update(self, t):# 수정할 제품번호와 새 가격을 Test 객체로 받아옴
        conn = self.connect()
        sql = 'update test set price=%s where num=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        d = (t.price, t.num)
        cursor.execute(sql, d)
        conn.commit()  # 쓰기 완료
        conn.close()

    def delete(self, num):
        conn = self.connect()
        sql = 'delete from test where num=%s'
        cursor = conn.cursor()  # 사용할 커서 객체 생성
        cursor.execute(sql, num)
        conn.commit()  # 쓰기 완료
        conn.close()

class Service:
    def __init__(self):
        self.dao = Dao()

    def addProduct(self):
        print('제품추가')
        name = input('name:')
        price = int(input('price:'))
        disc = input('describe:')
        self.dao.insert(Test(0, name, price, disc))

    def getProduct(self):
        print('제품검색')
        num = int(input('검색할 제품 번호:'))
        p = self.dao.select(num)
        if p==None:
            print('없는 제품 번호')
        else:
            print(p)

    def getAll(self):
        print('전체검색')
        datas = self.dao.selectAll()
        for i in datas:
            print(i)

    def editProduct(self):
        print('제품수정')
        num = int(input('수정할 제품 번호:'))
        p = self.dao.select(num)
        if p == None:
            print('없는 제품 번호. 수정취소')
        else:
            price = int(input('new price:'))
            self.dao.update(Test(num, '', price, ''))

    def delProduct(self):
        print('제품삭제')
        num = int(input('삭제할 제품 번호:'))
        p = self.dao.select(num)
        if p == None:
            print('없는 제품 번호. 삭제취소')
        else:
            self.dao.delete(num)

def main():
    service = Service()
    service.addProduct()
    service.addProduct()
    service.getAll()
    service.editProduct()
    service.editProduct()
    service.getProduct()
    service.delProduct()

main()