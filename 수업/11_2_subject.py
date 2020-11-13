#1. 구구단 한단 출력(단수 입력 받음)
#3*1=3
#3*2=6 이런식으로
dan = int(input("단수를 입력하세요. "))
num = 1
while num < 10 :
    #print(dan,'*',num,'=',dan*num)
    print(str(dan) + "*" + str(num) + "=" + str(dan*num))
    num += 1


print()    
#2. 구구단 2-9단 모두 출력 수식까지 다
print("구구단 출력 2-9단")

dan = 2
while dan < 10 :
    print(dan,"단")
    num = 1
    while num < 10:
        print(dan,'*',num,'=',dan*num)
        num += 1
    dan += 1

#3. 1-100사이의 소수(소수:약수가 1과 자기자신)

prime = [2]
num = int(input("숫자 입력 : "))
i = 2
while i <= num:
    j = 0
    while j < len(prime):
        if i % prime[j] == 0:  # 소수로 나눠지면 해당 숫자는 소수가 아님 ex) 6 / 2
            break
        if j + 1 == len(prime):  # 소수 일때
            prime.append(i)
        j += 1
    i += 1

i = 0
while i < len(prime):
    print(prime[i], end=", ")
    i += 1

#4. 삼각형1(크기 입력 받음)
# *
# **
# ***
# ****

size = int(input("크기를 입력하시오."))
i = 0
while i < size :
    j = 0
    while j <= i :
        print("*", end = "")
        j += 1
    print()
    i += 1


    
#5. 삼각형2(크기입력받음)
 #    *
 #   **
 #  ***
 # ****

size = int(input("크기를 입력하시오."))
i = 0
while i < size :
    j = size - 1
    while j > i :
        print(" ", end = "")
        j -= 1
    k = 0
    while k <= i :
        print("*", end = "")
        k += 1
   
    print()
    i += 1

    
#6.삼각형3(크기 입력받음)
#   *
#  ***
# *****


size = int(input("크기를 입력하시오."))
i = 0
while i < size :
    j = size - 1
    while j > i :
        print(" ", end = "")
        j -= 1
    k = 0
    while k <= i * 2  :
        print("*", end = "")
        k += 1
   
    print()
    i += 1
