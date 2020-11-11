'''
9. 입출력

스트림 : 단방향
입력스트림 : 밖에서 프로그램 쪽으로 데이터 흐름을 구현
출력스트림 : 프로그램에서 밖으로의 데이터 흐름을 구현

1. 표준 스트림
sys : 표준 시스템 객체나 함수가 정의. 표준 입력, 표준 출력, 표준 에러 정의
표준 입력 : sys.stdin, 키보드로 읽는 함수 제공
표준 출력 : sys.stdout, 콘솔에 출력하는 함수 제공
표준 에러 : sys.stderr, 콘솔에 표준 에러 메시지 출력하는 함수 제공

<표준 입출력을 쉽게 할 수 있는 함수>
input() - 키보드 입력
print() - 키보드 출력

2. 스트림의 읽기/쓰기 함수
1) 입력 스트림의 읽기 함수
read(size) : size만큼 읽음
read() : 전체 내용 읽음
readLine() : 한 줄 읽음

2) 출력 스트림의 쓰기 함수
write(str) : str을 씀
writelines() : 리스트나 튜플에 담긴 여러 줄을 한번에 출력

3. 파일 입출력
1) 파일 오픈 : open("파일경로","모드")
 모드 : "r"-읽기 / "w"-쓰기 / "a"-이어쓰기
 r - 없는 파일 열면 에러
 w - 없는 파일 열면 에러 안나고 새로 생성하여 오픈. 기존 내용 있으면 지우고 오픈
 a - 기존 내용이 있으면 이어쓰기
2) 파일 닫기 : close()
'''

'''
파일 읽기,쓰기 예제
'''

def main():
    f = open("a.txt", "r", encoding = "utf-8") # 파일 열기
    str1 = f.read() # 파일 내용 읽기
    print(str1)
    f.close() # 파일 닫기

    f = open("b.txt", "w", encoding="utf-8") # 파일을 쓰기 모드로 오픈
    msg = 'hello file open'
    f.write(msg) # msg값을 파일에 씀
    f.close()    # 파일 닫기

    # 파일 b.txt의 내용을 읽어서 콘솔에 출력
    f = open("b.txt", "r", encoding="utf-8")
    str2 = f.read()
    print(str2)
    f.close()

main()

# 원본파일명과 타깃 파일명을 입력받아 복사하는 프로그램을 만드시오
def file_copy():
    original_file = input('original file:')
    copy_file = input("copy file:")

    f = open(original_file + ".txt", "r", encoding="utf-8")
    str = f.read()
    f.close()

    f = open(copy_file+".txt", "w", encoding="utf-8")
    f.write(str)
    f.close()

file_copy()

def main2():
    f = open("test.txt","r",encoding="utf-8")
    while True:
        str = f.read(4)
        if str == '':
            break
        print(str, end = "") # 파일에 엔터가 포함되면 파일의 엔터와 print()의 엔터가 모두 출력됨.
    f.close()
main2()

def main3():
    f = open("test.txt" , "r")
    while True:
        str = f.readline()
        if str == '':
            break
        print(str, ", ", len(str))
    f.close()
main3()
def main4():
    with open("test.txt" , "r") as f:
        str = f.read()
        print(str)
main4()

'''
키보드로 입력받은 내용을 파일에 저장하시오. (파일이름도 입력받음.)
/stop을 입력받을 때까지 반복하고 저장하고 빠져나옴.
빠져나와서 파일 내용 읽어서 콘솔에 출력
'''

def input_keyboard():
    file_name = input("파일 이름:")
    # 파일 쓰기 모드 오픈 : ocreate & otruncate
    # ocreate : 파일이 없으면 새로 생성. 있으면 기존 파일 오플
    # otruncate : 기존에 쓰던 파일을 오픈하면 기존 파일의 내용을 지우고 오픈

    # open(file_name, "a", encoding="utf-8")
    # 이어쓰기 모드, 기존 파일을 쓰기 모드로 오픈할 때 기존 내용을 지우지 않고 새 내용을 뒤에 이어서 씀
    f1 = open(file_name + ".txt", "w", encoding="utf-8")

    while True:
        str = input()

        if str == "/stop":
            print("프로그램 종료")
            break
        f1.write(str + "\n")

    f1.close()
    f2 = open(file_name + ".txt","r",encoding="utf-8")
    str = f2.read()
    print(str)
    f2.close()

input_keyboard()

'''
4. 바이너리 읽기 쓰기
모드 :  "rb" - 읽기 / "wb" - 쓰기 / "ab" - 이어쓰기
'''

def main5() :
    f = open('image_test.jpg', 'rb') # 바이너리 읽기 모드로 오픈
    b_data = f.read()
    print("바이너리 데이터")
    print(b_data)
    f.close()

    f = open('image_test_복사본.jpg','wb') # 바이너리 쓰기 모드로 오픈
    f.write(b_data)
    f.close()

main5()

'''
5. 위치 제어
tell() - 현재 읽고 쓸 위치 반환
seek(off, whence) : 읽고 쓸 위치 whence를 기준으로 off만큼 떨어진 위치로 이동
    whence : 0 => 맨 앞을 기준
    whence : 1 => 현재 위치를 기준
    whence : 2 => 맨 뒤를 기준
'''
def main6():
    f = open('b.txt','w')
    str1 = 'abcdefghijklmnopqrstuvwxyz'
    print(str1)
    f.write(str1)
    f.close()

    f = open('b.txt','rb') # 위치 제어하려면 바이너리 모드로 오픈해야 함
    print(f.read(3))
    print('현재 위치:',f.tell())

    f.seek(5)
    print('현재 위치:',f.tell())
    print('맨 앞에서 5위치의 문자:',f.read(1))

    f.seek(10, 0)
    print('현재 위치:',f.tell())
    print('맨 앞에서 10위치의 문자:',f.read(1))
    print(f.tell())
    f.seek(3,1)
    print('현재 위치:',f.tell())
    print('현재 위치에서 3위치의 문자:',f.read(1))

    f.seek(-3,1)
    print('현재 위치:', f.tell())
    print('현재 위치에서 -3위치의 문자:,',f.read(1))

    f.seek(-3,2)
    print('현재 위치:', f.tell())
    print('맨 뒤에서 -3위치의 문자:',f.read(1))

    for i in range(1,len(str1)+1) :
        f.seek(-i , 2)
        print(f.read(1).decode(), end="") # 바이트객체.decode(), bytes를 str로 변환
        #print(str(f.read(1).split('\'')[1])
    f.close()

main6()

'''
6. 파일 제어 함수들
1) truncate(size) - size 크기로 파일 절삭
2) rename(old, new) - 파일명을 old에서 new로 변경
3) remove(파일명) - 파일 삭제
'''

def main():
    str1 = "abcdefghijklmnopqrstuvwxyz"
    f = open('f.txt', 'w')
    f.write(str1)
    f.truncate(10)
    f.close()

    f = open('f.txt','r')
    print(f.read())
    f.close()

main()

import os
def main1():
    old_name = input('이름을 수정할 파일명을 입력하시오: ')
    new_name = input('새 파일명을 입력하시오: ')

    os.rename(old_name, new_name)

    f = open(new_name, 'r')
    print(f.read())
    f.close()

main1()

import os
def main2():
    f = open('rem.txt','w+')
    # r+: 읽고 쓰기 모드. r특징 가지고 있음. 없는 파일 열면 에러
    # w+: 읽고 쓰기 모드. w특징 가지고 있음. 없는 파일 열면 에러 안나고 새로 생성하여 오픈. 기존 내용 있으면 지우고 오픈
    # a+: 읽고 쓰기 모드. a특징 가지고 있음. 기존 내용이 있으면 이어쓰기

    f.write("hello Python")
    print(f.tell()) # 12
    f.seek(0) # 커서 위치를 맨 앞으로 이동.
    print(f.read()) # 다시 읽기
    f.close()

    os.remove('rem.txt')

    f = open('rem.txt','r') # 파일이 없기 때문에 여기서 에러 발생
    print(f.read())
    f.close()

main2()

'''
7. 디렉토리 제어
import os
os.getcwd() - 현재 작업 디렉토리 명 반환
os.chdir(path) - 작업 디렉토리는 path로 변경
os.mkdir(path) - 디렉토리 생성
os.rmdir(path) - 디렉토리 삭제
os.listdir(path) - 디렉토리 파일 목록 리스트로 반환
os.path.isfile(path) - path의 파일이 존재하면 True, 아니면 False
os.path.isdir(path) - path의 디렉토리가 존재하면 True, 아니면 False
'''

import os

def main():
    print("현재 작업 디렉토리:",os.getcwd())

    new_dir = input("생성할 디렉토리 이름을 입력하시오:")
    print(new_dir, "exist?", os.path.isdir(new_dir))

    os.mkdir(new_dir)
    print(new_dir,"디렉토리 생성")
    print(new_dir, "exist", os.path.isdir(new_dir))

    os.chdir(new_dir)
    print(new_dir,"로 디렉토리 이동")
    print("현재 작업 디렉토리:",os.getcwd())

    list1 = ['a.txt','b.txt','c.txt']
    for f_name in list1:
        f = open(f_name, 'w')
        print(f_name, '파일 생성. 내용으로 파일명 작성')
        f.write(f_name)
        f.close()

    os.chdir('../')
    # 절대 경로 : c:\000\
    # 상대 경로 : 현재 파일을 기준으로 경로 설정. 상위 폴더 : ../
    print("상위 디렉토리로 이동")
    print("현재 작업 디렉토리:", os.getcwd())

    files = os.listdir(new_dir)
    print(new_dir, "디렉토리의 파일 목록")
    for f_name in files:
        f = open(new_dir + "/" + f_name, 'r')
        print(f_name, "(content :", f.read(),")")
        f.close()

    for f_name in files:
        print(new_dir + "/" + f_name, "파일 삭제")
        os.remove(new_dir + "/" + f_name)

    print(new_dir, "디렉토리의 파일 목록")
    print(os.listdir(new_dir))

    print(new_dir, "디렉토리 삭제")
    os.rmdir(new_dir)
    print(new_dir,"exist?",os.path.isdir(new_dir))

main()

'''
메모장 만들기
'''
import os

def chdir():
    if os.getcwd() != "memo": # 현재 경로가 memo가 아니면
        os.chdir("C:/Users/wonseyoung/Desktop/python work")
        if not os.path.isdir("memo"): # memo가 존재하지 않으면
            os.mkdir("memo") # 디렉토리 만들고
            os.chdir("memo") # 이동
        else :
            os.chdir("memo") # 이동

def write_content(file_name, rwa):
    f = open(file_name + ".txt", rwa, encoding="utf-8")
    print("내용 입력(종료하시려면 EOI를 입력하세요)")
    while True:
        str = input()
        if str == "EOI":
            break
        f.write(str + '\n')
    f.close()

def main():
    print(os.getcwd())
    while True:
        menu = int(input('1.읽기 2.쓰기 3.삭제 4.청소 5.종료 =>'))

        if menu == 1:
            chdir()
            print(os.getcwd())

            file_list = os.listdir("./") # 현재 디렉토리 리스트 얻기
            if not file_list: # 빈 Sequence(String/ Tuple/ List)는 False 반환
               print("빈 디렉토리 입니다.")
            else :
                print(file_list)
                while True:
                    file_name = input("읽을 파일명을 입력하세요 : ")
                    if file_name + ".txt" in file_list:
                        #읽기
                        f = open(file_name + ".txt","r",encoding="utf-8")
                        print(f.read())
                        f.close()
                        break
                    else:
                        print("정확하지 않은 파일명입니다.")
                        continue
        elif menu == 2:
            flag = False
            chdir()
            isMemo = input("메모장을 만드시겠습니까?(y/n)")
            if isMemo == "y":
                while True:
                    file_name = input("파일명를 입력하세요 : ") # 중복 확인하기
                    file_list = os.listdir(os.getcwd())
                    if file_name + ".txt" in file_list:
                        print("해당 파일은 이미 존재합니다.")
                        menu = int(input("1. 새로쓰기 2.이어쓰기 => "))
                        if menu == 1:
                            continue
                        elif menu == 2:
                            break
                    else:
                        flag = True
                        break

                if flag or menu == 1: # 새로쓰기
                    write_content(file_name,'w')
                elif menu == 2: # 이어쓰기
                    write_content(file_name, 'a')
            elif isMemo == "n":
                continue

        elif menu == 3:
            print("파일 삭제")
            chdir()
            file_list = os.listdir("./")
            print(file_list)
            if file_list:
                while True:
                    f_name = input('삭제할 파일명을 입력하세요 : ')
                    if f_name + ".txt" in file_list:
                        os.remove(f_name + ".txt")
                        break
                    else :
                        print("해당 파일은 존재하지 않습니다.")



        elif menu == 4:
            chdir()
            file_list = os.listdir("./")
            print(file_list)
            print(not file_list)
            if file_list:
                for f_name in file_list:
                    os.remove(f_name)

            os.chdir("../")
            print(os.getcwd())
            os.rmdir("memo")
        elif menu == 5:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴입니다.")
            continue

main()



