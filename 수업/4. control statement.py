'''
3명의 학생 점수를 받아서 평균 출력
'''
i = 0
sum = 0
while i < 3:
    grade = int(input("점수 입력 : "))
    sum += grade
    i += 1

print("평균 : ", sum/3)

'''
요일 검사
0 : 일, 1 : 월, 2 : 화, 3 : 수, 4 : 목, 5 : 금, 6 : 토
'''
day = int(input("숫자 0-6을 입력받아 요일 출력하시오."))
if day == 0 :
    print("일요일 입니다.")
elif day == 1:
    print("월요일 입니다.")
elif day == 2:
    print("화요일 입니다.")
elif day == 3:
    print("수요일 입니다.")
elif day == 4:
    print("목요일 입니다.")
elif day == 5:
    print("금요일 입니다.")
else :
    print("토요일 입니다.")


'''
리스트
arr = [1,2,3,4,5]

print(arr[0])   # 리스트 요소 읽기

'''

score = [0, 0, 0]
for i in range(0, 3) :
    score[i] = int(input("math score:"))

sum = 0
for i in range(0, 3) :
    sum += score[i]

f = sum / 3
print("평균 : {0}".format(f))

print("평균보다 높은 점수 출력")
for i in score :
    if f < i :
        print(i)

print("최고 점수 출력")
m = score[0]
for i in range(0, len(score)) :
    if m < score[i] :
        m = score[i]

print(m)


#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sums = 0
# for i in nums:
#     sums += i
#
# print("총합 : %d" % sums)

'''
삼각형 찍기
'''
num = int(input())
for i in range(1, num + 1):
    for j in range(0, i):
        print("#", end="")
    print()
for i in range(num, 0, -1):
    for j in range(0, i):
        print("#", end="")
    print()
print()
####################
for i in range(0, num):
    for j in range(i, num-1):
        print(" ",end="")
    for k in range(0, i+1):
        print("*",end="")
    print()

for i in range(1, num + 1):
    for j in range(0, i-1):
        print(" ", end="")
    for k in range(i, num + 1):
        print("*", end="")
    print()
print()
####################
for i in range(0, num):
    for j in range(i, num-1):
        print(" ",end="")
    for k in range(0, i+1):
        print("*",end="")
    for n in range(0, i):
        print("*",end="")
    print()

for i in range(1, num + 1):
    for j in range(0, i-1):
        print(" ", end="")
    for k in range(i, num + 1):
        print("*", end="")
    for n in range(i, num):
        print("*", end="")
    print()
print()

# 강사님 코드
for i in range(1, num + 1):
    ch = '_'
    for j in range(num, 0, -1):
        if j == i:
            ch = '#'
        print(ch, end="")
    print()



'''
range와 enumerate
'''

data = [12, 56, 78, 34]
for idx, i in enumerate(data) : # 인덱스와 요소 함께 추출
    print('data[', idx, ']:', i)

for i in data :
    print(i, end = ',')

print()

# print() 마지막 end 생략하기

ch = ","
for idx, i in enumerate(data):
    if idx+1 == len(data):
        ch = "\n"
    print(i, end=ch)

'''
반복문
for : 리스트, 문자열, 나열된 값들을 처리할 때 활용
while : 조건에 의해서 반복하고자 할 때
'''
while True:
    score = int(input('score : '))
    if score >= 0 and score < 100:
        break

print(score)

