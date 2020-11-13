import tkinter as tk
import python_mini_project.movie.movieService as ms
from PIL import Image, ImageTk
import python_mini_project.movie.UI.MovieOne as pOne
import python_mini_project.movie.UI.MovieTwo as pTwo
import python_mini_project.movie.UI.MovieThree as pThree
import python_mini_project.main.UI.MainPage as mp
import os


class StartPage(tk.Frame):
    def __init__(self, master):
        # sd = sf.SwitchFrame()
        tk.Frame.__init__(self, master)
        tk.Label(self, text="상영 중인 영화", width = 10, font=('Helvetica', 18, "bold")).\
            grid(row=0, column=1, pady = 30)

        self.backButton()

        # os.chdir("../")
        print("영화 리스트 페이지1:",os.getcwd())
        load = Image.open('../data/movie/im.png')
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render) # width = 250, height = 350
        img.image = render
        img.size()
        img.grid(row = 1, column = 0, padx = 30, pady = 20)

        load2 = Image.open('../data/movie/im2.png')
        render2 = ImageTk.PhotoImage(load2)
        img2 = tk.Label(self, image=render2)
        img2.image = render2
        img2.size()
        img2.grid(row=1, column=1, padx = 30, pady = 20)

        load3 = Image.open('../data/movie/im3.png')
        render3 = ImageTk.PhotoImage(load3)
        img3 = tk.Label(self, image=render3)
        img3.image = render3
        img3.size()
        img3.grid(row=1, column=2, padx = 30, pady = 20)

        print("영화 리스트 페이지2:", os.getcwd())
        tk.Button(self, text="삼진그룹 영어토익반",
                  command=lambda: master.switch_frame(pOne.PageOne)).grid(row=2, column=0)

        tk.Button(self, text="도굴",
                  command=lambda: master.switch_frame(pTwo.PageTwo)).grid(row=2, column=1)
        tk.Button(self, text="노트북",
                  command=lambda: master.switch_frame(pThree.PageThree)).grid(row=2, column=2)

    def backButton(self):
        b1 = tk.Button(self, text="뒤로가기")
        b1.bind("<Button-1>", self.backButtonClicked)
        b1.grid(row=0, column=2)

    def backButtonClicked(self, event):
        # os.chdir("../")  # movie 파일로 이동
        print("시작 화면 : ", os.getcwd())
        print("눌렀음")
        self.master.switch_frame(mp.MainPage)