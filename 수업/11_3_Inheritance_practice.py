'''
캐릭터
1. 피카츄 2. 꼬부기 3. 이상해씨

hp : 체력. 0이면 죽음
exp : 경험치. 0부터 시작
level : 일정 경험치마다 레벨업. 1부터 시작

밥먹기 : hp증가
잠자기 : hp증가
운동하기 : hp감소, exp증가
놀기 : hp감소. exp증가
'''

class PocketMon: #피카추, 꼬부기, 이상해씨에 상속을 위해 만든 클래스. 공통의 멤버변수와 메서드 정의
    def __init__(self):
        self.hp = 0
        self.exp = 0
        self.level = 1
        self.name = ''

    def eat(self):
        print(self.name, '밥먹음')

    def sleep(self):
        print(self.name, '잠잠')

    def exc(self):
        print(self.name, '운동함')

    def play(self):
        print(self.name, '논다')

    def levelup(self):
        print('레벨업')

    def printInfo(self):
        print('hp:', self.hp)
        print('exp:', self.exp)
        print('level:', self.level)

class Picachu(PocketMon):
    def __init__(self):
        super().__init__()
        self.hp = 40
        self.name = '피카추'

    def eat(self):
        super().eat()#부모 클래스의 eat()호출
        self.hp += 5

    def sleep(self):
        super().sleep()
        self.hp += 10

    def exc(self):
        super().exc()
        self.hp -= 15
        self.exp += 10
        self.levelup()
        return self.hp>0    #반환값 True 살아있음. False 죽었음

    def play(self):
        super().play()
        self.hp -= 10
        self.exp += 5
        self.levelup()
        return self.hp > 0

    def levelup(self):
        #경험치 20마다 레벨 1씩 올려줌
        if self.exp >= 20:
            super().levelup()
            self.level+=1
            self.exp -= 20

    def 백만볼트(self):
        print('백만볼트 공격')


class Gobook(PocketMon):
    def __init__(self):
        super().__init__()
        self.hp = 50
        self.name = '꼬부기'

    def eat(self):
        super().eat()
        self.hp += 8

    def sleep(self):
        super().sleep()
        self.hp += 12

    def exc(self):
        super().exc()
        self.hp -= 20
        self.exp += 9
        self.levelup()
        return self.hp > 0  # 반환값 True 살아있음. False 죽었음

    def play(self):
        super().play()
        self.hp -= 15
        self.exp += 7
        self.levelup()
        return self.hp > 0

    def levelup(self):
        if self.exp >= 30:
            super().levelup()
            self.level += 1
            self.exp -= 30

    def 물대포(self):
        print('물대포 공격')

class Lee(PocketMon):
    def __init__(self):
        super().__init__()
        self.hp = 20
        self.name = '이상해씨'

    def eat(self):
        super().eat()
        self.hp += 3

    def sleep(self):
        super().sleep()
        self.hp += 5

    def exc(self):
        super().exc()
        self.hp -= 8
        self.exp += 9
        self.levelup()
        return self.hp > 0  # 반환값 True 살아있음. False 죽었음

    def play(self):
        super().play()
        self.hp -= 4
        self.exp += 6
        self.levelup()
        return self.hp > 0

    def levelup(self):
        if self.exp >= 10:
            super().levelup()
            self.level += 1
            self.exp -= 10

    def 넝쿨(self):
        print('넝쿨 공격')

class Menu:
    def __init__(self):
        self.ch = None

    def ch_choice(self):
        x = int(input('캐릭터 선택. 1.피카추 2.꼬부기 3.이상해씨'))
        if x==1:
            self.ch = Picachu() #업캐스팅
        elif x==2:
            self.ch = Gobook()
        elif x==3:
            self.ch = Lee()
        else:
            self.ch = Picachu()

    def run(self):
        flag = True

        while flag:
            menu = int(input('1.밥먹기 2.잠자기 3.운동하기 4.놀기 5.정보확인 6.종료 7.특기공격'))
            if menu==1:
                self.ch.eat()
            elif menu==2:
                self.ch.sleep()
            elif menu==3:
                flag = self.ch.exc()
                if not flag:
                    print('캐릭터 사망')
            elif menu==4:
                flag = self.ch.play()
                if not flag:
                    print('캐릭터 사망')
            elif menu==5:
                self.ch.printInfo()
            elif menu == 6:
                flag = False
            elif menu == 7:
                if isinstance(self.ch, Picachu):
                    self.ch.백만볼트()
                elif isinstance(self.ch, Gobook):
                    self.ch.물대포()
                elif isinstance(self.ch, Lee):
                    self.ch.넝쿨()


        print('게임 종료')

def main():
    m = Menu()
    m.ch_choice()
    m.run()
main()