# import python_mini_project.main.mainMenu as mm
import python_mini_project.Switch_Frame as sa


def main():
    # m = mm.MainMenu()
    # m.run()
    app = sa.SwitchFrame()
    app.geometry("1000x600+100+100")  # 창의 너비, 창의 높이, 창의 가로 방향 위치, 창의 세로 방향 위치
    app.mainloop()

main()