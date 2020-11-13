'''
클래스 변수, 클래스 함수
'''
class Test:
    # 모든 객체가 공유, 클래스 이름.변수면
    x = 0 # 클래스 변수. 자바의 static 변수와 비슷<객체 소속이 아니라 클래스 소속>
    def __init__(self):
        self.y = 0 # 멤버 변수. 객체 마다 생성되는 변수. 객체이름.변수명
        z = 0   # 지역변수. 이 함수가 끝나면 사라짐.

    @staticmethod # 이노테이션 : 설명
    def printNum(r): # 클래스 메서드. 멤버 변수 사용 없고, <객체 소속이 아니라 클래스 소속>
        print('정적 메소드')
        PI = 3.14
        w = r*r*PI
        print('원의 넓이 : ',w)

def main():
    Test.printNum(5)
    t1 = Test()
    Test.x += 1
    t1.y +=1
    print('x:',Test.x,', y:',t1.y)

    t2 = Test()
    Test.x += 1
    t2.y += 1
    print('x:', Test.x, ', y:', t2.y)

    t3 = Test()
    Test.x += 1
    t3.y += 1
    print('x:', Test.x, ', y:', t3.y)

main()

'''
접근 지정자
'''

class Test2:
    def __init__(self, x, y):
        self.x = x      # public : 클래스 밖에서 직접 접근 가능
        self.__y = y    # private(__Variable) : 클래스 밖에서 직접 접근 불가능

    def printXY(self):
        print('x:', self.x, ', y:', self.__y)

    # setter : private 멤버를 외부에서 값을 넣을(set) 수 있게 하는 메서드
    def setY(self, y):
        self.__y = y

    # getter : private 멤버를 외부에서 값을 읽을(get) 수 있게 하는 메서드
    def getY(self):
        return self.__y

def main2():
    t1 = Test2(10, 20)
    t1.printXY()
    print('t1.x:', t1.x)
    print('t1.y:', t1.getY())
    print('t1.y:', t1.__y) # 에러발생
main2()