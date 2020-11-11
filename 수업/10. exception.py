'''
1. 예외처리
예외 : 프로그램 런타임시 발생하는 문제. 보통 예외가 발생하면 프로그램은 중단
      예외처리는 예외가 발생하더라도 프로그램이 중단되는 것을 막는다.

try :
    # 예외가 발생할 만한 코드
except 예외명 :
    # try 블록에서 발생한 예외 중 동일한 이름의 예외만 받아서 처리
else :
    # try 블록에서 예외가 발생하지 않았을 때 실행될 코드 구현
finally :
    # 정상종료, 비정상종료 모두 종료 되기전 실행되는 블록
'''

def main():
    list1 = [1,2,3]
    try: # 예외가 발생할꺼 같은 곳은 try블록으로 묶음
        print(list1[1])
        result = 3/5
        res = 3 + 'abc' # 에러 발생하는 곳
        print("result=",result) # 예외 처리 블록. 발생한 예외 이름이 같아야 받는다.
    except ZeroDivisionError:
        print("0으로 나눌 수 없다.")
    except IndexError:
        print("없는 인덱스에 접근")
    #except ( ZeroDivisionError, IndexError ):
    #   print("예외 발생")
    except Exception as e:
        print("모든 예외 처리")
        print(type(e))
    except: # 모든 예외 객체 받아서 처리
        print("모든 예외 처리(예외 처리 명시 안함)")
    else:
        print("예외가 발생하지 않았다.")
    finally: # 프로그램이 끝나기 전에 무조건 실행되는 블록.
        print("종료전 무조건 실행.")

    print("프로그램은 중단되지 않았다")

main()

'''
2. 예외 발생시키기

raise 예외 객체
'''

def printNum():
    num = int(input("num(1~5사이만 입력):"))

    if num < 1 or num > 5:
        raise ValueError    # 예외 발생 시킴

    print("input num:",num)
def add_int(a, b):
    if not isinstance(a, int):
        raise TypeError('int 타입만 연산 가능')
    if not isinstance(b, int):
        raise TypeError('int 타입만 연산 가능')

    return a + b

def main2():
    try:
        result = add_int(2,4)
        print('result:',result)

        result = add_int('2','4')
        print('result:',result)

        printNum()
    except TypeError as e:
        print(e)
    except ValueError as v:
        print(v)
    except:
        print("예상치 못한 예외 발생")

main2()

# 사용자 정의 예외 클래스
class MyError(Exception): # Exception 파이썬에서 모든 예외의 조상 클래스
    def __init__(self, msg): # 생성자. 객체 생성시 한번 호출되는 함수로 객체를 초기화
        self.msg = msg # self.msg : 멤버변수.
        # 파라미터는 현재 함수가 종료하면 없어지지만 멤버 변수는 객체와 생명주기를 같이 한다.

def printNum2():
    num = int(input("num(1~5사이만 입력):"))

    if num < 1 or num > 5:
        raise MyError('잘못된 값')    # 예외 발생 시킴

    print("input num:",num)

def main3():
    try:
        printNum2()
    except MyError as e:
        print('예외 발생:', e)

main3()