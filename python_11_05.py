'''
# 리스트
# 인덱스와 같이 요소값 읽기
list1 = [1, 2, 3, 4, 5]
for idx, i in enumerate(list1) :
    print('index:',idx,',data.:',i)

list2 = ['aaa', 'bbb','ccc']
for idx, i in enumerate(list2) :
    print('list2[',idx,']=',i)

# 리스트 요소 여러 개 접근
list1 = list(range(1,11)) # [1,2,3,4,5,6,7,8,9,10]
a = list1[3:7]
print(a)

b = list1[3:8:2]
print(b)

# 리스트 요소 추가
# 추가
# list1[3] = 4
list1.append(4)
print(list1)
list1.insert(1, 5) # param1 : 끼워넣을 위치의 인덱스. param2 : 추가할 값
print(list1)

# 수정
list1[1] = 50
print(list1)

# 삭제 : del
del list1[1]
print(list1)

del list1[1:3]
print(list1)

list1.remove(4) # 인덱스 기준이 아니라 값으로 찾아서 삭제
print(list1)
# list1.remove(3) # 없는 갑 삭제 시 에러

list1.clear() # 전체 항목 삭제
print(list1)

del list1 # list1 자체 삭제
# print(list1) # 에러

# 요소 검색
list1 = [1,2,3,4,5]
if 3 in list1 : # in 연산자 : 뒤의 목록 안에 앞에서 지정한 값이 있으면 True, 없으면 False
    print('3은 목록에 포함')
    idx = list1.index(3)
    print(idx, '번째에 있다.')
else :
    print('3은 목록에 포함 안됨.')

# 요소 정렬
list1 = [7,3,5,9,2,4,1]
list1.sort() # reverse => False : 오름차순, True : 내림차순
print(list1)

list1.sort(reverse=True)
print(list1)

list2 = ['fsd', 'qwe','qbc','asdf']
print(list2)

list2.sort(reverse=False) # list2.sort()
print(list2)

# 리스트 복사
# 얕은 복사1
# 참조 값을 복사 = 주소값에 매칭이되는 난수

# 객체 지향 프로그래밍이란(OOP)?
# 객체 중심으로 코드 작성. 객체 중심이란 객체를 정의하고 객체와 객체 사이의 관계를 명시하는 것.
# 소형 프로그램보단 중대형 프로그램 작성 시 좋다.
# 객체 중심으로 코드를 짜기 때문에 메모리 해제 부분이 애매하며 개발자도 모르는 경우가 많음.
# heep이 흘러넘치는 경우 stack까지 침범.
# 참조 값이란 할당 받은 메모리 즉. 실 주소 값을 참조하는 값으로 얕은 복사는 이를 이용하는 것.

b = [1,2,3]
c = b
print(b)
print(c)
print(id(b))
print(id(c))
b[1] = 100
print(b)
print(c)

# 얕은 복사2
# 다른 메모리에 값을 복사
import copy

# 예제1
a = [1,2,3,4]
b = copy.copy(a)
print(a)
print(b)
print(id(a))
print(id(b))
a[1] = 100
print(a)
print(b)

# 예제2
c = [1,2,[3,4,5]] # mutable인 리스트가 요소에 포함되면 리스트는 참조 값이기 때문에 얕은 복사 시 문제 발생
d = copy.copy(c)
print(c)
print(d)
c[0] = 300
print(c)
print(d)
c[2][0] = 700
print(c)
print(d)

# 깊은 복사

e = [1,2,[3,4,5]]
f = copy.deepcopy(e)
print(e)
print(f)
e[2][0] = 700
print(e)
print(f)

# 리스트 확장
a = [1,2,3]
b = [6,7]
c = a + b
print(a)
print(b)
print(c)
a += b
print(a)
print(b)

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
print(b)


# 예제
# 주소록
# person : 이름, 전화, 주소
member = []


# for i in range(0, 3) :
#     name = input('name:')
#     tel = input('tel:')
#     address = input('address:')
#     l = [name,tel,address]
#     member.append(l)


# 함수 : 코드를 모듈화 해서 필요할때마다 호출하여 사용하는 방법
def make_mem() :
    global member
    name = input('name:')
    tel = input('tel:')
    address = input('address:')
    member.append([name,tel,address])

make_mem() # 함수 호출
print(member)

make_mem()
print(member)

make_mem()
print(member)


# 모든 사람의 이름만 출력
for i in range(0, 3) : # i는 index
    print(member[i][0])

for i in member : # i는 요소를 담는 변수
    print('name:',i[0])

# 이름으로 검색
name = input('search name:')
flag = True # 있다 없다에 대한 표시. 없으면 True, 있으면 False
for i in member :
    if name == i[0] :
        print(i)
        flag = False
if flag :
    print('없는 이름')

'''


# 함수
# 함수는 코드를 기능 단위로 끊어 프로그램의 모듈화를 가능하게 한다.
# 즉 반복적으로 등장하는 코드를 함수로 정의하고 이를 필요할 때마다 호출하여 사용.

# 함수 정의
# 함수가 어떻게 동작할 지 정의한다. 파라미터는 함수가 호출될 때 외부로부터 필요한 값을 받아오는 변수를 말한다.
# 반환값을 함수가 작업을 마친 뒤 반환하는 값을 말한다.

# 함수 정의 : 이 함수는 이러하게 동작한다. 함수 수식을 작성
# 함수 호출 : 정의한 함수를 불러서(이름) 그 함수를 실행시킴 => 분기(함수코드)
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
'''