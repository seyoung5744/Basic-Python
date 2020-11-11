# 주석 : 프로그램을 설명. 프로그램 실행에는 영향은 안줌.
# 변수 정의
# 파이썬은 참고 값이 저정됨.
a = 3  # '=' : 대입연산
b = 'qwer'
c = 'abc'
d = 3.14
e = True

# 변수 출력
print('a : ', a)
print('b : ', b)
print('c : ', c)
print('d : ', d)
print('e : ', e)

# 4. 타입 = 값의 형태(정수, 실수, 문자열, 참거짓(불린)
# int : 정수타입
# float : 실수타입
# str : 문자열타입
# bool : 참거짓타입

print('a : ', type(a))
print('b : ', type(b))
print('c : ', type(c))
print('d : ', type(d))
print('e : ', type(e))

'''
5. 주석
주석은 프로그램에 설명작성. 프로그램 실행 시 영향 안줌
#은 한줄 주석. ''' ''' 은 여러 줄 주석
'''

'''
6. 가비지 컬렉터
프로그램에서 사용되지 않는 값을 찾아서 자동으로 메모리 반
(파이썬은 모두 객체타입이다.)
스레드의 우선 순위를 매우 낮추고 평소에는 동작하지 않고 있다가 필요 상황이 오면 동작

del 변수명   # 변수 삭제

a = False
print('a=',a, 'type=',type(a))

del a   # 변수 afmf tkrwp
print(a)   # 여기서 에러발생
'''

#예제
a = 10
b = 20

print(a)
print(b)

del b

print(a)
#print(b)

print('\n\n\n')
# 연산자
a = 3
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)


