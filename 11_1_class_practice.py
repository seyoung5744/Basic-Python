'''
Product
제품번호/제품명/가격/수량

메뉴
추가
검색 (번호로)
수정
삭제
전제목록
'''

class Product:
    num = -1 # 클래스 변수. 제품의 객수 카운팅
    def __init__(self, name, price, product_amount): #
        Product.num += 1
        self.serial_num = Product.num
        self.name = name
        self.price = price
        self.product_amount = product_amount

    def printProduct(self):
        print("Serial Number:", self.serial_num)
        print("Product Name:", self.name)
        print("Price:",self.price)
        print("Product Amount:",self.product_amount)
        print("="*10)

    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        return self.price

class Dao: # 저장소 저장, 검색, 수정, 삭제
    def __init__(self):
        self.prod = []

    # p는 서비스에서 제품명, 가격, 수량을 입력받아 Product 객체를 생성해서
    # 이 메서드에 파라미터로 넣어서 호출
    def insert(self, p):
        self.prod.append(p)

    def select(self, num): # 제품 번호 반환
        for idx, p in enumerate(self.prod) :
            if num == p.serial_num:
                return idx

    def getProduct(self, idx):
        return self.prod[idx]

    def delete(self, num):
        for p in self.prod:
            if num == p.serial_num:
                self.prod.remove(p)

    def update(self, serial, price): # 제품 가격만 수정
        for p in self.prod:
            if serial == p.serial_num:
                p.price = price

    def selectAll(self):
        return self.prod

class Service:
    search_num = 0
    def __init__(self):
        self.dao = Dao()

    # 제품명, 가격, 수량 입력받아 Product객체 생성 후 dao.insert()로 추가
    def addProduct(self):
        product_name = input("제품명:")
        product_price = int(input("제품 가격:"))
        product_amount = int(input("제품 수량:"))
        p = Product(product_name, product_price, product_amount)
        self.dao.insert(p)

    # 검색할 번호 입력받아 dao.select()로 검색
    def getProduct(self):
        search_num = int(input("검색할 제품 번호 입력 : "))
        serial = self.dao.select(search_num)
        if serial is not None:
            self.dao.getProduct(serial).printProduct()
        else :
            print("해당 제품이 없습니다.")


    # 삭제할 제품 번호 입력받아 dao.delete()로 삭제
    def deleteProduct(self):
        search_num = int(input("삭제할 제품 번호 입력 : "))
        # 제품이 존재하는지 검사. 제품이 있으면 인덱스 반환, 없으면 None 반환
        if self.dao.select(search_num) is not None:
            self.dao.delete(search_num)
            print("삭제 완료")
        else :
            print("해당 제품이 없습니다.")

    # 수정할 제품 번호와 새 가격 입력받아 dao.update()로 수정
    def editProduct(self):
        search_num = int(input("수정할 제품 번호 입력 : "))
        # 제품이 존재하는지 검사. 제품이 있으면 인덱스 반환, 없으면 None 반환
        if self.dao.select(search_num) is not None:
            product_price = int(input("제품 가격:"))
            self.dao.update(search_num, product_price)
        else:
            print("해당 제품이 없습니다.")

    # dao.selectAll()로 전체 검색한 결과 출력
    def printAll(self):
        all = self.dao.selectAll()
        for i in all:
            i.printProduct()

class Menu:
    def __init__(self):
        self.service = Service()

    def run(self):
        while True:
            x = int(input('1.제품추가 2.제품검색 3.제품수정 4.제품삭제 5.전체목록 6.종료'))
            if x==1:
                self.service.addProduct()
            elif x==2:
                self.service.getProduct()
            elif x==3:
                self.service.editProduct()
            elif x==4:
                self.service.deleteProduct()
            elif x==5:
                self.service.printAll()
            elif x==6:
                break

def main():
    m = Menu()
    m.run()

main()