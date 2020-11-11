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