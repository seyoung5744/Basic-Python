'''
1. 함수
함수는 코드를 기능 단위로 끊어 프로그램의 모듈화를 가능하게 한다.
즉 반복적으로 등장하는 코드를 함수로 정의하고 이를 필요할 때마다 호출하여 사용.

함수 정의
함수가 어떻게 동작할 지 정의한다. 파라미터는 함수가 호출될 때 외부로부터 필요한 값을 받아오는 변수를 말한다.
반환값을 함수가 작업을 마친 뒤 반환하는 값을 말한다.

함수 정의 : 이 함수는 이러하게 동작한다. 함수 수식을 작성
함수 호출 : 정의한 함수를 불러서(이름) 그 함수를 실행시킴 => 분기(함수코드)
'''
def fun1() :

    # 파라미터 없음. 반환값 없음
    # 파라미터 : 함수가 동작할 때 필요한 값을 받아올 변수로 함수이름 옆의 괄호에 나열한다.
    # 반환값(리턴값) : 함수의 결과물을 호출한 쪽으로 던져줌
    # :return:

    print("hello function")

def fun2(a, b) : # 2개의 파라미터를 갖는다.
    print(a, ' + ', b, ' = ', a+b) # 파라미터로 받은 2개의 값을 더해서 출력
    # 리턴값이 없음.

def fun3(a, b) :
    return a + b # return : 1. 함수 종료 2. 값 반환

fun1() # 파타미터가 없기 때문에 호출할 때도 괄호에 아무것도 안넣음
fun2(1,2)
result = fun3(3,4)
print('result:',result)

# 함수를 이용한 계산기 (+, -, *, /)
# 숫자 2개 입력 받기

def add(a, b):
    return a + b
def sub(a, b) :
    return a - b
def mul(a, b) :
    if b == 0 :
        print('0으로 나눌 수 없습니다.')
        return None
    return a * b
def div(a, b) :
    return a / b

while True :
    menu = int(input('1.add 2.sub 3.mul 4.div 5.stop : '))

    if 1 <= menu <= 4:
        num1 = int(input('num1:'))
        num2 = int(input('num2:'))

    result = 0
    if menu == 1:
        result = add(num1, num2)
    elif menu == 2:
        result = sub(num1, num2)
    elif menu == 3:
        result = mul(num1, num2)
    elif menu == 4:
        result = div(num1, num2)
    elif menu == 5 :
        print('프로그램 종료')
        break
    else :
        print('잘못된 메뉴')
        result = None # None : 값이 없음을 나타내는 상수

    if result is not None: # result != None
        print('result:',result)


# 구구단
# 단수를 파라미터로 받아서한단만 출력하는 함수 정의 및 호출

def gugudan(dan) :
    for i in range(1, 10) :
        print(dan,'*',i,'=',i*dan)

dan = int(input('단수(1-9)를 입력하시오. '))

if 1<=dan<=9:
    gugudan(dan)
else :
    print('잘못된 입력')

# 약수 구하기
def aliquot1(num) :
    for i in range(1, num + 1) :
        if num % i == 0:
            print(i, end=',')

aliquot1(10)
print()

def aliquot2(num):
    res = []
    for i in range(1, num + 1) :
        if num % i == 0 :
            res.append(i)
    return res

print(aliquot2(25))


# 다양한 형태의 함수들
# 함수안에 코드를 다 실행하면 함수는 종료.
# return 함수 종료

def f1():
    print('파라미터 없고 리턴값도 없다.')

def f0(num) :
    if num % 2 == 0 :
        return # 함수 종료
    else :
        print(num)

def f2(num) : # 파라미터의 타입이 고정되지 않기 때문에 어떤 값을 전달해도 받을 수 있음.
    # 하지만 함수 안에서 실행 시 헤러 발생할 수 있음

    if isinstance(num, int) : # num의 값이 int인가?
        print('num/3:',num/3)
    else : # num이 문자열이면, '1234' 'qwer'
        if num.isdigit():
            print('num/3:',int(num)/3)
        else : # 'qwer'
            print('알파벳은 계산 불가')

def f3(name) : # 변수인데 함수가 호출될 때 함수에서 필요한 값을 받아오는 변수
    print('name:',name)

def f4(x) : # 파라미터로 리스트를 받아서 출력
    for i in x:
        print(i, end=', ')

f0(3)
f1()
f2(3)
f2('3')
f2('qwer')
f3('3')
f3('aaa')

s = [1,2,3,4,5]
f4(s)

print()
# 다양한 반환값

def add(a, b) :
    return a + b # 함수를 호출한 곳으로 값을 반환

print(add(5, 6))

# 위 리스트를 파라미터로 받아
# 합을 반환하는 함수
# 평균을 반환하는 함수
# 최대값을 반환하는 함수
# 최소값을 반환하는 함수

def add(l) :
    sum = 0
    for i in l:
        sum += i
    return sum

def average(l) :
    sum = 0
    for i in l :
        sum += i
    return sum/len(l)

def max(l) :
    max = l[0]
    for i in range(len(l)) :
        if max <= l[i] :
            max = l[i]
    return max


def min(l) :
    min = l[0]
    for i in range(len(l)) :
        if min >= l[i] :
            min = l[i]
    return min

def max_min1(list1 : list) -> list :
    result = [list1[0], list1[0]]
    for i in list1:
        if result[0] < i :
            result[0] = i

        if result[1] > i :
            result[1] = i

    return result # 리스트 반환

def max_min2(list1 : list) -> tuple :
    a, b = list1[0], list1[0]
    for i in list1:
        if a < i :
            a = i

        if b > i :
            b = i

    return a, b # 값을 2개 반환

print(add(s))
print(average(s))
print(max(s))
print(min(s))

r = max_min1(s)
print(r[0])
print(r[1])

# 반환할 값 저장할 변수로 2개
x, y = max_min2(s)
print(x)
print(y)

def f1():
    print('f1() 호출')

def f2():
    print('f2() 호출')

def f3():
    print('f3() 호출')

def f4(x): # 파라미터로 튜플 받음. 튜플 : immutable 요소로 개수, 값 변경 불가
    print('f4() 호출')
    for i in x:
        print(i, end=", ")
    print()

# params = None => 디폴트 인자. 호출 시 생략 가능
def select(f, params = None): # 함수 포인터 : 함수의 주소값이 전달됨. 파이썬 표현으로는 함수의 참조값을 받아오는 파라미터. params : f의 파라미터
    # ex) 핸들러 등록 함수.
    # 핸들러란? 이벤트가 발생하면 자동으로 호출되서 그 처리를 하는 함수.
    if params == None:
        f() # 파라미터 값이 f1이라면 f1() / 파라미터 값이 f2라면 f2()
    else:
        f(params)

def main(): # 시작함수
    print('main() 호출')
    # f1()
    # f2()
    # f3()
    select(f1) # 함수의 참조값
    select(f2)
    select(f3)
    select(f4,(1,2,3))
    # f1() # 함수를 호출하면 그 함수가 사용할 스택 메모리를 할당


# print('프로그램 실행')
# f1() # 다이렉트 실행

main() # 메인을 통해서 f1, f2, f3() 호출


'''
2. 함수의 다형성
파이썬 변수의 타입은 고정이 아니므로 파라미터에 타입이 다른 값들을 전달할 수 있다.
이로 인해 다양한 형태로 실행될 수 있는데, 함수 안에서 실행하는 연산에 문제가 없는 타입의 값을 전달해야 한다.
'''
def add(a, b):
    return a + b

def main():
    # 함수의 다형성
    print(add(1,2))
    print(add('aaa','bbb'))
    print(add(1.23,4.56))
    print(add([1,2],[3,4,5]))
    #print(add(1,'qwer')) # error

main()

'''
 3. immutable 인자와 mutable 인자
 immutable : 값이 바뀌면 참조값이 바뀜
 a = 10
 a = 20 # a의 참조값이 바뀜

 mutable
 b = [1,2,3] # b에는 참조값 100. b[0]는 1의 참조값. b[2]도 2이 참조값
 b[1] = 30 # b[1] 30의 참조값으로 바뀜
 b의 요소의 참조값은 바뀌지만 b자체 참조값은 바뀌지 않음.
'''

def paramTest1(num, msg):
    # immurable param test
    print('변경전')
    print('num:',num,',msg:',msg)
    num = 300
    msg = '함수안'
    print('변경후')
    print('num:', num, ',msg:', msg)

def main():
    n = 10
    m = 'main안'
    print('함수 호출 전')
    print('n:',n,',m:',m)
    paramTest1(n,m)
    print('함수 호출 후')
    print('n:', n, ',m:', m)

main()

'''
 mutable param test
'''
def paramTest2(list1, list2):
    # mutable param test
    print('변경전')
    print('list1:',list1)
    print('list2:',list2)
    list1 = [100, 200]
    list2[0] = 10
    list2[2] = 30
    print('변경후')
    print('list1:', list1)
    print('list2:', list2)

def main():
    li1 = [1,2,3]
    li2 = [4,5,6,7]
    print('함수 호출 전')
    print('li1:',li1)
    print('li2:',li2)
    paramTest2(li1,li2)
    print('함수 호출 후')
    print('li1:', li1)
    print('li2:', li2)

main()

'''
4. 파이썬 함수의 다양한 아규먼트(인자)
1) 요구인자 : 함수에서 일반적으로 사용하는 방법으로 파라미터 개수와 순서를 맟추어 호출
2) 키워드인자 : 파라미터 순서에 맞추지 않아도 됨. 단 이 인자가 어느 파라미터로 전달될지 지정해야함
3) 디폴트 인자 : 파라미터 기본값을 지정하여 생략 가능
4) 가변인자 : 파라미터 개수 가변. 인자값을 튜플에 담아 전달
'''
def argTest1(name, tel, age):
    print('name:',name)
    print('tel:',tel)
    print('age:',age)
    print('12년 후 age:',age + 12)

def argTest2(age, name='aaa',tel='111'): # 디폴트 인자
    print('name')
    print('tel:',tel)
    print('age:',age)

def argTest3(*nums): # 가변인자. 파라미터는 전달한 값의 개수를 크기로 한 리스트
    print(type(nums))
    for i in nums:
        print(i, end=',')
    print()

def main():
    argTest1('aaa','111',12) # 요구인자
    #argTest1('bbb',12, '222') # error => 인자의 순서가 바뀌어서
    argTest1(tel='1234',age=12,name='aaa') # 키워드 인자. 순서 바뀌어도 문제 없음

    # 디폴트 인자
    argTest2(12)
    argTest2(22,'bbb')
    argTest2(32,'ccc','4123')

    # 가변 인자
    argTest3(1,2,3)
    argTest3(10,20,30,40,50)

main()

'''
5. 전역변수와 지역변수
전역변수 : 함수 밖에 정의한 변수로 변수 정의 아래에 있는 모든 함수와 코드에서 사용가능
지역변수 : 함수 안에서 정의한 변수로 선언한 함수 안에서만 사용 가능
'''

a = 10 # 전역변수. 이 파일 어디에서나 사용가능한 변수. 단 사용전 선언은 필수
def f1(x): # 파라미터도 지역변수
    b = 20 # 지역변수
    print('a:',a,'b:',b,'x:',x)

def f2():
    # 에러 : b와 x는 f1()의 지역변수이므로 다른 함수에서 사용 불가
    print('a:', a, 'b:', b, 'x:', x)

def f3():
    a = 100 # a:지역변수
    print('f3()에서 a:',a)

def f5():
    global  a # a:전역변수
    a = 200
    print('f5()에서 a:',a)

def f4():
    print('f4()에서 a:',a)

# f1(30)
# f2()
f3()
f4()
f5()
f4()

'''
6. 전역변수의 visible
'''
def f1():
    print('f1()')
    print('a=',a)
    #print('b=',b)
    #print('c=',c)

def f2():
    print('f2()')
    print('a=',a)
    print('b=',b)
    print('c=',c)

def f3():
    print('f3()')
    print('a=',a)
    print('b=',b)
    print('c=',c)

a = 10
f1()
b = 20
f2()
c = 30
f3()

'''
7. return
1) return : 함수 종료(함수는 return이 없어도 더이상 실행할 문장이 없으면 종료)
2) return 값 : 함수 종료 및 값 반환
3) return None : 파이썬은 리턴값이 없는 함수도 None이 반환됨. None은 값이 없음을 나타내는 상수
'''

def printHello():
    print('hello')

def main():
    result = printHello()
    print('result=',result)
    print('result type=',type(result))

main()


'''
9. 재귀함수
함수 안에서 함수 자기자신을 호출하는 방식을 재귀호출(recursive call)이라고 합니다. 
재귀호출은 일반적인 상황에서는 잘 사용하지 않지만 알고리즘을 구현할 때 매우 유용합니다(구현은 만들다와 같은 뜻입니다). 
보통 알고리즘에 따라서 반복문으로 구현한 코드보다 재귀호출로 구현한 코드가 좀 더 직관적이고 이해하기 쉬운 경우가 많습니다.

주의사항 : 끝나는 기준을 잘 잡아줘야함.
참고) https://dojang.io/mod/page/view.php?id=2352
'''

# 팩토리얼
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
def main():
    result = factorial(4)
    print("factorial:",result)

main()

# 피보나치 수열 - 재귀함수
def fibo(num) :
    if num == 1 or num == 2 :
        return num
    else :
        return fibo(num - 1) + fibo(num - 2)

def main():
    for i in range(1, 51):
        print(fibo(i), end = ',')
    print()

main()

# 피보나치 수열 - 반복문
def fibo2(num) :
    num0, num1, num2 = 1, 1, 0
    for i in range(0 ,num):
        if i < 2 :
            print(1, end=", ")
        else :
            num2 = num0 + num1
            print(num2, end=", ")
            num0, num1 = num1, num2
def main():
    fibo2(100)

main()

# 피보나치 수열 - 리스트
def fibo3(num):
    li = [0] * num
    for i in range(0, len(li)):
        if i < 2:
            li[i] = 1
        else :
            li[i] = li[i-2] + li[i-1]

    for i in li:
        print(i, end=", ")

def main():
    fibo3(100)

main()

'''
10. 함수 객체
'''

def sayHello():
    print('hello~')

def main():
    funcObj = sayHello # 함수 이름엔 함수 참조값이 저장됨
    funcObj()
    sayHello()

main()

'''
1) 함수 객체 활용 - 룩업 테이블
'''
def error1():
    print('1번 에러 발생')
def error2():
    print('2번 에러 발생')
def error3():
    print('3번 에러 발생')
def error4():
    print('4번 에러 발생')

def main():
    ec = 2
    if ec == 1:
        error1()
    elif ec == 2:
        error2()
    elif ec == 3:
        error3()
    elif ec == 4:
        error4()

def main2():
    ec = 2
    f =[error1, error2, error3, error4]
    f[ec-1]()

main2()

'''
2) 함수 객체 활용 - 핸들러 처리
'''
def onEvent(f):
    print('핸들러가 등록되었습니다.')
    f()
    print()

def myHandler1():
    print('1번 이벤트 핸들러입니다.')

def myHandler2():
    print('2번 이벤트 핸들러입니다.')

def myHandler3():
    print('3번 이벤트 핸들러입니다.')

def main():
    a = myHandler1
    onEvent(a)
    onEvent(myHandler2)
    onEvent(myHandler3)

main()

