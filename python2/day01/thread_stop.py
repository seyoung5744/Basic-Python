import threading, time
"""
파이썬 스레드 강제 종료.
"""
# 외부 조건에 의해서 스레드 조작.
def th(flag): #flag는 쓰레드 밖에서 제어. 이 flag값이 True가 되면 쓰레드 종료
    a = 0
    while True:
        # 파라미터로 받은 함수 flag(). 람다로 처리 -> 자동적으로 동기화해줌.
        if flag(): # 동기화 해줘야 main이랑 th에서 사용되는 flag에 문제가 안생김
            break
        a += 1
        print(a)
        time.sleep(1)
    print('th stop')


def main():
    flag = False

    # 쓰레드 조작 flag는 꼭 함수 형태로 전달해야함.
    t = threading.Thread(target = th, args = (lambda : flag,))
    t.start()
    time.sleep(1) # main thread sleep. 메인이 파생 쓰레드 종료하는것을 확인하기 위해 약간의 딜레이 추가.
    flag = True # th 쓰레드 종료
    print('main stop')


main()