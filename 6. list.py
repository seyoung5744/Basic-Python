'''
리스트
인덱스와 같이 요소값 읽기
'''
list1 = [1, 2, 3, 4, 5]
for idx, i in enumerate(list1) :
    print('index:',idx,',data.:',i)

list2 = ['aaa', 'bbb','ccc']
for idx, i in enumerate(list2) :
    print('list2[',idx,']=',i)

'''
리스트 요소 여러 개 접근
'''
list1 = list(range(1,11)) # [1,2,3,4,5,6,7,8,9,10]

a = list1[3:7]
print(a)

b = list1[3:8:2]
print(b)

'''
리스트 요소 추가
'''
# 추가
# list1[3] = 4
list1.append(4)
print(list1)
list1.insert(1, 5) # param1 : 끼워넣을 위치의 인덱스. param2 : 추가할 값
print(list1)

'''
수정
'''
list1[1] = 50
print(list1)

'''
삭제 : del
'''
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

'''
요소 검색
'''
list1 = [1,2,3,4,5]
if 3 in list1 : # in 연산자 : 뒤의 목록 안에 앞에서 지정한 값이 있으면 True, 없으면 False
    print('3은 목록에 포함')
    idx = list1.index(3)
    print(idx, '번째에 있다.')
else :
    print('3은 목록에 포함 안됨.')

'''
요소 정렬
'''
list1 = [7,3,5,9,2,4,1]
list1.sort() # reverse => False : 오름차순, True : 내림차순
print(list1)

list1.sort(reverse=True)
print(list1)

list2 = ['fsd', 'qwe','qbc','asdf']
print(list2)

list2.sort(reverse=False) # list2.sort()
print(list2)

'''
리스트 복사
얕은 복사1
참조 값을 복사 = 주소값에 매칭이되는 난수

객체 지향 프로그래밍이란(OOP)?
객체 중심으로 코드 작성. 객체 중심이란 객체를 정의하고 객체와 객체 사이의 관계를 명시하는 것.
소형 프로그램보단 중대형 프로그램 작성 시 좋다.
객체 중심으로 코드를 짜기 때문에 메모리 해제 부분이 애매하며 개발자도 모르는 경우가 많음.
heep이 흘러넘치는 경우 stack까지 침범.
참조 값이란 할당 받은 메모리 즉. 실 주소 값을 참조하는 값으로 얕은 복사는 이를 이용하는 것.
'''
b = [1,2,3]
c = b
print(b)
print(c)
print(id(b))
print(id(c))
b[1] = 100
print(b)
print(c)

'''
얕은 복사2
다른 메모리에 값을 복사
'''
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

'''
깊은 복사
'''
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


