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
