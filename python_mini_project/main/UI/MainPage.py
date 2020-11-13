import tkinter as tk
from PIL import Image, ImageTk
import python_mini_project.movie.UI.MovieListPage as movie
import python_mini_project.login.UI.LoginPage as lp
import python_mini_project.staticString as ss
import os



class MainPage(tk.Frame):
    def __init__(self, master):
        # sd = sf.SwitchFrame()
        tk.Frame.__init__(self, master)
        # self.pack(fill = "both", expand = True)
        print("현재 페이지 : ",os.getcwd())
        # isMi = os.getcwd().split('\\')
        # print(len(isMi))
        # print(isMi[len(isMi)-1])
        # if isMi[len(isMi)-1] != 'main':
        #     print("fdas")
        #     os.chdir("main")
        # print(os.getcwd())
        load = Image.open('../data/main/cgv_logo.png')
        print("이동한 경로 : ", os.getcwd())
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render, bg = "red") # width = 250, height = 350
        img.image = render
        img.size()
        # img.grid(row = 0, column = 1, padx = 190, pady = 100)
        img.place(x = 200, y = 100, width = 607, height = 292)

        if ss.isLogin:
            tk.Button(self, text="로그인",
                  command=lambda: master.switch_frame(lp.LoginPage)).place(x=360, y=440)

        tk.Button(self, text="상영 중인 영화",
                  command=lambda: master.switch_frame(movie.StartPage)).place(x = 470, y = 440)

        tk.Button(self, text="종료", command=lambda: master.quit()).place(x = 620, y = 440)
