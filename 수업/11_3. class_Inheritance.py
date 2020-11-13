'''
상속
부모 클래스, 멤버 변수, 메서드
1. 코드 재사용성 향상
2. 다형성 구현 -> 하나의 코드가 실행할때마다 모양이 바뀌는...
'''
# 부모 클래스 : 하위 클래스들의 공통점을 추출하여 상위 클래스에 정의
class Parent:
    def __init__(self):
        self.x = 0
        self.y = 0
        print("parent의 생성자")

    def setData(self, x, y):
        self.x = x
        self.y = y

    def parentMethod(self):
        print("부모 메소드")

    def printXY(self):
        print('x:', self.x, ', y:', self.y)


# 하위 클래스
# 상속 방법 : 하위 클래스명(상위 클래스명)
class Child(Parent):
    def __init__(self):
        # 외부적으로는 자식 클래스 객체를 생성하지만 내부적으론 super()로 인해 부모 객체가 먼저 생성됨.
        super().__init__() # 부모 클래스의 생성자 호출. super() : 상속 관계에서 부모 객체 참조값 반환.
        self.z = 0
        print("child의 생성자")

    # 메소드 재정의 필요. 상속받은 메소드를 현재 클래스에 맞게 수정하여 사용
    def setZ(self, z):
        self.z = z

    def printZ(self):
        print('z:', self.z)

    def childMethod(self):
        print('자식 메소드')


def main():
    p = Parent()
    p.setData(1, 2)
    p.printXY()
    p.parentMethod()

    print('='*10)

    c = Child() # 멤버 변수 x, y, z
    c.setData(10, 20) # 부모에게 받은 메소드로 x, y set
    c.setZ(30)
    c.printXY() # 부모에게 받은 메소드로 x, y 출력
    c.printZ()
    c.parentMethod() # 부모의 private 빼고는 모두 상속받는다.
    c.childMethod()

main()

# 컴파일 방식은 번역한 결과를 파일로 저장함.
# 자바는 컴파일, 인터프리터 방식 둘다 사용됨. 플랫폼에 자유롭다 => 동일한 코드가 os가 바뀌어도 똑같이 동작함.
# 자바는 .class라는 파일로 저장함. 이 파일은 JVM에서 돌아가도록 하는 코드.

# c, c++의 경우 컴파일 환경이 바뀌면 안될 수도 있음.
# 파이썬은 실행할 때마다 번역하면서 실행됨. 인터프리터 방식

# 컴파일, 인터프리터 방식 공부하기

'''
객체를 정의하고 객체와 객체 사이의 관계 명시
관계
포함 : has a (소유) -> 다른 객체를 멤버, 변수 클래스 안에서 객체 생성
상속 : is a  (나 자신) -> 
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        print('(',self.x,', ',self.y,')')

# 도형. 삼각형, 사각형, 원...등을 상속해주기 위해 만든 클래스.
# 좌표를 갖는다. 그리는 동작
class Shape: # 상속을 목적으로 만든 클래스
    def __init__(self):
        self.points = [] # 포함 관계
        self.name = ''

    def draw(self):
        print(self.name, '을 그림')

class Triangle(Shape): # 상속 관계
    def __init__(self, p): # p : 좌표 3개를 담은 리스트
        super().__init__()
        self.name = '삼각형'
        for j in p:
            self.points.append(j)

    # 부모 클래스로부터 상속받은 현재 클래스에 적합하게 고쳐씀. 메소드 오버라이딩, 메소드 재정의
    def draw(self):
        super().draw() # 재정의 하기 이전 메소드 사용
        for p in self.points:
            p.printXY()

# 사각형 클래스
class Rectangle(Shape):  # 상속 관계
    def __init__(self, p):
        super().__init__()
        self.name = '사각형'
        for j in p:
            self.points.append(j)

    # 부모 클래스로부터 상속받은 현재 클래스에 적합하게 고쳐씀. 메소드 오버라이딩, 메소드 재정의
    def draw(self):
        super().draw()
        for p in self.points:
            p.printXY()

# 원 클래스
class Circle(Shape):  # 상속 관계
    def __init__(self, p, r):  # p : 좌표 3개를 담은 리스트
        super().__init__()
        self.name = '원'
        self.points.append(p)
        self.r = r

    # 부모 클래스로부터 상속받은 현재 클래스에 적합하게 고쳐씀. 메소드 오버라이딩, 메소드 재정의
    def draw(self):
        super().draw()
        print("중심점:")
        self.points[0].printXY()
        print('반지름:', self.r)

def main():
    s = Shape()
    s.draw() # 부모의 draw()를 호출

    t = Triangle([Point(1, 2), Point(3, 4), Point(5, 6)])
    t.draw() # 자식에서 재정의한 draw호출

    r = Rectangle([Point(10, 20), Point(30, 40)])
    r.draw() # 자식에서 재정의한 draw호출

    c = Circle(Point(100, 200), 150)
    c.draw() # 자식에서 재정의한 draw호출

main()







