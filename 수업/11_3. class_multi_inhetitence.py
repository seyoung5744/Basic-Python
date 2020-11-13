# class Parent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Child(Parent):
#     def __init__(self, name, age, hobby):
#         super().__init__(name, age) # 상속관계의 부모 클래스 생성자가 파라미터가 있으면 자식 클래스의 생성자에서 넣어줌
#         self.hobby = hobby
#
# def main():
#     c = Child('aaa', 12, '드럼')
#     print('c.name:', c.name, ", c.age:", c.age, ', c.hobby:', c.hobby)
#
# main()
#
# class A:
#     def methodA(self):
#         print('methodA')
#
# class B:
#     def methodB(self):
#         print('methodB')
#
# class C:
#     def methodC(self):
#         print('methodC')
#
# class D(A, B, C): # 다중상속
#     def methodD(self):
#         print('methodD')
#
# '''
# 생성자 : 멤버변수 정의
#
# class Test:
#     def a(self):
#         self.x = x
#     def b(self):
#         print(self.x)
#
# t = Test()
# t.a(10)
# t.b() # 정상적으로 될꺼 같지만
#
# 만약 순서를 뒤집으면?
#
# t.b()
# t.a(10) # 오류가 남. 그러므로 멤버변수는 생성자에서 생성하는게 안전함
# '''
# def main():
#     d = D()
#     d.methodA()
#     d.methodB()
#     d.methodC()
#     d.methodD()
#
# main()

class A:
    def __init__(self, a):
        self.a = a

    def methodA(self):
        print('methodA')

class B:
    def __init__(self, b):
        self.b = b

    def methodB(self):
        print('methodB')

class C:
    def __init__(self, c):
        self.c = c

    def methodC(self):
        print('methodC')

class D(A, B, C): # 다중상속
    def __init__(self, a, b, c, d):
        A.__init__(self, a) # 부모 A클래스의 생성자 호출
        B.__init__(self, b) # 부모 B클래스의 생성자 호출
        C.__init__(self, c) # 부모 C클래스의 생성자 호출
        self.d = d

    def methodD(self):
        print('methodD')
        print('a:', self.a)
        print('b:', self.b)
        print('c:', self.c)
        print('d:', self.d)

def main():
    d = D(1, 2, 3, 4)
    d.methodA()
    d.methodB()
    d.methodC()
    d.methodD()

main()