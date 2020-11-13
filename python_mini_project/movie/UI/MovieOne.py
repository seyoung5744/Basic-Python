import tkinter as tk
import python_mini_project.movie.movieService as ms
import python_mini_project.movie.UI.MovieListPage as sp
import python_mini_project.booking.UI.BookingPage as bp
import python_mini_project.staticString as ss
import os

class PageOne(tk.Frame):
    def __init__(self, master):
        self.service = ms.MovieService()
        self.master = master
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self) #  bg='blue'

        tk.Label(self, text = self.service.getMovieInfo("삼진그룹 영어토익반"), font=('Helvetica', 10, "bold")).place(x = 240, y = 40)
        self.backButton()
        self.bookingButton()

        tk.Button(self, text="종료", command = lambda : master.quit()).place(x = 870, y = 30)

    def bookingButton(self):
        b = tk.Button(self, text = "예매하기")
        b.bind("<Button-1>",self.bookingButtonClicked)
        b.place(x = 480, y = 500)

    def bookingButtonClicked(self, event):
        # os.chdir("../")
        # os.chdir("../")
        print("예매하기 : ", os.getcwd())
        ss.screen = "삼진그룹 영어토익반"
        self.master.switch_frame(bp.bookingPage)

    def backButton(self):
        b1 = tk.Button(self, text="뒤로가기" )
        b1.bind("<Button-1>",self.backButtonClicked)
        b1.place(x = 800, y = 30)

    def backButtonClicked(self, event):
        # os.chdir("../")  # movie 파일로 이동
        print("PageOne : ", os.getcwd())
        print("눌렀음")
        self.master.switch_frame(sp.StartPage)
