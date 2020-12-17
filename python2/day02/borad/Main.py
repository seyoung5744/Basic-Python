import day02.borad.member.menu as member_menu
import day02.borad.article.menu as article_menu
def main():
    mem_menu = member_menu.MemMenu()
    ar_menu = article_menu.ArtMenu()

    while True:
        m = int(input('1.회원관리 2.게시판 3.종료'))
        if m == 1:
            mem_menu.run()
        elif m == 2: # 로그인 되어있어야 사용 가능하도록 구현
            d = mem_menu.loginCheck()
            if d[0] : # 로그인 상태. d[1] : 로그인 아이디
                ar_menu.run(d[1])
            else :
                print("로그인 먼저 하시오")

        elif m == 3:
            print("프로그램 종료")
            break

main()
