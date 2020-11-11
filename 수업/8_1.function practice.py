'''
과제
1. 숫자를 요소로 갖는 빈 리스트를 하나 만듦.
메뉴 : 추가(중복안됨), 검색, 수정, 삭제, 전체목록, 전체 삭제, 종료
'''

num_list = []


# 문자열이 숫자인지 판별
def isNumber(s : str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def search_num(num : str) :
    if isNumber(num):  # 입력된 문자가 숫자인지 판별
        if float(num) in num_list:  # 중복된 숫자 값이 존재
            return "중복"
        else :
            return "중복아님"
    return "문자"

def check_empty_list() -> bool:
    if not num_list: # 비어있는 리스트는 False반환
        print('리스트가 비어있습니다.')
        return True
    return False

def add() -> None:
    while True:
        num = input('추가할 숫자 입력 : ')

        if search_num(num) == "중복아님":
            # if res : # False이면 중복된 숫자 존재
            num_list.append(float(num))
            break
        else:
            print('추가가 불가능합니다.\n')

def search() -> None:
    while True:
        num = input('검색할 숫자 입력 : ')

        if search_num(num) == "중복":
            print('인덱스:', num_list.index(float(num)))
            break
        else:
            print('검색이 불가능합니다.\n')


def modificate() -> None:
    if check_empty_list() :
        return

    while True:
        num = input('수정할 숫자 입력 : ')
        if search_num(num) == "중복":
            modi = input('변경할 숫자 입력 : ')
            if search_num(modi) == "중복":
                print("중복된 숫자가 존재합니다.")
                continue
            elif search_num(modi) == "중복아님":
                num_list[num_list.index(float(num))] = float(modi)
                break
        else:
            print('검색이 불가능합니다.\n')

def delete() -> None:
    if check_empty_list() :
        return

    while True:
        num = input('삭제할 숫자 입력 : ')
        if search_num(num) == "중복":
            num_list.remove(float(num))
            print('삭제 완료!!\n')
            break
        else:
            print('검색이 불가능합니다.\n')

def printAll() -> None:
    print(num_list)
    print()


def deleteAll() -> None:
    num_list.clear()
    print('전제 삭제 완료!!\n')


def stop() -> bool:
    return False


def main():
    flag = True
    while flag:
        li = [add, search, modificate, delete, printAll, deleteAll, stop]
        # menu = int(input('1.추가\n2.검색\n3.수정\n4.삭제\n5.전체목록\n6.전체 삭제\n7.종료\n=>'))
        try:
            menu = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체목록 6.전체 삭제 7.종료 =>'))
        except ValueError :
            print("숫자가 아님")

        if 1 <= menu <= 6:
            li[menu - 1]()
        elif menu == 7:
            print('프로그램 종료')
            flag = li[menu - 1]()
        else:
            print('잘못된 메뉴입니다.')

main()

'''
과제2
주소록, 빈 리스트에서 시작.
1. [[이름, 전화, 주소],[],[]]
메뉴 : 추가(중복안됨), 검색, 수정, 삭제, 전체목록, 전체 삭제, 종료 
'''
members=[]
def search_name(name):
    for idx, i in enumerate(members):
        if i[0]==name:
            return idx

def add():
    global members
    m = ['', '', '']
    while True:
        name = input('name:')
        flag = search_name(name)
        if flag==None:
            m[0]=name
            break
        else:
            print('중복된 이름. 다시 입력하시오')

    m[1] = input('tel:')
    m[2] = input('address:')
    members.append(m)

def printAll():
    for i in members:
        print(i)
    print()

# 이름이 있으면 전화번호, 주소값만 수정
def edit():
    while True:
        name = input('name:')
        idx = search_name(name)

        if idx != None:
            print("수정 가능")
            tel = input('tel:')
            address = input('address:')
            members[idx][1], members[idx][2] = tel, address
            break
        else :
            print("해당 이름이 없습니다.")
    return

def search():
    while True:
        name = input('name:')
        idx = search_name(name)
        if idx == None :
            print("해당 이름이 없습니다.")
        else :
            print(members[idx])
            break

# 이름 찾아서 아애 삭제
def delete():
    while True:
        name = input('name:')
        idx = search_name(name)
        if idx == None:
            print("해당 이름이 없습니다.")
        else :
            del members[idx]
            break
def deleteAll():
    members.clear()

def stop():
    return False

def main():
    li = [add, search, edit, delete, printAll, deleteAll, stop]  # 룩업 테이블. 함수 객체 리스트
    flag = True
    while flag:
        menu = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.전체삭제 7.종료'))
        if 1 <= menu <= 6:
            li[menu - 1]()
        elif menu == 7:
            flag = li[menu - 1]()

main()
