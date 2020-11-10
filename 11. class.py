'''
ex) 번호/이름/국/영/수/총/평

리스트
[['aaa',1,34,45,56,0,0],
['bbb',2,65,15,26,0,0],
['ccc',3,54,67,87,0,0]] => 이 방법은 이름 명시가 안되어 있어서 관리하기 불편.

클래스 : 타입 정의. 캡슐화(하나의 객체 정보를 하나로 묶음)
객체 : 프로그램으로 모델링할 때 구성 요소들(사람, 사물, 개념)

클래스는 사용자가 직접 정의하는 타입
변수를 만들려면 먼저 타입 정의가 필요

class 타입 이름:
    def 함수(self):
        self.a = 10
'''
# ex) 사람의 정보를 이름. 나이 3명
# 클래스 정의. 타입 정의. 타입 이름 : Person.
# 클래스는 멤버 변수와 멤버 함수로 구성
# 멤버 변수 : 객체 안의 변수.
# 멤버 함수 : 클래스 안에 정의한 함수. 첫 파라미터는 항상 self(객제 자신). 호출할 때 이 파라미터는 전달 안함

def func1(): # 클래스와 상관이 없는 전역 함수
    print("func1()")

class Person:
    # __init__(생성자, 함수) : 객체 생성 시 자동 생성. 객체 초기화.
    def __init__(self, name, age):
        self.name = name    # self.멤버변수이름
        self.age = age

    def printPerson(self): # 멤버함수
        print(self.name)
        print(self.age)

def main():
    p1 = Person('won',23) # 클래스로 변수 생성 => 객체
    print('name:',p1.name)
    print('age:',p1.age)
    p1.printPerson()
    print(p1)
    p2 = Person('bbb', 27)
    p2.printPerson()
    p3 = Person('ccc', 34)
    p3.printPerson()

main()

class Member: # 생성자 없는 클래스
    def setData(self, name, tel):
        self.name = name
        self.tel = tel

    def printMember(self):
        print('name:', self.name)
        print('tel:', self.tel)
def main2():
    m1 = Member() # 파라미터 없는 디폴트 생성자 사용
    m1.setData('aaa','111')
    print('m1.name:',m1.name)
    print('m1.tel:',m1.tel)
    m1.printMember()

    m2 = Member()
    m2.setData('bbb','222')
    print('m2.name:',m2.name)
    print('m2.tel',m2.tel)
    m2.printMember()

    m3 = m1 # 객체의 얕은 복사. 참조값 복사
    print('변경 전 m3 : ', end = ' ')
    m3.printMember()
    m1.name = 'abc'
    print('변경 후 m3 : ', end = ' ')
    m3.printMember()
    print('변경 후 m1 :', end = ' ')
    m1.printMember()

main2()

'''
성적 처리 프로그램 클래스 예제 (MVC 패턴 이용)
https://m.blog.naver.com/jhc9639/220967034588

Student(Vo : value object, Dto : data transfer object) : 값을 담는 객체 
Dao : 저장소에 데이터 추가, 검색 제공, 수정
https://jungwoon.github.io/common%20sense/2017/11/16/DAO-VO-DTO/
Service : 사용자에게 기능을 제공해주는 클래스

MVC
M : Model, 데이터,비지니스 로직
V : View, UI
C : Controller, 제어부

Model : Vo, Dao, Service
View : 웹, 어플...

ex) 웹 개발
model -> Java
view -> html, jsp, javascript, css
controller -> servlet

사용자가 view를 통해 데이터를 입력하면 
controller(클라이언트가 전송한 데이터와 명령어를 받아서 전체적인 프로그램 흐름 제어, 
spring을 통해 개발자가 신경쓰지 않도록 함. 요즘은 숨기는 추세)이 제일 먼저 받는다.
controller를 통한 명령어를 통해서 model에서 호출해서 실행

이때 db 작업을 구현한 클래스는 Dao(db query를 프로그램에서 실행시켜주는 클래스)
ex) 갑자기 db를 바꾸라고 하면 코드 전체를 수정하는 것이 아니라 Dao만 수정하면 됨.

콘솔에서 controller 역할은 메뉴

service는 controller이 명령한 것을 구현된 기능을 통해 dao한테 데이터 요청후 결과 값 리턴받음.

참고) 개발자는 SQL, PL SQL 정도만 알면 됨. 더 알면 더 좋은거구 예를들어 데이터마이닝 같은거 
'''

class Student: # 한 학생의 정보 및 성적처리. 캡슐화
    # 잘못된 코드
    # def __init...
    #   self.name[] = name => 이러한 코드는 객체지향적인 것이 아닌 순차적 형태 코드.
    # 객체는 객체로 다뤄야 함.
    def __init__(self, name, num, kor, eng, math):
        self.name = name
        self.num = num
        self.kor = kor
        self.eng = eng
        self.math = math

    def calc(self):
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3

    def printInfo(self):
        print('name:',self.name)
        print('num:', self.num)
        print('kor:', self.kor)
        print('eng:', self.eng)
        print('math:', self.math)
        print('total:', self.total)
        print('avg:', self.avg)
        print("="*10)

class Dao: # (Data access object) : DB 작업 전담 클래스
    # 저장소에 추가, 삭제, 수정 작업
    def __init__(self):
        self.datas = []

    def insert(self, s): # self.datas : 멤버변수(리스트)
        self.datas.append(s) # 파라미터로 받은 Student객체 s를 리스트(self.datas)에 추가

    def selectAll(self):
        return self.datas

class Service: # 비즈니스 로직 구현
    def __init__(self):
        self.dao = Dao()

    def addStudent(self): # 학생 정보 하나를 추가
        name = input('name:')
        num = int(input('num:'))
        kor = int(input('kor:'))
        eng = int(input('eng:'))
        math = int(input('math:'))
        s = Student(name,num,kor,eng,math) # 입력받은 값으로 Student 객체 생성
        s.calc()
        self.dao.insert(s)

    def printAll(self):
        all = self.dao.selectAll()
        for i in all:
            i.printInfo()

def main3():
    service = Service()
    service.addStudent()
    service.addStudent()
    service.addStudent()
    service.printAll()

main3()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPoint(self):
        print('(',self.x,',',self.y,')')


def main4():
    points = [Point(1,2), Point(3,4), Point(5,6)]
    # p1 = Point(1,2)
    # p2 = Point(3,4)
    # p3 = Point(5,6)
    # p1.printPoint()
    # p2.printPoint()
    # p3.printPoint()
    for point in points:
        point.printPoint()

main4()




