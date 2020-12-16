import day02.borad.member.menu as member_menu
import day02.borad.article.menu as article_menu
def main():
    mem_menu = member_menu.MemMenu()
    ar_menu = article_menu.ArtMenu()

    while True:
        m = int(input('1.회원관리 2.게시판 3.종료'))
        if m == 1:
            mem_menu.run()
        elif m == 2:
            ar_menu.run()
        elif m == 3:
            print("프로그램 종료")
            break

main()
