import product.productDAO as dao
import product.productVO as prod

class Service:
    search_num = 0
    def __init__(self):
        self.dao = dao.Dao()

    # 제품명, 가격, 수량 입력받아 Product객체 생성 후 dao.insert()로 추가
    def addProduct(self):
        product_name = input("제품명:")
        product_price = int(input("제품 가격:"))
        product_amount = int(input("제품 수량:"))
        p = prod.Product(product_name, product_price, product_amount)
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
